from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QMainWindow
from inter import Choice  

class MainPage(QMainWindow):
    def __init__(self):
        super(MainPage, self).__init__()

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

        lsb_button = QPushButton("LSB Steganography")
        fft_button = QPushButton("DCT Steganography")

        layout.addWidget(lsb_button)
        layout.addWidget(fft_button)

        lsb_button.clicked.connect(self.show_lsb_interface)
        fft_button.clicked.connect(self.show_fft_interface)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_lsb_interface(self):
        self.stego_interface = Choice()  # Update class instantiation
        self.stego_interface.show()
        self.close()

    def show_fft_interface(self):
        from dct_GUI import Ui_MainWindow
        self.stego_interface = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(self.stego_interface)
        self.stego_interface.show()
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_page = MainPage()
    main_page.show()
    sys.exit(app.exec_())
