from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit


class TextInput(QWidget):
    def __init__(self, titulo: str, placeholder: str = "", valor_inicial: str = ""):
        super().__init__()

        layout = QVBoxLayout()
        layout.setSpacing(5)

        label = QLabel(titulo)
        label.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(label)

        self.input = QLineEdit()
        self.input.setPlaceholderText(placeholder)
        self.input.setText(valor_inicial)
        self.input.setStyleSheet("""
            padding: 8px;
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 4px;
        """)
        layout.addWidget(self.input)

        self.setLayout(layout)

    def get_text(self):
        return self.input.text()

    def set_text(self, text: str):
        self.input.setText(text)
