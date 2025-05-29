from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from interface.components.title import Title
from interface.components.custom_button import CustomButton

class HomeScreen(QWidget):
    def __init__(self, navegar_callback):
        super().__init__()
        self.navegar = navegar_callback

        layout = QVBoxLayout()
        layout.setSpacing(25)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        title = Title("🎯 BEM-VINDO AO Matheqs CardHunt!")
        subtitle = Title("🛠️ Versão 1.1")
        layout.addWidget(title)
        layout.addWidget(subtitle)

        # Botões com callbacks placeholders (você conecta depois)
        btn_nova = CustomButton("📥 Nova Contagem", lambda: self.navegar("nova_contagem"))
        btn_retomar = CustomButton("♻️ Retomar Contagem", lambda: self.navegar("retomar_contagem"))
        btn_exibir = CustomButton("📊 Exibir Contagens", lambda: self.navegar("exibir_contagens"))
        btn_marcos = CustomButton("🏁 Exibir Marcos", lambda: self.navegar("exibir_marcos"))

        layout.addWidget(btn_nova)
        layout.addWidget(btn_retomar)
        layout.addWidget(btn_exibir)
        layout.addWidget(btn_marcos)

        self.setLayout(layout)
