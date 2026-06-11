from MainWindow import MainWindow
from PyQt6.QtWidgets import QApplication

app: QApplication = QApplication([])
window: MainWindow = MainWindow()
window.show()
app.exec()