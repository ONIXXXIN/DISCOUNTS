import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bababoui")
        self.setGeometry(1200, 300, 500, 600)
        self.setStyleSheet("background-color:#000000")

        # Кнопка
        self.lolikhopter = QPushButton("nolik", self)
        self.lolikhopter.setGeometry(130, 200, 300, 100)  # Уменьшил размеры, чтобы оставить место
        self.lolikhopter.clicked.connect(self.score)
        self.lolikhopter.setStyleSheet("""
        QPushButton {
            font-size: 40px;
            background-color: #f8fc00;
            color: black;
            border-radius: 25% 
        }
        QPushButton:hover {
            font-size: 40px;
            background-color: #d6d918;
            color: black;
            border-radius: 35% 
        }
        QPushButton:pressed {
            font-size: 50px;
            background-color: #aba732;
            color: black;
            border-radius: 40% 
        }
        """)

        # Метка с текстом
        self.label = QLabel("Введите текст:", self)
        self.label.setGeometry(50, 50, 200, 30)
        self.label.setStyleSheet("color: white; font-size: 16px;")

        # Поле ввода
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(200, 50, 200, 30)
        self.input_field.setStyleSheet("""
                QLineEdit {
                    font-size: 40px;
                    background-color: #f8fc00;
                    color: black;
                    border-radius: 25%;
                }
                QLineEdit:hover {
                    font-size: 40px;
                    background-color: #d6d918;
                    color: black;
                    border-radius: 35%;
                }
                QLineEdit:focus {
                    font-size: 50px;
                    background-color: #aba732;
                    color: black;
                    border-radius: 40px;
                }
                """)

    def score(self):
        print("no")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()