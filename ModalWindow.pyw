from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QRegion, QPolygon, QPalette, QBrush, QPixmap
from PyQt6.QtCore import QPoint, Qt

class ModalTypeA(QDialog):
    def modalTypeA(self, parent=None):
        self.setWindowTitle("Модальное окно 1")
        self.setModal(True)
        self.setGeometry(100, 100, 300, 300)
        self.setWindowOpacity(0.6)
        palette = self.palette()
        palette.setBrush(QPalette.ColorGroup.Normal, QPalette.ColorRole.Window, 
                        QBrush(QPixmap("Image/Bonk.jpg").scaled(self.size(), Qt.AspectRatioMode.IgnoreAspectRatio)))
        self.setPalette(palette)
        polygon = QPolygon([QPoint(0, 300), QPoint(150, 0), QPoint(300, 300)])
        region = QRegion(polygon)
        self.setMask(region)
        self.label = QLabel("<center><i><br><br><br><br>Треугольное модальное окно</i></center>")
        self.btnQuit = QPushButton("&Закрыть окно")
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)
        self.btnQuit.clicked.connect(self.close)
        self.move(1000, 250)
        self.exec()
    
class ModalTypeB(QDialog):
    def modalTypeB(self, parent=None):
        self.setWindowTitle("Модальное окно 2")
        self.setModal(True)
        self.label = QLabel("<center>Модальное окно считывающие нажатия</center>")
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)
        self.exec()

    def keyPressEvent(self, event):
            if event.key() == Qt.Key.Key_Escape:
                self.label.setText("Нажата клавиша Escape")
                self.close()
            elif event.key() == Qt.Key.Key_Enter or event.key() == Qt.Key.Key_Return:
                self.label.setText("Нажата клавиша Enter")
            else:
                self.label.setText(f"Нажата клавиша: {event.text()}")

if __name__ == "__main__":
    app = QApplication([])
    modal = ModalTypeA()
    window = QPushButton("открыть модальное окно")
    window.clicked.connect(modal.modalTypeA)
    window.show()
    app.exec()