from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class MarcoCard(QWidget):
    def __init__(self, marco):
        super().__init__()

        layout = QVBoxLayout()
        layout.setSpacing(3)
        layout.setContentsMargins(5, 5, 5, 5)

        label_id = QLabel(f"ID: {marco.id}")
        label_mob = QLabel(f"Mob: {marco.mob}")
        label_count = QLabel(f"Mortes até o drop: {marco.count}")

        data_inicio = marco.timestamp_inicio.strftime('%d/%m/%Y %H:%M:%S')
        label_inicio = QLabel(f"Início: {data_inicio}")

        if marco.timestamp_fim:
            data_fim = marco.timestamp_fim.strftime('%d/%m/%Y %H:%M:%S')
            duracao = marco.timestamp_fim - marco.timestamp_inicio
            dias = duracao.days
            horas = duracao.seconds // 3600
            minutos = (duracao.seconds % 3600) // 60
            duracao_str = f"{dias}d {horas}h {minutos}min"
        else:
            data_fim = "Em aberto"
            duracao_str = "Ainda em andamento"

        label_fim = QLabel(f"Fim: {data_fim}")
        label_duracao = QLabel(f"Duração: {duracao_str}")

        for label in [label_id, label_mob, label_count, label_inicio, label_fim, label_duracao]:
            label.setStyleSheet("font-size: 13px;")

        layout.addWidget(label_id)
        layout.addWidget(label_mob)
        layout.addWidget(label_count)
        layout.addWidget(label_inicio)
        layout.addWidget(label_fim)
        layout.addWidget(label_duracao)

        self.setLayout(layout)
        self.setStyleSheet("""
            background-color: #f8f9fa;
            border-left: 4px solid #9b59b6;
            padding: 8px;
            margin-bottom: 8px;
            border-radius: 4px;
        """)
