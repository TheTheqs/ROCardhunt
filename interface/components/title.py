from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class Title(QLabel):
    def __init__(self, texto: str):
        super().__init__(texto)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        self.setStyleSheet("color: #2c3e50; margin-top: 20px;")
