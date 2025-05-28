from PySide6.QtWidgets import QWidget, QVBoxLayout, QMessageBox
from interface.components.title import Title
from interface.components.custom_button import CustomButton
from interface.components.text_input import TextInput
from interface.components.back_button import BackButton

from database.engine import SessionLocal
from database.models.contagem import Contagem


class NovaContagemScreen(QWidget):
    def __init__(self, navegar_callback, set_contagem_callback):
        super().__init__()
        self.navegar = navegar_callback
        self.set_contagem_id = set_contagem_callback

        layout = QVBoxLayout()
        layout.setSpacing(15)

        layout.addWidget(BackButton(lambda: self.navegar("home")))
        layout.addWidget(Title("🆕 Nova Contagem"))

        self.input_mob = TextInput("Nome do monstro", "Ex: Hunter Fly")
        layout.addWidget(self.input_mob)

        self.btn_criar = CustomButton("✅ Iniciar Contagem", self.salvar_contagem)
        layout.addWidget(self.btn_criar)

        layout.addStretch()
        self.setLayout(layout)

    def salvar_contagem(self):
        nome = self.input_mob.get_text().strip()

        if not nome:
            QMessageBox.warning(self, "Erro", "Digite o nome do monstro.")
            return

        session = SessionLocal()
        nova = Contagem(mob=nome)
        session.add(nova)
        session.commit()
        session.refresh(nova)
        self.set_contagem_id(nova.id)

        QMessageBox.information(self, "Sucesso", f"Contagem criada para '{nome}'!")
        self.set_contagem_id(nova.id)
