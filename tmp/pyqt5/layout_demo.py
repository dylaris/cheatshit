from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QGridLayout, QPushButton, QLineEdit, QLabel)
import sys

class VBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("vertical box demo")
        self.setGeometry(100, 100, 640, 480)

        layout = QVBoxLayout()
        layout.addWidget(QPushButton("button1"))
        layout.addWidget(QPushButton("button2"))
        layout.addWidget(QPushButton("button3"))
        layout.addStretch()
        self.setLayout(layout)

class HBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("horizontal box demo")
        self.setGeometry(100, 100, 640, 480)

        layout = QHBoxLayout()
        layout.addWidget(QLabel("name:"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QPushButton("search"))
        layout.addStretch()
        self.setLayout(layout)

class GridDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("grid demo")
        self.setGeometry(100, 100, 640, 480)

        layout = QGridLayout()
        layout.addWidget(QLabel("username:"), 0, 0)
        layout.addWidget(QLineEdit(), 0, 1)
        layout.addWidget(QLabel("password:"), 1, 0)
        layout.addWidget(QLineEdit(), 1, 1)
        layout.addWidget(QPushButton("login"), 2, 0, 1, 2)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    vbox = VBoxDemo()
    hbox = HBoxDemo()
    grid = GridDemo()

    vbox.show()
    hbox.show()
    grid.show()

    sys.exit(app.exec_())
