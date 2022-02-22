import shutil
import os


def RemoveXMLFromFolder(destino, XMLs, TXTOrigem):
    Dest = ''
    Dest = destino.text()

    try:

        for XML in XMLs['chv']:
            caminho = Dest + '/' + XML
            os.remove(caminho)

    except Exception as Ex:

        print(Ex)
