import os
import sys
import gui_hapEncoder
from PyQt5 import QtWidgets, QtCore, QtGui

#from PySide6 import QtWidgets, QtGui

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    """
    CREATE A SYSTEM TRAY ICON CLASS AND ADD MENU
    """
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip(f'CUDO Server Manager - v1.00')

        menu = QtWidgets.QMenu(parent)
        app_Hapcodec = menu.addAction("HAP 코덱변환")
        app_Hapcodec.setToolTip(f'HAP코덱변환(H.264 -> HAP)')
        app_Hapcodec.triggered.connect(self.open_hapEncoder)
        app_Hapcodec.setIcon(QtGui.QIcon("icon.png"))

        exit_ = menu.addAction("Exit")
        exit_.triggered.connect(lambda: sys.exit())
        exit_.setIcon(QtGui.QIcon("icon.png"))

        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconActivated)

    def onTrayIconActivated(self, reason):
        """
        This function will trigger function on click or double click
        :param reason:
        :return:
        """
        if reason == self.DoubleClick:
            self.open_hapEncoder()
        # if reason == self.Trigger:
        #     self.open_notepad()

    # --------------------- Open HapEncoder window ---------------------- #
    def open_hapEncoder(self):
        self.hapencoder_window = gui_hapEncoder.mainGUI()
        self.hapencoder_window.show()

def main(image):
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon(image), w)
    tray_icon.show()
    tray_icon.showMessage('Cudo Communication', 'www.ailed.co.kr')
    sys.exit(app.exec())


if __name__ == '__main__':
    icon = "icon.png"
    main(icon)