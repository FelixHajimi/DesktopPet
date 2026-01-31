from PySide6 import QtWidgets
from PySide6 import QtGui
from PySide6 import QtCore
import sys
import json
from importlib import util


# 创建菜单工具
def menuGenerate(master: QtWidgets.QWidget, structure: dict):
    menu = QtWidgets.QMenu(master)

    def func(mainMenu: QtWidgets.QMenu, structure: dict):
        for i in structure.keys():
            if i == "__type__":
                continue
            elif i == "__debug__":
                continue
            elif structure[i]["__type__"] == "command":
                command = QtGui.QAction(i, mainMenu)
                command.triggered.connect(structure[i]["__func__"])
                mainMenu.addAction(command)
            elif structure[i]["__type__"] == "sep":
                mainMenu.addSeparator()
            elif structure[i]["__type__"] == "menu":
                submenu = QtWidgets.QMenu(i, mainMenu)
                func(submenu, structure[i])
                mainMenu.addMenu(submenu)

    func(menu, structure)
    return menu


# 定义窗口
class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(data["name"])
        self.setWindowIcon(QtGui.QIcon(f"./data/{setting["desktopPet"]}/res/icon.gif"))
        self.setWindowFlags(
            QtCore.Qt.WindowType.WindowStaysOnTopHint
            | QtCore.Qt.WindowType.FramelessWindowHint
        )
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.nowMousePos = [0, 0]
        self.lastMousePos = [0, 0]

        self.position = [(screenWidth - 128) // 2, screenHeight - 128]
        self.motion = [0, 0]
        self.pause = False
        self.pressed = False

        self.showBox = False

        self.mainTimer = QtCore.QTimer(self)
        self.mainTimer.timeout.connect(self.mainStep)
        self.mainTimer.start(20)

        self.physicsTimer = QtCore.QTimer(self)
        self.physicsTimer.timeout.connect(self.physicsStep)
        self.physicsTimer.start(20)

        self.desktopPet = QtWidgets.QLabel(self)
        self.desktopPet.setCursor(QtCore.Qt.CursorShape.OpenHandCursor)
        self.desktopPet.mousePressEvent = self.MousePressEvent
        self.desktopPet.mouseMoveEvent = self.MouseMoveEvent
        self.desktopPet.mouseReleaseEvent = self.MouseReleaseEvent
        self.image = QtGui.QMovie()
        self.desktopPet.setMovie(self.image)
        self.desktopPet.resize(128, 128)

        self.state = {
            "pause": False,
            "position": self.position,
            "motion": self.motion,
            "screenWidth": screenWidth,
            "screenHeight": screenHeight,
            "update": [],
        }

        # 自启动判断
        _ = []
        for plugin in pluginList:
            for displayName, entry in plugin.menu.items():

                def itemFunc(f=entry):
                    def _():
                        getattr(f, "create")(
                            self.image,
                            self.mainTimer,
                            self.physicsTimer,
                            self.state,
                            self,
                        )

                    return _

                if getattr(entry, "__autoStart__"):
                    _.append(itemFunc())
        for i in _:
            i()

    def loadMovie(self, path: str):
        # 加载动画
        if self.image.fileName() != path:
            self.image.setFileName(path)
            self.image.jumpToFrame(0)
        self.image.start()

    def mainStep(self):
        # 主时钟循环
        self.pause = self.state["pause"]
        self.motion = self.state["motion"]
        self.position = self.state["position"]
        if not self.pause:
            if (
                abs(self.state["motion"][0]) <= data["acc"][0]
                and abs(self.state["motion"][1]) <= data["acc"][1]
            ):
                self.loadMovie(f"./data/{setting["desktopPet"]}/res/basic/stand.gif")
            else:
                self.loadMovie(f"./data/{setting["desktopPet"]}/res/basic/drop.gif")

        for i in self.state["update"]:
            i()

        self.desktopPet.move(self.state["position"][0], self.state["position"][1])

    def physicsStep(self):
        # 物理时钟循环

        # 重力模拟
        self.state["motion"][0] += data["acc"][0]
        self.state["motion"][1] += data["acc"][1]

        # 速度预处理
        if self.state["motion"][0] > screenWidth - (self.state["position"][0] + 128):
            self.state["motion"][0] = 0
            self.state["position"][0] = screenWidth - 128
        elif -self.state["motion"][0] > self.state["position"][0]:
            self.state["motion"][0] = 0
            self.state["position"][0] = 0
        elif self.state["motion"][1] > screenHeight - (self.state["position"][1] + 128):
            self.state["motion"][1] = 0
            self.state["position"][1] = screenHeight - 128
        elif -self.state["motion"][1] > self.state["position"][1]:
            self.state["motion"][1] = 0
            self.state["position"][1] = 0

        # 碰墙检测
        if self.state["position"][0] < 0:
            self.state["position"][0] = 0
            self.state["motion"][0] = 0
        elif self.state["position"][1] < 0:
            self.state["position"][1] = 0
            self.state["motion"][1] = 0
        elif self.state["position"][0] > screenWidth - 128:
            self.state["position"][0] = screenWidth - 128
            self.state["motion"][0] = 0
        elif self.state["position"][1] > screenHeight - 128:
            self.state["position"][1] = screenHeight - 128
            self.state["motion"][1] = 0

        # 摩擦力
        if (
            self.state["position"][0] == 0
            or self.state["position"][0] == screenWidth - 128
        ):
            if abs(self.state["motion"][1]) < data["fri"][1]:
                self.state["motion"][1] = 0
            else:
                self.state["motion"][1] += data["fri"][1] * (
                    (-1) ** (self.state["motion"][1] > 0)
                )
        elif (
            self.state["position"][1] == 0
            or self.state["position"][1] == screenHeight - 128
        ):
            if abs(self.state["motion"][0]) < data["fri"][0]:
                self.state["motion"][0] = 0
            else:
                self.state["motion"][0] += data["fri"][0] * (
                    (-1) ** (self.state["motion"][0] > 0)
                )

        # 设置位置
        self.state["position"][0] += self.state["motion"][0]
        self.state["position"][1] += self.state["motion"][1]

    def MouseMoveEvent(self, event: QtGui.QMouseEvent):
        if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            self.state["position"] = [
                event.globalPosition().x() - self.mouseOffset[0],
                event.globalPosition().y() - self.mouseOffset[1],
            ]
            self.nowMousePos = [
                event.globalPosition().x(),
                event.globalPosition().y(),
            ]
            self.state["motion"] = [
                self.nowMousePos[0] - self.lastMousePos[0],
                self.nowMousePos[1] - self.lastMousePos[1],
            ]
            self.lastMousePos = self.nowMousePos

    def MousePressEvent(self, event: QtGui.QMouseEvent):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.mouseOffset = [
                event.position().x(),
                event.position().y(),
            ]
            self.state["motion"] = [0, 0]
            self.desktopPet.setCursor(QtCore.Qt.CursorShape.ClosedHandCursor)
            self.physicsTimer.stop()
        elif event.button() == QtCore.Qt.MouseButton.RightButton:
            self.showMenu(event.globalPosition().toPoint())

    def MouseReleaseEvent(self, event: QtGui.QMouseEvent):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.desktopPet.setCursor(QtCore.Qt.CursorShape.OpenHandCursor)
            self.physicsTimer.start(20)

    def showMenu(self, globalPos):
        # 右键菜单
        def about():
            QtWidgets.QMessageBox.about(
                self,
                f"关于{data["name"]}",
                f"桌宠名字: {data["name"]}\n版本号: v{data["version"]}\n作者: {data["author"]}",
            )

        menuDict = {
            "退出": {"__type__": "command", "__func__": self.close},
            f"关于{data["name"]}": {"__type__": "command", "__func__": about},
        }

        # 导入插件
        for plugin in pluginList:

            menuDict[plugin.pluginName] = {"__type__": "menu"}
            for displayName, entry in plugin.menu.items():

                def itemFunc(f=entry):
                    def _():
                        getattr(f, "create")(
                            self.image,
                            self.mainTimer,
                            self.physicsTimer,
                            self.state,
                            self,
                        )

                    return _

                menuDict[plugin.pluginName][displayName] = {
                    "__type__": "command",
                    "__func__": itemFunc(),
                }

        if setting["debug"]:
            if self.showBox:
                menuDict["开/关碰撞箱"] = {
                    "__type__": "command",
                    "__func__": lambda: self.desktopPet.setStyleSheet(""),
                }
                self.showBox = False
            else:
                menuDict["开/关碰撞箱"] = {
                    "__type__": "command",
                    "__func__": lambda: self.desktopPet.setStyleSheet(
                        "border: 1px solid yellow;"
                    ),
                }
                self.showBox = True
        menu = menuGenerate(self, menuDict)
        menu.exec(globalPos)


# 导入数据
setting = json.load(open("./setting.json", encoding="utf-8"))
data = json.load(open(f"./data/{setting["desktopPet"]}/config.json", encoding="utf-8"))

pluginList = []
if "plugin" in data:
    for path in data["plugin"]:
        spec = util.spec_from_file_location("plugin", f"./data/{setting["desktopPet"]}/plugin/{path}/main.py")
        plugin = util.module_from_spec(spec)
        sys.modules["plugin"] = plugin
        spec.loader.exec_module(plugin)
        pluginList.append(plugin)

app = QtWidgets.QApplication(sys.argv)

screenWidth = app.primaryScreen().size().width()
screenHeight = app.primaryScreen().size().height()

window = Window()
window.showFullScreen()

sys.exit(app.exec())
