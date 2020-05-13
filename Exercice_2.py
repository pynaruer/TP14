from PySide2.QtWidgets import QLabel, QWidget, QGridLayout, QApplication, QTextEdit, QPushButton

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout=QGridLayout()
        self.label=QLabel("Laissez un commentaire")
        self.textEdit=QTextEdit()
        self.button_1=QPushButton("Success")
        self.button_2=QPushButton("Exit")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.textEdit)
        self.layout.addWidget(self.button_1)
        self.layout.addWidget(self.button_2)

        self.setWindowTitle("Laisser un commentaire")
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()
