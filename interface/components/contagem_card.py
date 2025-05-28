from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt


class ContagemCard(QWidget):
    def __init__(self, contagem):
        super().__init__()

        layout = QVBoxLayout()
        layout.setSpacing(3)
        layout.setContentsMargins(5, 5, 5, 5)

        label_id = QLabel(f"ID: {contagem.id}")
        label_mob = QLabel(f"Mob: {contagem.mob}")
        label_count = QLabel(f"Mortes: {contagem.count}")
        label_data = QLabel(f"Criado em: {contagem.timestamp.strftime('%d/%m/%Y %H:%M:%S')}")

        for label in [label_id, label_mob, label_count, label_data]:
            label.setStyleSheet("font-size: 13px;")

        layout.addWidget(label_id)
        layout.addWidget(label_mob)
        layout.addWidget(label_count)
        layout.addWidget(label_data)

        self.setLayout(layout)
        self.setStyleSheet("""
            background-color: #ecf0f1;
            border-left: 4px solid #3498db;
            padding: 8px;
            margin-bottom: 8px;
            border-radius: 4px;
        """)
