import sys
import os

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout

from PyQt5.QtWidgets import QAction,qApp,QMainWindow


class Notepad(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()
    def init_ui(self):

        self.yazı_alani = QTextEdit()

        self.temizle = QPushButton("temizle")
        self.ac = QPushButton("ac")
        self.kaydet = QPushButton("kaydet")

        h_box = QHBoxLayout()

        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)

        v_box = QVBoxLayout()

        v_box.addWidget(self.yazı_alani)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.setWindowTitle("Notepad")

        self.temizle.clicked.connect(self.yaziyi_temizle)
        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosya_kaydet)





    def yaziyi_temizle(self):
        self.yazı_alani.clear()
    def dosya_ac(self):
        dosya_ismi = QFileDialog.getOpenFileName(self,"dosya aç",os.getenv("Desktop"))

        with open(dosya_ismi[0],"r") as file:
            self.yazı_alani.setText(file.read())

    def dosya_kaydet(self):
        dosya_ismi = QFileDialog.getSaveFileName(self,"dosya kaydet",os.getenv("Desktop"))

        with open(dosya_ismi[0],"w") as file:

            file.write(self.yazı_alani.toPlainText())

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.pencere = Notepad()

        self.setCentralWidget(self.pencere)

        self.menuleri_olustur()

    def menuleri_olustur(self):

        menubar = self.menuBar()

        dosya = menubar.addMenu("Dosya")


        dosya_ac = QAction("Dosya aç",self)
        dosya_ac.setShortcut("ctrl+O")

        dosya_kaydet = QAction("Dosya kaydet",self)
        dosya_kaydet.setShortcut("ctrl+S")

        temizle = QAction("dosyayı temizle",self)
        temizle.setShortcut("ctrl+D")

        cikis = QAction("çıkış",self)
        cikis.setShortcut("ctrl+Q")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(temizle)
        dosya.addAction(cikis)

        dosya.triggered.connect(self.response)





        self.setWindowTitle("Metin Editörü")
        self.show()

    def response(self,action):

        if action.text() == "dosya aç":
            self.pencere.dosya_ac()
        elif action.text() == "dosya kaydet":
            self.pencere.dosya_kaydet()
        elif action.text() == "dosyayı temizle":
            self.pencere.yaziyi_temizle()
        elif action.text() == "çıkış":
            qApp.quit()






app = QApplication(sys.argv)

menu = Menu()

sys.exit(app.exec_())