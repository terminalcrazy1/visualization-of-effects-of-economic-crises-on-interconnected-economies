from PyQt6.QtWidgets import QApplication
from MainWindow import MainWindow

app: QApplication = QApplication([])
window: MainWindow = MainWindow()
window.show()
app.exec()