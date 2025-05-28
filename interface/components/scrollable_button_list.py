from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QPushButton, QSizePolicy


class ScrollableButtonList(QWidget):
    def __init__(self, items: list[str], on_click):
        super().__init__()

        layout = QVBoxLayout()
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        content_widget = QWidget()
        content_layout = QVBoxLayout()
        content_layout.setSpacing(10)

        for item in items:
            btn = QPushButton(item)
            btn.setStyleSheet("""
                padding: 10px;
                font-size: 14px;
                background-color: #2ecc71;
                color: white;
                border-radius: 6px;
            """)
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            # A função lambda agora aceita o argumento `checked`
            btn.clicked.connect(lambda checked=False, nome=item: on_click(nome))
            content_layout.addWidget(btn)

        content_widget.setLayout(content_layout)
        scroll_area.setWidget(content_widget)
        layout.addWidget(scroll_area)
        self.setLayout(layout)
