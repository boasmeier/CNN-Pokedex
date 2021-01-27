import sys
import random

from PySide6 import QtCore, QtWidgets, QtGui



class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
        self.button = QtWidgets.QPushButton("Click me!")
        self.buttonImg = QtWidgets.QPushButton("Chose img!")
        self.text = QtWidgets.QLabel("Pokedex!", alignment=QtCore.Qt.AlignTop.AlignHCenter)
        self.img = QtWidgets.QLabel(self)

        self.initFileDialog()
        self.initLayout()
        
        self.button.clicked.connect(self.magic)
        self.buttonImg.clicked.connect(self.openFileDialog)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

    def initLayout(self):
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.img)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.buttonImg)
        self.setLayout(self.layout)

    def initFileDialog(self):
        self.dialog = QtWidgets.QFileDialog(self)
        self.dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        self.dialog.setViewMode(QtWidgets.QFileDialog.Detail)
        self.dialog.setNameFilter("Images (*.png *.xpm *.jpg)")

    def openFileDialog(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "./", "Images (*.png *.xpm *.jpg)")
        if(filePath):
            print(filePath)
            self.pixmap = QtGui.QPixmap(filePath)
            self.img.setPixmap(self.pixmap)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())