from PyQt5 import QtCore, QtWidgets, QtGui
from test_scene.vehicle_scene.items import tractor


class VehicleScene(QtWidgets.QGraphicsScene):
    def __init__(self, *args, **kkargs):
        QtWidgets.QGraphicsScene.__init__(self, *args, **kkargs)
        self.update_list = []
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_scene)
        self.tractor = tractor.Tractor(self)

    def update_scene(self):
        for item in self.update_list:
            self.item.update()

    def add_to_update(self, item):
        self.addItem(item)
        self.update_list.append(item)
