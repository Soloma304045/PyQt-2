from PyQt6.QtWidgets import QApplication
from MainWindow import MainWindow # type: ignore

app = QApplication([])
window = MainWindow()
window.setWindowTitle("Главное окно")
window.resize(450, 520)
window.show()
app.exec()