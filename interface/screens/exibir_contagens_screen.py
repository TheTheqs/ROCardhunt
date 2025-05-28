from PySide6.QtWidgets import QWidget, QVBoxLayout, QMessageBox, QPushButton
from interface.components.title import Title
from interface.components.back_button import BackButton
from interface.components.object_scroll_box import ObjectScrollBox
from interface.components.confirm_delete_modal import ConfirmDeleteModal
from interface.components.contagem_card import ContagemCard

from database.engine import SessionLocal
from database.models.contagem import Contagem


class ExibirContagensScreen(QWidget):
    def __init__(self, navegar_callback):
        super().__init__()
        self.navegar = navegar_callback

        self.layout_principal = QVBoxLayout()
        self.layout_principal.setSpacing(15)

        self.layout_principal.addWidget(BackButton(lambda: self.navegar("home")))
        self.layout_principal.addWidget(Title("📊 Contagens Ativas"))

        # Espaço reservado para a scroll box dinâmica
        self.scroll_box_widget = QWidget()
        self.scroll_box_layout = QVBoxLayout()
        self.scroll_box_widget.setLayout(self.scroll_box_layout)
        self.layout_principal.addWidget(self.scroll_box_widget)

        # Botão de deletar
        btn_deletar = QPushButton("🗑️ Deletar Contagem")
        btn_deletar.clicked.connect(self.abrir_modal_deletar)
        self.layout_principal.addWidget(btn_deletar)

        self.setLayout(self.layout_principal)

        # Carrega pela primeira vez
        self.atualizar()

    def atualizar(self):
        # Limpa a área da scroll box antes de recarregar
        for i in reversed(range(self.scroll_box_layout.count())):
            widget = self.scroll_box_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        # Recarrega do banco
        session = SessionLocal()
        contagens = session.query(Contagem).order_by(Contagem.timestamp.desc()).all()
        session.close()

        # Recria a scroll box com os dados atualizados
        scroll_box = ObjectScrollBox(contagens, lambda c: ContagemCard(c))
        self.scroll_box_layout.addWidget(scroll_box)

    def abrir_modal_deletar(self):
        def deletar_por_id(id_str):
            try:
                id_int = int(id_str)
                session = SessionLocal()
                contagem = session.query(Contagem).filter(Contagem.id == id_int).first()
                if contagem:
                    session.delete(contagem)
                    session.commit()
                    QMessageBox.information(self, "Sucesso", f"Contagem #{id_int} deletada!")
                    self.atualizar()  # atualiza em vez de navegar
                else:
                    QMessageBox.warning(self, "Não encontrado", f"Nenhuma contagem com ID {id_int}.")
                session.close()
            except ValueError:
                QMessageBox.warning(self, "Erro", "ID inválido.")

        modal = ConfirmDeleteModal("Digite o ID da contagem a ser deletada:", "Ex: 3", deletar_por_id)
        modal.exec()
