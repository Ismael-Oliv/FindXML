from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QProgressBar,
    QLabel,
    QFrame,
    QPushButton,
    QTextEdit
    )

import os
from src.xml.services.index import ReadXML
from src.xml.services.RemoveXML import RemoveXMLFromFolder


def XMLFeature(Screen):
    Lista = {'chv':''}
    def SaveButtonClicked(Barra_Progesso, TXTchv, TXTOrigem, TXTDestino):

        Barra_Progesso.setValue(0)
        chv = TXTchv.toPlainText()

        caminho = TXTOrigem.text()
        Destino = TXTDestino.text()

        params = {
                    'Barra_Progesso': Barra_Progesso,
                    'chv': chv,
                    'caminho': caminho,
                    'Destino': Destino
                  }
        result = ReadXML(params)
        Lista.update({'chv':result})
        LabelStatus.setText('Processo concluido')

    def RemoverXML(TXTDestino, TXTOrigem, Barra_Progesso):
        RemoveXMLFromFolder(TXTDestino, Lista, TXTOrigem)
        LabelStatus.setText('Arquivo Removido')
        Barra_Progesso.setValue(0)

    def SelectPath(TXTOrigem, TXTchv):
        LabelStatus.setText('Status:')
        directory = QtWidgets.QFileDialog.getExistingDirectory(
            None, 'Selecione a pasta com XML:', os.getcwd(), QtWidgets.QFileDialog.ShowDirsOnly)

        TXTchv.setText('')
        TXTOrigem.setText(directory)

    def SelectDestino(TXTDestino):
        LabelStatus.setText('Status:')
        directory = QtWidgets.QFileDialog.getExistingDirectory(
            None, 'Selecione a pasta destino:', os.getcwd(), QtWidgets.QFileDialog.ShowDirsOnly)

        TXTDestino.setText(directory)

    Screen.setGeometry(5, 20, 640, 320)
    Screen.setFixedSize(640, 320)

    Frame = Screen.frame = QFrame(Screen)
    Frame.setGeometry(15, 20, 560, 300)
    Frame.setFrameShape(QFrame.StyledPanel)

   # Label descrição da tela
    # =======================================================
    LabelDescricao = Screen.LabelDescricao = QLabel(Frame)
    LabelDescricao.setGeometry(200, 10, 400, 17)
    LabelDescricao.setText('Importar XML Entrada')
    # =======================================================
    
    LabelOrigem = Screen.labelOrigem = QLabel(Frame)
    LabelOrigem.setGeometry(50, 50, 67, 17)
    LabelOrigem.setText('Origem:')

    TXTOrigem = Screen.txtOrigem = QLabel(Frame)
    TXTOrigem.setGeometry(130, 50, 321, 17)
    TXTOrigem.setStyleSheet("""
            background-color: rgb(186, 189, 182);
    """)

    # =======================================================
    SelectPathButton = Screen.SelectPathButton = QPushButton(Frame)
    SelectPathButton.setGeometry(460, 45, 30, 30)
    SelectPathButton.setText('...')
    SelectPathButton.clicked.connect(lambda: SelectPath(TXTOrigem, TXTchv))
    # ==============================================================

    LabelDestino = Screen.LabelDestino = QLabel(Frame)
    LabelDestino.setGeometry(50, 90, 67, 17)
    LabelDestino.setText('Destino:')

    TXTDestino = Screen.TXTDestino = QLabel(Frame)
    TXTDestino.setGeometry(130, 90, 321, 17)
    TXTDestino.setStyleSheet("""
            background-color: rgb(186, 189, 182);
    """)

    # =======================================================
    SelecionarDestinoButton = Screen.SelecionarDestinoButton = QPushButton(Frame)
    SelecionarDestinoButton.setGeometry(460, 85, 30, 30)
    SelecionarDestinoButton.setText('...')
    SelecionarDestinoButton.clicked.connect(lambda: SelectDestino(TXTDestino))
    # ==============================================================

    # =======================================================
    Labelchv = Screen.Labelchv = QLabel(Frame)
    Labelchv.setGeometry(50, 125, 67, 17)
    Labelchv.setText('Num NF:')

    TXTchv = Screen.TXTchv = QTextEdit(Frame)
    TXTchv.setGeometry(130, 123, 150, 27)

    # ==================================================
    # Status Bar
    Barra_Progesso = Screen.Barra_Progesso = QProgressBar(Frame)
    Barra_Progesso.setGeometry(130, 170, 321, 25)

    # ==================================================

    PesquisarButton = Screen.PesquisarButton = QPushButton(Frame)
    PesquisarButton.setGeometry(140, 210, 101, 31)
    PesquisarButton.setText('Pesquisar')
    PesquisarButton.clicked.connect(
        lambda: SaveButtonClicked(Barra_Progesso, TXTchv, TXTOrigem, TXTDestino
                                  )
    )

    RemoverButton = Screen.RemoverButton = QPushButton(Frame)
    RemoverButton.setGeometry(300, 210, 101, 31)
    RemoverButton.setText('Remover XML')
    RemoverButton.clicked.connect(lambda: RemoverXML(TXTDestino, TXTOrigem, Barra_Progesso))

    LabelStatus = Screen.LabelStatus = QLabel(Frame)
    LabelStatus.setGeometry(160, 220, 180, 100)
    LabelStatus.setText('Status:')

    Screen.show()
