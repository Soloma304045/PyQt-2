from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QIcon
from ModalWindow import ModalTypeA, ModalTypeB # type: ignore

class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.modalA = ModalTypeA()
        self.modalB = ModalTypeB()
        self.setWindowIcon(QIcon("Image/Pepe.jpg"))
        self.label = QLabel('''
            <center>
                <h1>Лабораторная работа №2</h1><br>
                <b>Работа с окнами. Обработка сигналов и событий</b><br>
                Выполнил студент группы <span style="color: red;">ИТД-21<br>
                <h2>Чайдаков Иван Миронович</h2></span>
            </center>
        ''')
        modalButton_1 = QPushButton("Модальное окно 1")
        modalButton_1.setToolTip("Модальное окно треугольной формы")
        modalButton_2 = QPushButton("Модальное окно 2")
        modalButton_2.setToolTip("Модальное окно считывающие клавиши")
        self.btnQuit = QPushButton("&Закрыть окно")
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(modalButton_1)
        self.vbox.addWidget(modalButton_2)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)
        modalButton_1.clicked.connect(self.modalA.modalTypeA)
        modalButton_2.clicked.connect(self.modalB.modalTypeB)
        self.btnQuit.clicked.connect(QApplication.instance().quit)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Главное окно")
    window.resize(300, 70)
    window.show()
    sys.exit(app.exec())