from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout


class ConfirmDeleteModal(QDialog):
    def __init__(self, pergunta: str, placeholder: str, callback_confirm, callback_cancel=None):
        super().__init__()
        self.setWindowTitle("Confirmação")
        self.setModal(True)
        self.callback_confirm = callback_confirm
        self.callback_cancel = callback_cancel

        layout = QVBoxLayout()
        layout.addWidget(QLabel(pergunta))

        self.input = QLineEdit()
        self.input.setPlaceholderText(placeholder)
        layout.addWidget(self.input)

        btn_layout = QHBoxLayout()

        btn_confirmar = QPushButton("✅ Confirmar")
        btn_confirmar.clicked.connect(self.on_confirmar)
        btn_layout.addWidget(btn_confirmar)

        btn_cancelar = QPushButton("❌ Cancelar")
        btn_cancelar.clicked.connect(self.reject)
        btn_layout.addWidget(btn_cancelar)

        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def on_confirmar(self):
        id_str = self.input.text().strip()
        if id_str and self.callback_confirm:
            self.callback_confirm(id_str)
        self.accept()
