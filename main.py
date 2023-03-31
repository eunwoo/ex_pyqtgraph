import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, \
    QHBoxLayout, QVBoxLayout, QListWidget, QComboBox, QLabel, QGroupBox, QMainWindow, \
    QLineEdit, QLCDNumber, QFrame, QTabWidget, QCheckBox, QFileDialog, QDialog
from PySide6 import QtCore
from PySide6 import QtGui
from PySide6.QtGui import QFont, QIcon, QPixmap, QScreen, QClipboard, QImage
from PySide6.QtCore import Slot, Signal, QObject, QRunnable, QThreadPool, QSize, QPropertyAnimation, Property, QTimer, QEvent, QMimeData
# from main_window import Ui_MainWindow
import pyqtgraph as pg
import pandas as pd
import numpy as np
import math

# https://www.pythonguis.com/tutorials/plotting-pyqtgraph/


uiclass, baseclass = pg.Qt.loadUiType("main_window.ui")

# class Main(QMainWindow, Ui_MainWindow):
class Main(uiclass, baseclass):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.widget.setBackground('w')

        data = pd.read_csv('0001.CSV', names=['blank', 'U1', 'I1', 'U2', 'I2', 'U3', 'I3', 'blank1'], skiprows=99)
        print(data['U1'])
        print(len(data['U1']))
        print(np.linspace(0, 50e-3, 1602))

        Vu = (data['U1'] + data['U3'])/3
        Vv = (data['U1'] - 2*data['U3'])/3
        Vw = -(2*data['U1'] - data['U3'])/3
        t = np.linspace(0, 50e-3, 1602)
        Vmag = 261
        Vu_approx = Vmag*np.cos(2*math.pi*87.5*t - math.pi*0.53)
        Iu_approx = 22*np.cos(2*math.pi*87.5*t - math.pi*0.53)
        Vv_approx = Vmag*np.cos(2*math.pi*87.5*t - math.pi*0.53 - 2/3*math.pi)
        Iv_approx = 22*np.cos(2*math.pi*87.5*t - math.pi*0.53 - 2/3*math.pi)
        Vw_approx = Vmag*np.cos(2*math.pi*87.5*t - math.pi*0.53 - 4/3*math.pi)
        Iw_approx = 22*np.cos(2*math.pi*87.5*t - math.pi*0.53 - 4/3*math.pi)

        # pen = pg.mkPen(color=(255, 0, 0), width=15)
        # self.widget.plot(np.linspace(0, 50e-3, 1602)[0:365], Vu_approx[0:365], pen=pen)
        # pen = pg.mkPen(color=(255, 0, 0))
        # self.widget.plot(np.linspace(0, 50e-3, 1602)[0:365], Vu.iloc[0:365], pen=pen)

        # pen = pg.mkPen(color=(255, 0, 0))
        # self.widget.plot(np.linspace(0, 50e-3, 1602), data['I1'], pen=pen)
        # pen = pg.mkPen(color=(0, 255, 0), width=10)
        # self.widget.plot(np.linspace(0, 50e-3, 1602), Iu_approx, pen=pen)

        # power
        pen = pg.mkPen(color=(255, 0, 0))
        # self.widget.plot(np.linspace(0, 50e-3, 1602), Vu_approx*Iu_approx, pen=pen)
        self.widget.plot(np.linspace(0, 50e-3, 1602), Vu_approx*Iu_approx + Vv_approx*Iv_approx + Vw_approx*Iw_approx, pen=pen)

        # self.widget.plot(np.linspace(0, 50e-3, 1602), data['I1'], pen=pen)
        # self.widget.plot(np.linspace(0, 50e-3, 1602), (data['U1'] + data['U3'])/3*data['I1'], pen=pen)
        # pen = pg.mkPen(color=(255, 255, 0))
        # self.widget.plot(np.linspace(0, 50e-3, 1602), (data['U1'] - 2*data['U3'])/3, pen=pen)
        # pen = pg.mkPen(color=(0, 0, 255))
        # self.widget.plot(np.linspace(0, 50e-3, 1602), -(2*data['U1'] - data['U3'])/3, pen=pen)

        # self.widget.plot(np.linspace(0, 50e-3, 1602), Vu*data['I1'] + Vv*data['I2'] + Vw*data['I3'], pen=pen)


def main():
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    app.exec()

if __name__ == '__main__':
    main()
    exit()
