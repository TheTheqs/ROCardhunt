from PySide6.QtWidgets import QWidget, QVBoxLayout, QMessageBox, QPushButton
from interface.components.title import Title
from interface.components.back_button import BackButton
from interface.components.object_scroll_box import ObjectScrollBox
from interface.components.confirm_delete_modal import ConfirmDeleteModal
from interface.components.marco_card import MarcoCard

from database.engine import SessionLocal
from database.models.marco import Marco


class ExibirMarcosScreen(QWidget):
    def __init__(self, navegar_callback):
        super().__init__()
        self.navegar = navegar_callback

        self.layout_principal = QVBoxLayout()
        self.layout_principal.setSpacing(15)

        self.layout_principal.addWidget(BackButton(lambda: self.navegar("home")))
        self.layout_principal.addWidget(Title("🏁 Marcos de Drop"))

        # Área dinâmica para scroll box
        self.scroll_box_widget = QWidget()
        self.scroll_box_layout = QVBoxLayout()
        self.scroll_box_widget.setLayout(self.scroll_box_layout)
        self.layout_principal.addWidget(self.scroll_box_widget)

        # Botão "Deletar"
        btn_deletar = QPushButton("🗑️ Deletar Marco")
        btn_deletar.clicked.connect(self.abrir_modal_deletar)
        self.layout_principal.addWidget(btn_deletar)

        self.setLayout(self.layout_principal)

        # Primeira carga
        self.atualizar()

    def atualizar(self):
        # Limpa widgets antigos
        for i in reversed(range(self.scroll_box_layout.count())):
            widget = self.scroll_box_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        # Recarrega dados
        session = SessionLocal()
        marcos = session.query(Marco).order_by(Marco.timestamp_inicio.desc()).all()
        session.close()

        scroll_box = ObjectScrollBox(marcos, lambda m: MarcoCard(m))
        self.scroll_box_layout.addWidget(scroll_box)

    def abrir_modal_deletar(self):
        def deletar_por_id(id_str):
            try:
                id_int = int(id_str)
                session = SessionLocal()
                marco = session.query(Marco).filter(Marco.id == id_int).first()
                if marco:
                    session.delete(marco)
                    session.commit()
                    QMessageBox.information(self, "Sucesso", f"Marco #{id_int} deletado!")
                    self.atualizar()  # recarrega dinamicamente
                else:
                    QMessageBox.warning(self, "Não encontrado", f"Nenhum marco com ID {id_int}.")
                session.close()
            except ValueError:
                QMessageBox.warning(self, "Erro", "ID inválido.")

        modal = ConfirmDeleteModal("Digite o ID do marco a ser deletado:", "Ex: 3", deletar_por_id)
        modal.exec()
