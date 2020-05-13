from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setFixedSize(400,300)
        self.setWindowTitle("Charging...")

        self.icon = QIcon("C:\Documents\PyCharm Projects\drapeau-fr.png")
        self.layout = QBoxLayout()
        self.label = QLabel("Hello World")
        self.progressbar = QProgressBar()
        self.lineEdit = QLineEdit()
        self.button = QPushButton("Click me !")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.progressbar)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.button)

        self.setWindowIcon(self.myicon)
        self.label.setAlignment(Qt.AlignCenter)
        self.progressbar.setValue(50)
        self.button.setToolTip("YES CLICK!")
        self.setLayout(self.layout)

if __name__ == "_main_":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()
