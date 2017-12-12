#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math
import logging
from PyQt5 import QtWidgets, QtCore
from test_scene import vehicle_scene

LOG = logging.getLogger(__name__)


class TestScene(QtWidgets.QGraphicsView):
    def __init__(self, *args, **kwargs):
        super(TestScene, self).__init__(*args, **kwargs)
        self.setSceneRect(
            -500, -500, 1000.0, 1000.0)
        self.setScene(vehicle_scene.VehicleScene())
        self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self.setTransformationAnchor(
            QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(
            QtWidgets.QGraphicsView.AnchorViewCenter)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Left:
            pass
        elif event.key() == QtCore.Qt.Key_Right:
            pass
        elif event.key() == QtCore.Qt.Key_Up:
            pass
        elif event.key() == QtCore.Qt.Key_Down:
            pass
        elif event.key() == QtCore.Qt.Key_Space:
            pass


def main():
    import sys
    # parcser = stream_parser.StreamParser()
    app = QtWidgets.QApplication(sys.argv)
    w = TestScene()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
