import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from password import Ui_MainWindow
import sqlite3
import random
import string


baglanti = sqlite3.connect("sifrelerim.db")
cursor = baglanti.cursor()
sorgu = "CREATE TABLE IF NOT EXISTS sifreler(hesap1 TEXT, email1 TEXT,sifre1 TEXT)"
cursor.execute(sorgu)
baglanti.commit()

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.olustur.clicked.connect(self.olustur)
        self.ui.yazdir.clicked.connect(self.yazdir)

    def olustur(self):
        karakterler = string.ascii_letters+string.digits+string.punctuation
        uzunluk = int(self.ui.uzunluk.text())
        sifre = ''.join(random.choice(karakterler) for i in range(uzunluk))
        self.ui.sifre_2.setText(sifre)
        hesap = self.ui.hesap.text()
        email = self.ui.email.text()

        sorgu = "INSERT INTO sifreler VALUES(?,?,?)"
        cursor.execute(sorgu,(hesap,email,sifre))
        baglanti.commit()

    def yazdir(self):
        self.ui.listWidget.clear()
        sorgu = "select * from sifreler"
        cursor.execute(sorgu)
        liste = cursor.fetchall()
        for i in liste:
            self.ui.listWidget.addItems(["***HESAP BİLGİLERİ***"])
            self.ui.listWidget.addItems(i)

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())