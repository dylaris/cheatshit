from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys

class WindowDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("window demo")
        self.setGeometry(100, 100, 640, 480)
        self.setMinimumSize(600, 400)
        self.setWindowIcon(QIcon("jellyfish.png"))
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WindowDemo()
    window.show()
    sys.exit(app.exec_())
