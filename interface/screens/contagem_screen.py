from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QMessageBox
from interface.components.title import Title
import os
from interface.components.custom_button import CustomButton
from interface.components.img import Img
from interface.components.counter_display import CounterDisplay
from interface.components.back_button import BackButton
from service.get_gif_service import GetGifService

from database.engine import SessionLocal
from database.models.contagem import Contagem

import threading
import keyboard


class ContagemScreen(QWidget):
    def __init__(self, navegar_callback):
        super().__init__()
        self.navegar = navegar_callback
        self.contagem = None
        self.valor = 0

        layout = QVBoxLayout()
        layout.setSpacing(15)

        layout.addWidget(BackButton(lambda: self.navegar("home")))
        layout.addWidget(Title("🔥 Contagem Ativa"))

        self.img = Img()
        layout.addWidget(self.img)

        self.counter_display = CounterDisplay()
        layout.addWidget(self.counter_display)

        btn_marco = CustomButton("🏁 Criar Marco", self.criar_marco)
        layout.addWidget(btn_marco)

        layout.addWidget(QLabel("🖱️ Aperte F1 para aumentar a contagem."))

        self.setLayout(layout)

        # Escutador global de F1
        threading.Thread(target=self._escutar_f1, daemon=True).start()

    def carregar_contagem(self, contagem_id: int):
        session = SessionLocal()
        self.contagem = session.query(Contagem).filter(Contagem.id == contagem_id).first()
        session.close()

        if self.contagem:
            self.valor = self.contagem.count
            self.counter_display.set_valor(self.valor)

            # Tenta carregar gif local, senão busca online
            gif_path = os.path.join("assets", f"{self.contagem.mob}.gif")
            if not os.path.exists(gif_path):
                gif_path = GetGifService.get_gif(self.contagem.mob)

            if gif_path:
                self.layout().removeWidget(self.img)
                self.img.deleteLater()
                self.img = Img(gif_path=gif_path)
                self.layout().insertWidget(1, self.img)

    def _escutar_f1(self):
        keyboard.add_hotkey("F1", lambda: self._incrementar())

    def _incrementar(self):
        if not self.contagem:
            return

        self.contagem.count += 1
        self.counter_display.set_valor(self.contagem.count)

        # Persistência no banco
        from database.engine import SessionLocal
        session = SessionLocal()
        try:
            contagem_db = session.query(Contagem).filter_by(id=self.contagem.id).first()
            if contagem_db:
                contagem_db.count = self.contagem.count
                session.commit()
        finally:
            session.close()

    def criar_marco(self):
        from database.models.marco import Marco
        from database.models.contagem import Contagem
        from database.engine import SessionLocal

        session = SessionLocal()
        try:
            # Armazena o valor atual ANTES de zerar
            valor_atual = self.valor
            valor_display = 0
            # Cria o novo marco com o valor atual
            if self.contagem is not None:
                marco = Marco.create(self=Marco(), contagem=self.contagem)
                session.add(marco)
                valor_display = marco.count
                session.commit()

            # Reseta a contagem no banco
            contagem_db = session.query(Contagem).filter_by(id=self.contagem.id).first()
            if contagem_db:
                contagem_db.count = 0
                self.contagem.count = 0  # Atualiza a cópia local

            session.commit()

            # Atualiza a interface
            self.counter_display.set_valor(0)
            self.valor = 0

            QMessageBox.information(self, "Marco", f"Marco criado com {valor_display} mortes registradas!")

        finally:
            session.close()

