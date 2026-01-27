from PySide6 import QtWidgets, QtGui, QtCore
import time
import random
import rich

pluginName = "模板"

IMAGE = QtGui.QMovie
TIMER = QtCore.QTimer
STATE = dict
WINDOW = QtWidgets.QWidget


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

class Test(Template):
    def create(self, image, mainTimer, physicsTimer, state, window):
        print("Hello My DesktopPet!")
    
menu = {
    "模板": Test
}
