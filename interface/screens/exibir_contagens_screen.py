from PySide6.QtWidgets import QWidget, QVBoxLayout
from interface.components.title import Title
from interface.components.back_button import BackButton
from interface.components.object_scroll_box import ObjectScrollBox
from interface.components.contagem_card import ContagemCard

from database.engine import SessionLocal
from database.models.contagem import Contagem


class ExibirContagensScreen(QWidget):
    def __init__(self, navegar_callback):
        super().__init__()
        self.navegar = navegar_callback

        layout = QVBoxLayout()
        layout.setSpacing(15)

        layout.addWidget(BackButton(lambda: self.navegar("home")))
        layout.addWidget(Title("📊 Contagens Ativas"))

        # Carrega contagens do banco
        session = SessionLocal()
        contagens = session.query(Contagem).order_by(Contagem.timestamp.desc()).all()
        session.close()

        # Cria lista de ContagemCards scrolláveis
        scroll_box = ObjectScrollBox(contagens, lambda c: ContagemCard(c))
        layout.addWidget(scroll_box)

        self.setLayout(layout)
