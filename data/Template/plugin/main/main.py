from PySide6 import QtWidgets, QtGui, QtCore
import os

pluginName = "模板"

IMAGE = QtGui.QMovie
TIMER = QtCore.QTimer
STATE = dict
WINDOW = QtWidgets.QWidget

PATH = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")


class Template:
    def __init__(self):
        self.__autoStart__ = False

    def create(
        self,
        image: IMAGE,
        mainTimer: TIMER,
        physicsTimer: TIMER,
        state: STATE,
        window: WINDOW,
    ):
        """
        这是用来创建插件的模板
        发挥你的想象力！
        """
        self.image = image

    def loadMovie(self, path: str):
        # 加载动画
        if self.image.fileName() != path:
            self.image.setFileName(path)
            self.image.jumpToFrame(0)
        self.image.start()


import logging


class Test(Template):
    def __init__(self):
        super().__init__()

    def create(self, image, mainTimer, physicsTimer, state, window):
        super().create(image, mainTimer, physicsTimer, state, window)
        logging.info("Hello My DesktopPet!")
        QtWidgets.QMessageBox.information(window, "TEST", "Hello My DesktopPet!")


menu = {"模板": Test()}
