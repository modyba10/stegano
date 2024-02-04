from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import lsb.lsb as stego
import fitz  # PyMuPDF

class pdf_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Partie "Code"
        self.groupBoxCode = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxCode.setGeometry(QtCore.QRect(20, 20, 350, 500))
        self.groupBoxCode.setTitle("Code")

        self.labelImageCode = QtWidgets.QLabel(self.groupBoxCode)
        self.labelImageCode.setGeometry(QtCore.QRect(20, 30, 120, 30))
        self.labelImageCode.setText("Image:")
        self.lineEditImageCode = QtWidgets.QLineEdit(self.groupBoxCode)
        self.lineEditImageCode.setGeometry(QtCore.QRect(150, 30, 150, 30))
        self.buttonBrowseImageCode = QtWidgets.QPushButton(self.groupBoxCode)
        self.buttonBrowseImageCode.setGeometry(QtCore.QRect(310, 30, 30, 30))
        self.buttonBrowseImageCode.setText("...")
        self.buttonBrowseImageCode.clicked.connect(self.browseImageCode)

        self.labelPDFCode = QtWidgets.QLabel(self.groupBoxCode)
        self.labelPDFCode.setGeometry(QtCore.QRect(20, 80, 120, 30))
        self.labelPDFCode.setText("PDF:")
        self.lineEditPDFCode = QtWidgets.QLineEdit(self.groupBoxCode)
        self.lineEditPDFCode.setGeometry(QtCore.QRect(150, 80, 150, 30))
        self.buttonBrowsePDFCode = QtWidgets.QPushButton(self.groupBoxCode)
        self.buttonBrowsePDFCode.setGeometry(QtCore.QRect(310, 80, 30, 30))
        self.buttonBrowsePDFCode.setText("...")
        self.buttonBrowsePDFCode.clicked.connect(self.browsePDFCode)

        self.labelKeyGenerate = QtWidgets.QLabel(self.groupBoxCode)
        self.labelKeyGenerate.setGeometry(QtCore.QRect(20, 130, 120, 30))
        self.labelKeyGenerate.setText("Key Generate:")
        self.lineEditKeyGenerate = QtWidgets.QLineEdit(self.groupBoxCode)
        self.lineEditKeyGenerate.setGeometry(QtCore.QRect(150, 130, 150, 30))
        self.buttonKeyGenerate = QtWidgets.QPushButton(self.groupBoxCode)
        self.buttonKeyGenerate.setGeometry(QtCore.QRect(310, 130, 30, 30))
        self.buttonKeyGenerate.setText("Generate Key")
        self.buttonKeyGenerate.clicked.connect(self.generateKey)

        self.labelProgressCode = QtWidgets.QLabel(self.groupBoxCode)
        self.labelProgressCode.setGeometry(QtCore.QRect(20, 180, 120, 30))
        self.labelProgressCode.setText("Progress:")
        self.progressBarCode = QtWidgets.QProgressBar(self.groupBoxCode)
        self.progressBarCode.setGeometry(QtCore.QRect(150, 180, 190, 30))

        self.buttonEncode = QtWidgets.QPushButton(self.groupBoxCode)
        self.buttonEncode.setGeometry(QtCore.QRect(20, 230, 150, 30))
        self.buttonEncode.setText("Encode")
        self.buttonEncode.clicked.connect(self.encode)

        # Partie "Decode"
        self.groupBoxDecode = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxDecode.setGeometry(QtCore.QRect(380, 20, 350, 500))
        self.groupBoxDecode.setTitle("Decode")

        self.labelImageDecode = QtWidgets.QLabel(self.groupBoxDecode)
        self.labelImageDecode.setGeometry(QtCore.QRect(20, 30, 120, 30))
        self.labelImageDecode.setText("Image:")
        self.lineEditImageDecode = QtWidgets.QLineEdit(self.groupBoxDecode)
        self.lineEditImageDecode.setGeometry(QtCore.QRect(150, 30, 150, 30))
        self.buttonBrowseImageDecode = QtWidgets.QPushButton(self.groupBoxDecode)
        self.buttonBrowseImageDecode.setGeometry(QtCore.QRect(310, 30, 30, 30))
        self.buttonBrowseImageDecode.setText("...")
        self.buttonBrowseImageDecode.clicked.connect(self.browseImageDecode)

        self.labelKeyDecode = QtWidgets.QLabel(self.groupBoxDecode)
        self.labelKeyDecode.setGeometry(QtCore.QRect(20, 80, 120, 30))
        self.labelKeyDecode.setText("Key:")
        self.lineEditKeyDecode = QtWidgets.QLineEdit(self.groupBoxDecode)
        self.lineEditKeyDecode.setGeometry(QtCore.QRect(150, 80, 190, 30))

        self.labelProgressDecode = QtWidgets.QLabel(self.groupBoxDecode)
        self.labelProgressDecode.setGeometry(QtCore.QRect(20, 130, 120, 30))
        self.labelProgressDecode.setText("Progress:")
        self.progressBarDecode = QtWidgets.QProgressBar(self.groupBoxDecode)
        self.progressBarDecode.setGeometry(QtCore.QRect(150, 130, 190, 30))

        self.buttonDecode = QtWidgets.QPushButton(self.groupBoxDecode)
        self.buttonDecode.setGeometry(QtCore.QRect(20, 180, 150, 30))
        self.buttonDecode.setText("Decode")
        self.buttonDecode.clicked.connect(self.decode)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Steganography Software"))

    def browseImageCode(self):
        file_path, _ = QFileDialog.getOpenFileName(None, 'Open Image file', "", "Image Files (*.png *.jpg *.bmp)")
        if file_path != '':
            self.lineEditImageCode.setText(file_path)

    def browsePDFCode(self):
        file_path, _ = QFileDialog.getOpenFileName(None, 'Open PDF file', "", "PDF Files (*.pdf)")
        if file_path != '':
            self.lineEditPDFCode.setText(file_path)

    def generateKey(self):
        # Votre logique de génération de clé ici
        # Actuellement, cela ne fait rien
        pass

    def encode(self):
        # Votre logique de codage ici
        # Actuellement, cela ne fait rien
        pass

    def browseImageDecode(self):
        file_path, _ = QFileDialog.getOpenFileName(None, 'Open Image file', "", "Image Files (*.png *.jpg *.bmp)")
        if file_path != '':
            self.lineEditImageDecode.setText(file_path)

    def decode(self):
        # Votre logique de décodage ici
        # Actuellement, cela ne fait rien
        pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = pdf_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show
