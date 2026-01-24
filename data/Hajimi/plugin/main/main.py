from PySide6 import QtWidgets, QtGui, QtCore
import time
import random
import rich

pluginName = "哈基米"

IMAGE = QtGui.QMovie
TIMER = QtCore.QTimer
STATE = list
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
        pass


class main(Template):
    def __init__(self):
        super().__init__()
        self.__autoStart__ = True
        self.timer = None
        self.lastTime = None
        self.eventTime = None
        self.state = 0
        """
        以下所有的比均按照 事件:..=值:.. 来定义
        0：待机 => 等待:移动:飞扑:休息=3:4:2:1
        1：等待 => 待机
        2：移动 => 等待
        3：飞扑 => 等待
        5：休息 => 等待
        """

    def create(self, image, mainTimer, physicsTimer, state, window):
        if self.timer is None:
            self.timer = QtCore.QTimer(window)
            self.timer.timeout.connect(lambda: self.timeout(image, state))
            self.timer.start(100)
            menu["关闭哈基米AI"] = menu.pop("启动哈基米AI")
            rich.print("[green]哈基米AI已启动![/]")
        else:
            self.timer.stop()
            self.timer = None
            self.lastTime = None
            self.eventTime = None
            self.state = 0
            state["pause"] = False
            menu["启动哈基米AI"] = menu.pop("关闭哈基米AI")
            rich.print("[red]哈基米AI已关闭![/]")

    def timeout(self, image: IMAGE, state: STATE):
        if self.lastTime is None:
            self.lastTime = time.time()
        if state["postion"][0] + 128 >= state["screenWidth"] - 32:
            self.state = 1
            self.eventTime = 5
            self.lastTime = time.time()
            state["motion"][0] -= 5
            print("哈基米被右侧一股无形的力量弹飞了")
        elif state["postion"][0] <= 32:
            self.state = 1
            self.eventTime = 5
            self.lastTime = time.time()
            state["motion"][0] += 5
            print("哈基米被左侧一股无形的力量弹飞了")
        if state["postion"][1] == state["screenHeight"] - 128:
            if self.state == 0:
                rich.print("[yellow]哈基米开始决策[/]")
                rand = random.random()
                if 0 < rand < 0.3:
                    print("哈基米开始等待")
                    self.eventTime = random.randint(15, 20)
                    self.state = 1
                elif 0.3 < rand < 0.7:
                    print("哈基米开始移动")
                    self.eventTime = random.randint(7, 10)
                    self.state = 2
                elif 0.7 < rand < 0.9:
                    rand = random.random()
                    print("哈基米开始飞扑")
                    self.eventTime = 0
                    self.state = 3
                elif 0.9 < rand < 1:
                    print("哈基米开始休息")
                    self.eventTime = random.randint(10, 30)
                    self.state = 4
            elif self.state == 1:
                state["pause"] = False
                if time.time() - self.lastTime >= self.eventTime:
                    print("哈基米等待完毕")
                    self.state = 0
                    self.lastTime = time.time()
            elif self.state == 2:
                state["pause"] = True
                image.setFileName("./data/Hajimi/plugin/main/move.gif")
                image.jumpToFrame(0)
                image.start()
                if self.eventTime % 2 == 0:
                    state["motion"][0] += 5
                else:
                    state["motion"][0] -= 5
                if time.time() - self.lastTime >= self.eventTime:
                    print("哈基米移动完毕")
                    self.state = 1
                    self.eventTime = 1
                    self.lastTime = time.time()
            elif self.state == 3:
                state["pause"] = True
                image.setFileName("./data/Hajimi/plugin/main/pounce.gif")
                image.jumpToFrame(0)
                image.start()
                if time.time() - self.lastTime >= self.eventTime:
                    state["motion"][0] += random.randint(-10, 10)
                    state["motion"][1] -= random.randint(5, 7)
                    print("哈基米飞扑完毕")
                    self.state = 1
                    self.eventTime = 3
                    self.lastTime = time.time()
            elif self.state == 4:
                state["pause"] = True
                image.setFileName("./data/Hajimi/plugin/main/rect.gif")
                image.jumpToFrame(0)
                image.start()
                if time.time() - self.lastTime >= self.eventTime:
                    print("哈基米休息完毕")
                    self.state = 1
                    self.eventTime = 5
                    self.lastTime = time.time()
            else:
                self.state = 0
                print(f"您的代码有点问题：\nstate:{self.state}")


entry = main()

menu = {"启动哈基米AI": entry}
