import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import classify
import cast

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.buttonImg = QtWidgets.QPushButton("Chose img!")
        self.buttonDownload = QtWidgets.QPushButton("Download")
        self.text = QtWidgets.QLabel("Pokedex!", alignment=QtCore.Qt.AlignTop.AlignHCenter)
        self.img = QtWidgets.QLabel(self, alignment=QtCore.Qt.AlignVCenter.AlignHCenter)
        #self.image = None

        self.initLayout()
        self.buttonImg.clicked.connect(self.openFileDialog)
        self.buttonDownload.clicked.connect(self.download)

    def initLayout(self):
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.img)
        self.layout.addWidget(self.buttonImg)
        self.layout.addWidget(self.buttonDownload)
        self.setLayout(self.layout)

    def openFileDialog(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "./", "Images (*.png *.xpm *.jpg)")
        if(filePath):
            self.showClassification(filePath)

    def showClassification(self, filePath):
        print(filePath)
        classifiedImg = classify.classifyImg("pokedex.model", "lb.pickle", filePath)
        self.image = QtGui.QImage(classifiedImg, classifiedImg.shape[1], classifiedImg.shape[0], classifiedImg.shape[1] * 3, QtGui.QImage.Format_RGB888).rgbSwapped()
        pixmap = QtGui.QPixmap(self.image)
        self.img.setPixmap(pixmap)

    def download(self):
        if(self.image):
            converter = cast.QPixmap2QByteArray()
            QtWidgets.QFileDialog.saveFileContent(converter(self.image), "classified.jpg")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())