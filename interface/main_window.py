from PySide6.QtWidgets import QMainWindow, QStackedWidget
from interface.screens.home_screen import HomeScreen
from interface.screens.nova_contagem_screen import NovaContagemScreen
from interface.screens.retomar_contagem_screen import RetomarContagemScreen
from interface.screens.exibir_contagens_screen import ExibirContagensScreen
from interface.screens.exibir_marcos_screen import ExibirMarcosScreen
from interface.screens.contagem_screen import ContagemScreen


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matheqs CardHunt")
        self.setMinimumSize(500, 300)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Telas
        self.home_screen = HomeScreen(self.ir_para)
        self.nova_contagem_screen = NovaContagemScreen(self.ir_para,  self.set_contagem_id)
        self.retomar_contagem_screen = RetomarContagemScreen(self.ir_para, self.set_contagem_id)
        self.exibir_contagens_screen = ExibirContagensScreen(self.ir_para)
        self.exibir_marcos_screen = ExibirMarcosScreen(self.ir_para)
        self.contagem_screen = ContagemScreen(self.ir_para)

        self.stack.addWidget(self.home_screen)
        self.stack.addWidget(self.nova_contagem_screen)
        self.stack.addWidget(self.retomar_contagem_screen)
        self.stack.addWidget(self.exibir_contagens_screen)
        self.stack.addWidget(self.exibir_marcos_screen)
        self.stack.addWidget(self.contagem_screen)

        self.stack.setCurrentWidget(self.home_screen)

    def ir_para(self, destino: str):
        if destino == "home":
            self.stack.setCurrentWidget(self.home_screen)
        elif destino == "nova_contagem":
            self.stack.setCurrentWidget(self.nova_contagem_screen)
        elif destino == "retomar_contagem":
            self.retomar_contagem_screen.atualizar()
            self.stack.setCurrentWidget(self.retomar_contagem_screen)
        elif destino == "exibir_contagens":
            self.exibir_contagens_screen.atualizar()
            self.stack.setCurrentWidget(self.exibir_contagens_screen)
        elif destino == "exibir_marcos":
            self.exibir_marcos_screen.atualizar()
            self.stack.setCurrentWidget(self.exibir_marcos_screen)
        elif destino == "contagem_screen":
            self.stack.setCurrentWidget(self.contagem_screen)

    def set_contagem_id(self, contagem_id: int):
        self.contagem_screen.carregar_contagem(contagem_id)
        self.ir_para("contagem_screen")
