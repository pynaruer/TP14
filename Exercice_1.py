from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QVBoxLayout

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QVBoxLayout()

        self.label = QLabel("label")
        self.button = QPushButton("button")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()
