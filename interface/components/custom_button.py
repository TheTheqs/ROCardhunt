from PySide6.QtWidgets import QPushButton


class CustomButton(QPushButton):
    def __init__(self, label: str, on_click):
        super().__init__(label)

        self.setStyleSheet("""
            padding: 10px;
            font-size: 16px;
            background-color: #3498db;
            color: white;
            border-radius: 5px;
        """)

        self.clicked.connect(on_click)
