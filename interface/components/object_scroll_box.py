from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QSizePolicy


class ObjectScrollBox(QWidget):
    def __init__(self, objetos, widget_factory):
        super().__init__()

        layout = QVBoxLayout()
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        content = QWidget()
        content_layout = QVBoxLayout()
        content_layout.setSpacing(10)

        for obj in objetos:
            widget = widget_factory(obj)
            widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            content_layout.addWidget(widget)

        content.setLayout(content_layout)
        scroll.setWidget(content)
        layout.addWidget(scroll)
        self.setLayout(layout)
