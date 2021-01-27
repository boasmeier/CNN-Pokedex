import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import classify

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.buttonImg = QtWidgets.QPushButton("Chose img!")
        self.text = QtWidgets.QLabel("Pokedex!", alignment=QtCore.Qt.AlignTop.AlignHCenter)
        self.img = QtWidgets.QLabel(self, alignment=QtCore.Qt.AlignVCenter.AlignHCenter)

        self.initLayout()
        self.buttonImg.clicked.connect(self.openFileDialog)

    def initLayout(self):
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.img)
        self.layout.addWidget(self.buttonImg)
        self.setLayout(self.layout)

    def openFileDialog(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "./", "Images (*.png *.xpm *.jpg)")
        if(filePath):
            self.showClassification(filePath)

    def showClassification(self, filePath):
        print(filePath)
        self.pixmap = QtGui.QPixmap(filePath)
        self.img.setPixmap(self.pixmap)
        classifiedImg = classify.classifyImg("pokedex.model", "lb.pickle", filePath)
        self.img.setPixmap(classifiedImg)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())