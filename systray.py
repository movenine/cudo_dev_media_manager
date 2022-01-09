import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PySide6 import QtWidgets, QtGui

import gui_hapEncoder

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
            self.open_notepad()
        # if reason == self.Trigger:
        #     self.open_notepad()

    # --------------------- Open HapEncoder window ---------------------- #
    def open_hapEncoder(self):
        try:
            self.hapencoder_window = gui_hapEncoder.mainGUI(self)
            self.hapencoder_window.show()
        except (OSError, TypeError) as e:
            QMessageBox.information(self, '오류', '유효하지 않는 요청입니다.')
            print(e)
            pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("icon.png"), w)
    tray_icon.show()
    tray_icon.showMessage('VFX Pipeline', 'Hello "Name of logged in ID')
    sys.exit(app.exec())


if __name__ == '__main__':
    main()