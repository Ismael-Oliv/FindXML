import os


path_tobe_removed = 'C:/Users/Ismae/Desktop/Importação Andorinha/XML em Importação'

xml_not_imported = os.listdir('C:/Users/Ismae/Desktop/Importação Andorinha/XML cm problemas - Andorinha')
xml_be_imported = os.listdir(path_tobe_removed)

for xml in xml_not_imported:
    if xml in xml_be_imported:
        os.remove(path_tobe_removed + "/" + xml)