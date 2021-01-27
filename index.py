import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import classify
import cast

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # setting title 
        self.setWindowTitle("CNN-Pokedex")

        self.buttonImg = QtWidgets.QPushButton("Choose img")
        self.buttonDownload = QtWidgets.QPushButton("Download")
        self.text = QtWidgets.QLabel("Pokedex!", alignment=QtCore.Qt.AlignCenter)
        self.errorMessage = QtWidgets.QLabel("Please, first classify an image.", alignment=QtCore.Qt.AlignCenter)
        self.errorMessage.setHidden(True)
        self.img = QtWidgets.QLabel(self, alignment=QtCore.Qt.AlignVCenter.AlignHCenter)
        self.image = None

        self.initLayout()
        self.setStyles()
        self.buttonImg.clicked.connect(self.openFileDialog)
        self.buttonDownload.clicked.connect(self.download)

    def initLayout(self):
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.errorMessage)
        self.layout.addWidget(self.img)
        self.layout.addWidget(self.buttonImg)
        self.layout.addWidget(self.buttonDownload)
        self.setLayout(self.layout)

    def setStyles(self):
        self.text.setFont(QtGui.QFont('Arial', 30))
        self.text.setStyleSheet("background-color: yellow;padding: 0px; margin: 0px;")
        self.errorMessage.setStyleSheet("color: red")

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
        self.errorMessage.setHidden(True)

    def download(self):
        if(self.image):
            converter = cast.QPixmap2QByteArray()
            QtWidgets.QFileDialog.saveFileContent(converter(self.image), "classified.jpg")
        else:
            self.errorMessage.setHidden(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())