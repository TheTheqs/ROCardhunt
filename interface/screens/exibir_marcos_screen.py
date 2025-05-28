from PySide6.QtWidgets import QWidget, QVBoxLayout
from interface.components.title import Title
from interface.components.back_button import BackButton
from interface.components.object_scroll_box import ObjectScrollBox
from interface.components.marco_card import MarcoCard

from database.engine import SessionLocal
from database.models.marco import Marco


class ExibirMarcosScreen(QWidget):
    def __init__(self, navegar_callback):
        super().__init__()
        self.navegar = navegar_callback

        layout = QVBoxLayout()
        layout.setSpacing(15)

        layout.addWidget(BackButton(lambda: self.navegar("home")))
        layout.addWidget(Title("🏁 Marcos de Drop"))

        # Carrega marcos do banco
        session = SessionLocal()
        marcos = session.query(Marco).order_by(Marco.timestamp_inicio.desc()).all()
        session.close()

        # Cria lista scrollável de marcos
        scroll_box = ObjectScrollBox(marcos, lambda m: MarcoCard(m))
        layout.addWidget(scroll_box)

        self.setLayout(layout)
