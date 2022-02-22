import xmltodict
import os
import shutil


def ReadXML(Params):

    TipoNF = ['enviNFe', 'nfeProc']

    Findchv = Params['chv']
    pathSrc = Params['caminho']
    Destino = Params['Destino']
    Barra_Progesso = Params['Barra_Progesso']

    arrXML = os.listdir(pathSrc)
    XMLTotal = len(arrXML)
    lista = []

    for index, xml in enumerate(arrXML):

        with open(os.path.join(pathSrc, xml), mode='r', encoding='utf-8') as fd:
            doc = xmltodict.parse(fd.read())

            for tipo in doc:
                if tipo in TipoNF:
                    tag = tipo
            try:

                if doc[tag]:

                    nNF = doc[tag]['NFe']['infNFe']['ide']['nNF']

                    # chv = doc[tag]['NFe']['infNFe']['@Id']
                    # emit = doc[tag]['NFe']['infNFe']['emit']
                    # dest = doc[tag]['NFe']['infNFe']['dest']

                    if nNF == Findchv:
                        print(xml)
                        shutil.copy(file=os.path.join(pathSrc, xml), dst=os.path.join(Destino, xml))
                        lista.append(xml)

            except Exception as Ex:
                print(Ex)

        Barra_Progesso.setValue((index / XMLTotal) * 100)

    return lista