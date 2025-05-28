from PySide6.QtWidgets import QWidget, QVBoxLayout, QMessageBox
from interface.components.title import Title
from interface.components.back_button import BackButton
from interface.components.scrollable_button_list import ScrollableButtonList

from database.engine import SessionLocal
from database.models.contagem import Contagem


class RetomarContagemScreen(QWidget):
    def __init__(self, navegar_callback):
        super().__init__()
        self.navegar = navegar_callback

        layout = QVBoxLayout()
        layout.setSpacing(15)

        layout.addWidget(BackButton(lambda: self.navegar("home")))
        layout.addWidget(Title("♻️ Retomar Contagem"))

        self.btn_list = ScrollableButtonList([], self.handle_retomar)
        layout.addWidget(self.btn_list)

        self.setLayout(layout)
        self.carregar_contagens()

    def carregar_contagens(self):
        session = SessionLocal()
        contagens = session.query(Contagem).all()
        nomes = [f"{c.mob} (#{c.id})" for c in contagens]
        session.close()

        # Recria o componente com os dados
        self.btn_list.setParent(None)
        self.btn_list = ScrollableButtonList(nomes, self.handle_retomar)
        self.layout().addWidget(self.btn_list)

    def handle_retomar(self, nome):
        QMessageBox.information(self, "Placeholder", f"Você escolheu: {nome}")
        # self.navegar("count_screen", id_contagem)
