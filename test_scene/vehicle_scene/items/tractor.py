from PyQt5 import QtGui, QtWidgets, QtCore
import logging

LOG = logging.getLogger(__name__)


class Tractor(QtWidgets.QGraphicsItemGroup):
    body_length = 4.0
    body_width = 2

    pen = QtGui.QPen()
    pen.setWidth(1)
    pen.setCosmetic(True)

    def __init__(self, scene):
        super(Tractor, self).__init__()
        scene.add_to_update(self)

        # 1. front_body_
        self.body = QtWidgets.QGraphicsRectItem(
            QtCore.QRectF(
                - self.body_length / 2.0,
                -self.body_width / 2.0,
                self.body_length,
                self.body_width),
            self)

        self.body.setBrush(
            QtGui.QBrush(
                QtGui.QColor(QtCore.Qt.red)))
        self.body.setPen(self.pen)
