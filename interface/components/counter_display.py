from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt


class CounterDisplay(QLabel):
    def __init__(self, valor=0):
        super().__init__(str(valor))
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("""
            font-size: 40px;
            font-weight: bold;
            color: #34495e;
            padding: 10px;
        """)

    def set_valor(self, valor: int):
        self.setText(str(valor))
