from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt


class BackButton(QWidget):
    def __init__(self, on_back):
        super().__init__()

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # remove padding
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        button = QPushButton("🔙")
        button.setStyleSheet("""
            padding: 6px;
            font-size: 14px;
            background-color: #bdc3c7;
            color: black;
            border-radius: 5px;
            max-width: 50px;
        """)
        button.clicked.connect(on_back)

        layout.addWidget(button)
        self.setLayout(layout)