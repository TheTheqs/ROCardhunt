from PySide6.QtWidgets import QWidget, QVBoxLayout, QMessageBox
from interface.components.title import Title
from interface.components.back_button import BackButton
from interface.components.scrollable_button_list import ScrollableButtonList

from database.engine import SessionLocal
from database.models.contagem import Contagem


class RetomarContagemScreen(QWidget):
    def __init__(self, navegar_callback, set_contagem_callback):
        super().__init__()
        self.navegar = navegar_callback
        self.set_contagem_id = set_contagem_callback

        self.layout_principal = QVBoxLayout()
        self.layout_principal.setSpacing(15)

        self.layout_principal.addWidget(BackButton(lambda: self.navegar("home")))
        self.layout_principal.addWidget(Title("♻️ Retomar Contagem"))

        self.btn_list = ScrollableButtonList([], self.handle_retomar)
        self.layout_principal.addWidget(self.btn_list)

        self.setLayout(self.layout_principal)

        self.atualizar()

    def atualizar(self):
        session = SessionLocal()
        contagens = session.query(Contagem).all()
        session.close()

        nomes = [f"{c.mob} (#{c.id})" for c in contagens]

        # Atualiza lista de botões
        self.layout_principal.removeWidget(self.btn_list)
        self.btn_list.deleteLater()
        self.btn_list = ScrollableButtonList(nomes, self.handle_retomar)
        self.layout_principal.addWidget(self.btn_list)

    def handle_retomar(self, label: str):
        try:
            id_str = label.split("#")[1].replace(")", "").strip()
            self.set_contagem_id(int(id_str))
        except Exception:
            QMessageBox.warning(self, "Erro", "Não foi possível identificar o ID.")
