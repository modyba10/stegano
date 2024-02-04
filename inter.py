from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QMainWindow
from lsb_GUI import Ui_MainWindow
from pdf import pdf_MainWindow

class Choice(QMainWindow):
    def __init__(self):
        super(Choice, self).__init__()

        self.setWindowTitle("Steganography Tool")
        self.setGeometry(400, 400, 400, 400)

        # Utilisation de style CSS pour améliorer l'esthétique
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #333;
            }
            QPushButton {
                font-size: 14px;
                padding: 8px 16px;
                margin-top: 8px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        layout = QVBoxLayout()

        label = QLabel("Choose a Steganography method:")
        layout.addWidget(label)

        text_button = QPushButton("TEXT_DATA")
        pdf_button = QPushButton("PDF_DATA")

        layout.addWidget(text_button)
        layout.addWidget(pdf_button)

        pdf_button.clicked.connect(self.show_pdf_interface)
        text_button.clicked.connect(self.show_text_interface)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_pdf_interface(self):

        from pdf import pdf_MainWindow
        self.stego_interface = QtWidgets.QMainWindow()
        ui = pdf_MainWindow()
        ui.setupUi(self.stego_interface)
        self.stego_interface.show()
        self.close()
       
    

    def show_text_interface(self):
        from lsb_GUI import Ui_MainWindow
        self.stego_interface = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(self.stego_interface)
        self.stego_interface.show()
        self.close()
