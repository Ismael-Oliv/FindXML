from PyQt5 import QtCore, QtGui, QtWidgets

from src.xml.index import XMLFeature


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        # ============================================================================
        # Header

        MainWindow.setObjectName("")
        MainWindow.setMinimumSize(603, 534)
        MainWindow.setMaximumSize(603, 534)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        XMLFeature(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Procurar XML"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
