from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QMovie, QPixmap
from PySide6.QtCore import Qt
import os

class Img(QLabel):
    def __init__(self, gif_path=None):
        super().__init__()
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFixedHeight(180)

        if gif_path and os.path.exists(gif_path):
            movie = QMovie(gif_path)
            self.setMovie(movie)
            movie.start()
        else:
            self.setPixmap(QPixmap("assets/image_not_found.png").scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio))
