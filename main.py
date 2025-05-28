import sys
from PySide6.QtWidgets import QApplication
from interface.main_window import MainWindow
from database.engine import init_db

if __name__ == "__main__":
    # Inicializa o banco de dados
    init_db()

    # Inicializa a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
