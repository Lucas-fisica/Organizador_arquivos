import sys
from PyQt5.QtWidgets import QApplication, QFileDialog
import PyQt5.uic as ui
import PyQt5.QtGui as gt
import getpass as gt
import os
import shutil as sh
import platform as pt

distro = pt.release()
distro = distro[0:3]

app = QApplication([])
princ = ui.loadUi('jane1.ui')
secunda = ui.loadUi('jane2.ui')
ter = ui.loadUi('jan3.ui')

texto = ['.txt', '.docx', '.odt', '.xltx']
musica = ['.mp3', '.wav']
video = ['.mp4', '.3gp', '.mkv']
py = ['.ipynb', '.py']
pdf = '.pdf'
imagem = ['.jpeg', '.png', '.jpg', '.gif', ]
compact = ['.tar', '.zip', '.rar', '.xz', '.gz', '.deb']

class MAin():
    def Dialo(self):
        self.dialogo = QFileDialog()
        self.dir = (f'/home/{gt.getuser()}/Downloads')
        self.dialogo.setFileMode(self.dialogo.Directory)
        self.dialogo.setOption(self.dialogo.ShowDirsOnly)
        self.Can = self.dialogo.getExistingDirectory(directory=self.dir)
        if len(self.Can) <8:
            self.diretorio =self.dir
        else:
            self.diretorio = self.Can
        self.prime.bot2.setEnabled(True)
        print(self.diretorio)

    def Salve(self):
        self.lugar = QFileDialog()
        if distro=='4.1':
            self.dir = f'/home/{gt.getuser()}/Documents'
        else:
            self.dir = f'/home/{gt.getuser()}/Documentos'
        self.lugar.setFileMode(self.lugar.Directory)
        self.lugar.setOption(self.lugar.ShowDirsOnly)
        self.vai = self.lugar.getExistingDirectory(directory=self.dir)
        self.sejan.bot6.setEnabled(True)
        if len(self.vai)!=len(self.dir):
            self.camin = self.vai

        else:
            self.camin=self.dir
        print(self.camin)

    def pesquisa(self):
        self.lista = os.listdir(self.diretorio)
        self.exten = []
        os.chdir(self.diretorio)
        for i in self.lista:
            if os.path.isfile(i) == True:
                if not i.startswith('.'):
                    self.exten.append(i)
        return self.exten

    def separa(self):
        Outros = f'{self.camin}/Outros'
        Pdf= f'{self.camin}/Pdfs'
        Imagem = f'{self.camin}/Imagens'
        musica= f'{self.camin}/Musicas'
        texto = f'{self.camin}/Texto'
        Video = f'{self.camin}/Videos'
        Compactad = f'{self.camin}/Compactados'
        Jupyter = f'{self.camin}/Outros'

        os.chdir(self.diretorio)
        for tipo in self.pesquisa():
            indice = tipo.rfind('.')
            final = tipo[indice:]
            final = final.lower()
            if final in texto:
                if os.path.isdir(texto) == False:
                    os.mkdir(texto)
                if os.path.isfile(f'{texto}/{tipo}') == False:
                    sh.move(tipo, texto)
                elif os.path.isfile(f'{texto}/{tipo[:indice]}-1{final}') == False:
                    sh.move(tipo, f'{text}/{tipo[:indice]}-1{final}')
                elif os.path.isfile(f'{texto}/{tipo[:indice]}-2{final}') == False:
                    sh.move(tipo, f'{texto}/{tipo[:indice]}-2{final}')

            elif final in py:
                if os.path.isdir(Jupyter) == False:
                    os.mkdir(Jupyter)
                if os.path.isfile(f'{Jupyter}/{tipo}') == False:
                    sh.move(tipo, Jupyter)
                elif os.path.isfile(f'{Jupyter}/{tipo[:indice]}-1{final}') == False:
                    sh.move(tipo, f'{Jupyter}/{tipo[:indice]}-1{final}')
                elif os.path.isfile(f'{Jupyter}/{tipo[:indice]}-2{final}') == False:
                    sh.move(tipo, f'{Jupyter}/{tipo[:indice]}-2{final}')

            elif final in pdf:
                if os.path.isdir(Pdf) == False:
                    os.mkdir(Pdf)
                if os.path.isfile(f'{Pdf}/{tipo}') == False:
                    sh.move(tipo, Pdf)
                elif os.path.isfile(f'{Pdf}/{tipo[:indice]}-1{final}') == False:
                    sh.move(tipo, f'{Pdf}/{tipo[:indice]}-1{final}')
                elif os.path.isfile(f'{Pdf}/{tipo[:indice]}-2{final}') == False:
                    sh.move(tipo, f'{Pdf}/{tipo[:indice]}-2{final}')

            elif final in video:
                if os.path.isdir(Video) == False:
                    os.mkdir(Video)
                if os.path.isfile(f'{Video}/{tipo}') == False:
                    sh.move(tipo, Video)
                elif os.path.isfile(f'{Video}/{tipo[:indice]}-1{final}') == False:
                    sh.move(tipo, f'{Video}/{tipo[:indice]}-1{final}')
                elif os.path.isfile(f'{Video}/{tipo[:indice]}-2{final}') == False:
                    sh.move(tipo, f'{Video}/{tipo[:indice]}-2{final}')

            elif final in musica:
                if os.path.isdir(Musica) == False:
                    os.mkdir(Musica)
                if os.path.isfile(f'{Musica}/{tipo}') == False:
                    sh.move(tipo, Musica)
                elif os.path.isfile(f'{Musica}/{tipo[:indice]}-1{final}') == False:
                    sh.move(tipo, f'{Musica}/{tipo[:indice]}-1{final}')
                elif os.path.isfile(f'{Musica}/{tipo[:indice]}-2{final}') == False:
                    sh.move(tipo, f'{Musica}/{tipo[:indice]}-2{final}')

            elif final in imagem:
                if os.path.isdir(Imagem) == False:
                    os.mkdir(Imagem)
                if os.path.isfile(f'{Imagem}/{tipo}') == False:
                    sh.move(tipo, Imagem)
                elif os.path.isfile(f'{Imagem}/{tipo[:indice]}-1{final}') == False:
                    sh.move(tipo, f'{Imagem}/{tipo[:indice]}-1{final}')
                elif os.path.isfile(f'{Imagem}/{tipo[:indice]}-2{final}') == False:
                    sh.move(tipo, f'{Imagem}/{tipo[:indice]}-2{final}')

            elif final in compact:
                if os.path.isdir(Compactad) == False:
                    os.mkdir(Compactad)
                if os.path.isfile(f'{Compactad}/{tipo}') == False:
                    sh.move(tipo, Compactad)
                elif os.path.isfile(f'{Compactad}/{tipo[:indice]}-1{final}') == False:
                    sh.move(tipo, f'{Compactad}/{tipo[:indice]}-1{final}')
                elif os.path.isfile(f'{Compactad}/{tipo[:indice]}-2{final}') == False:
                    sh.move(tipo, f'{Compactad}/{tipo[:indice]}-2{final}')

            else:
                if os.path.isdir(Outros) == False:
                    os.mkdir(Outros)
                if os.path.isfile(f'{Outros}/{tipo}') == False:
                    sh.move(tipo, Outros)
                elif os.path.isfile(f'{Outros}/{tipo[:indice]}-1{final}') == False:
                    sh.move(tipo, f'{Outros}/{tipo[:indice]}-1{final}')
                elif os.path.isfile(f'{Outros}/{tipo[:indice]}-2{final}') == False:
                    sh.move(tipo, f'{Outros}/{tipo[:indice]}-2{final}')


    def ja2(self):
        self.sejan = secunda
        self.sejan.bot3.clicked.connect(lambda : self.Salve())
        self.sejan.bot4.clicked.connect(lambda : self.sejan.close())
        self.sejan.bot6.clicked.connect(lambda : self.Chama())
        self.sejan.move(477, 230)
        self.sejan.show()

    def ja1(self):
        self.prime=princ
        self.prime.bot1.clicked.connect(lambda : self.Dialo())
        self.prime.bot2.clicked.connect(lambda: self.ja2())
        self.prime.bot1a.clicked.connect(lambda : self.prime.close())
        self.prime.move(450, 170)
        self.prime.show()

    def ja3(self):
        self.ter = ter
        self.ter.bot7.clicked.connect(lambda : self.Sair())
        self.ter.move(600, 300)
        self.ter.show()

    def Chama(self):
        self.separa()
        self.ja3()

    def Sair(self):
        self.sejan.close()
        self.ter.close()

Janela = MAin()
Janela.ja1()
app.exec_()