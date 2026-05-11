import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QTextEdit, QComboBox, QCheckBox, QRadioButton, QSlider,
                             QSpinBox, QProgressBar, QListWidget, QTableWidget,
                             QTabWidget, QButtonGroup, QTableWidgetItem, QVBoxLayout)
from PyQt5.QtCore import Qt

class LabelDemo(QWidget):
  def __init__(self):
        super().__init__()
        self.setWindowTitle("label demo")
        self.setGeometry(100, 100, 640, 480)

class LineEditDemo(QWidget):
  def __init__(self):
        super().__init__()
        self.setWindowTitle("line edit demo")
        self.setGeometry(100, 100, 640, 480)

class ButtonDemo(QWidget):
  def __init__(self):
        super().__init__()
        self.setWindowTitle("button demo")
        self.setGeometry(100, 100, 640, 480)

class ComboBoxDemo(QWidget):
  def __init__(self):
        super().__init__()
        self.setWindowTitle("combo box demo")
        self.setGeometry(100, 100, 640, 480)

class CheckBoxDemo(QWidget):
  def __init__(self):
        super().__init__()
        self.setWindowTitle("check box demo")
        self.setGeometry(100, 100, 640, 480)

class RadioButtonDemo(QWidget):
  def __init__(self):
        super().__init__()
        self.setWindowTitle("radio button demo")
        self.setGeometry(100, 100, 640, 480)

class SliderDemo(QWidget):
  def __init__(self):
        super().__init__()
        self.setWindowTitle("slider demo")
        self.setGeometry(100, 100, 640, 480)

class ListWidgetDemo(QWidget):
  def __init__(self):
        super().__init__()
        self.setWindowTitle("list widget demo")
        self.setGeometry(100, 100, 640, 480)

class TableWidgetDemo(QWidget):
  def __init__(self):
        super().__init__()
        self.setWindowTitle("table widget demo")
        self.setGeometry(100, 100, 640, 480)

class LabelDemo(QWidget):
  def __init__(self):
        super().__init__()
        self.setWindowTitle("label demo")
        self.setGeometry(100, 100, 640, 480)

class LabelDemo(QWidget):
  def __init__(self):
        super().__init__()
        self.setWindowTitle("label demo")
        self.setGeometry(100, 100, 640, 480)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    demo_classes = [
        LabelDemo, LineEditDemo, ButtonDemo, ComboBoxDemo,
        CheckBoxDemo, RadioButtonDemo, SliderDemo,
        ListWidgetDemo, TableWidgetDemo
    ]

    for demo_class in demo_classes:
        window = demo_class()
        window.show()

    sys.exit(app.exec_())

