from PySide6.QtWidgets import QWidget, QVBoxLayout, QMessageBox
from interface.components.title import Title
from interface.components.custom_button import CustomButton
from interface.components.text_input import TextInput
from interface.components.back_button import BackButton

from database.engine import SessionLocal
from database.models.contagem import Contagem


class NovaContagemScreen(QWidget):
    def __init__(self, navegar_callback, set_contagem_callback):
        super().__init__()
        self.navegar = navegar_callback
        self.set_contagem_id = set_contagem_callback

        layout = QVBoxLayout()
        layout.setSpacing(15)

        layout.addWidget(BackButton(lambda: self.navegar("home")))
        layout.addWidget(Title("🆕 Nova Contagem"))

        self.input_mob = TextInput("Nome do monstro", "Ex: Mosca Caçadora")
        layout.addWidget(self.input_mob)

        self.input_item = TextInput("Item buscado", "Ex: Carta Mosca Caçadora")
        layout.addWidget(self.input_item)

        self.input_chance = TextInput("Chance de drop (%)", "Ex: 0.02")
        layout.addWidget(self.input_chance)

        self.btn_criar = CustomButton("✅ Iniciar Contagem", self.salvar_contagem)
        layout.addWidget(self.btn_criar)

        layout.addStretch()
        self.setLayout(layout)

    def salvar_contagem(self):
        nome = self.input_mob.get_text().strip()
        item = self.input_item.get_text().strip()
        chance_raw = self.input_chance.get_text().strip()

        if not nome:
            QMessageBox.warning(self, "Erro", "Digite o nome do monstro.")
            return

        # Filtragem e correção silenciosa da chance
        chance_filtrada = self._sanitizar_chance(chance_raw)
        chance_valor = min(chance_filtrada, 99.99)  # Garante que cabe em Numeric(5,2)

        session = SessionLocal()
        try:
            nova = Contagem(
                mob=nome,
                item=item,
                chance=chance_valor
            )
            session.add(nova)
            session.commit()
            session.refresh(nova)

            QMessageBox.information(self, "Sucesso", f"Contagem criada para '{nome}'!")
            self.set_contagem_id(nova.id)

        finally:
            session.close()

    def _sanitizar_chance(self, texto: str) -> float:
        """Sanitiza e converte o valor da chance em float, tolerando vírgula e excesso de símbolos."""
        texto = texto.replace(",", ".")
        permitido = "0123456789."
        filtrado = ''.join(c for c in texto if c in permitido)

        # Garante apenas um ponto decimal
        partes = filtrado.split(".")
        if len(partes) > 2:
            partes = partes[:2]  # ignora excessos
        filtrado = ".".join(partes)

        try:
            valor = float(filtrado)
        except ValueError:
            valor = 0.0

        return round(valor, 2)
