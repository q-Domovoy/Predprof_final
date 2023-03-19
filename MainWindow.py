from PyQt5.QtWidgets import *
from PyQt5 import uic
import math


class MainWindow(QMainWindow):
    def __init__(self, lst):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.task = lst
        self.days1, self.days2, self.days3 = 0, 0, 0

        self.get_days()

        self.days_table.setItem(0, 0, QTableWidgetItem(str(math.ceil(self.days1))))
        self.days_table.setItem(0, 1, QTableWidgetItem(str(math.ceil(self.days2))))
        self.days_table.setItem(0, 2, QTableWidgetItem(str(math.ceil(self.days3))))

        self.mosh_table.setItem(0, 0, QTableWidgetItem(str(self.w1)))
        self.mosh_table.setItem(0, 1, QTableWidgetItem(str(self.e1)))

    def get_days(self):
        d1 = []
        for w in range(1, 81):
            d1.append(self.task[0][0][1] / (2 * w / 80 * 200 / (192 + self.task[0][0][0])))
        self.days1 = min(d1)
        self.w1 = d1.index(self.days1)
        self.e1 = 100 - self.w1
        self.days2 = 0
        self.days3 = 0
        for i in self.task[1]:
            self.days2 += i[1] / (400 / (192 + i[0]))
        for i in self.task[2]:
            self.days3 += i[1] / (400 / (192 + i[0]))


