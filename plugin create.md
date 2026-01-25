# 如何制作一款插件？

## 准备

- ### 目录：

```text
your-project/
└── [你的宠物文件夹]/
    ├── config.json
    └── plugin/
        └── [你想制作的插件的文件夹]/
            ├── main.py
            ├── [资源1]
            ├── [资源2]
            └── ...
```

**主要的逻辑都在main.py里面写**

- ### 模板：

```py
from PySide6 import QtWidgets, QtGui, QtCore

pluginName = "插件在右键菜单的显示名称"

IMAGE = QtGui.QMovie
TIMER = QtCore.QTimer
STATE = dict
"""
self.state = {
    "pause": False,                 # 是否暂停动画(仅限于stand.gif,drop.gif)
    "postion": self.postion,        # 桌宠位置
    "motion": self.motion,          # 桌宠动量
    "screenWidth": screenWidth,     # 屏幕宽度
    "screenHeight": screenHeight,   # 屏幕高度
}
"""
WINDOW = QtWidgets.QWidget


class Template:
    def __init__(self):
        self.__autoStart__ = False

    def create(
        self,
        image: IMAGE,
        mainTimer: TIMER,           # 这个如果暂停会暂停位置更新
        physicsTimer: TIMER,        # 物理更新
        state: STATE,
        window: WINDOW,             # 这个是主窗口，可以把一些自己的想法放到上面
    ):
        """
        这是用来创建插件的模板
        发挥你的想象力！
        """
        pass
```

> 其中的 \_\_autoStart\_\_ 是判断桌宠启动时的自启动选项，默认为False(关闭)

制作时只需要再定义一个类，让他继承模板就行了

## 菜单

在最后要有一个菜单才能被程序识别：

```py
menu = {
    "功能1": entry, #你制作的类
    "功能2": entry,
    ...
}
```

## 导入

在你的桌宠的 config.json 文件里，plugin 键里的列表新增一个值用来保存 main.py 的路径

**例如:**

```json
{
    ...
    "plugin": [
        "./data/Template/plugin/插件1/",
        ...
        ],
    ...
}
```

**注意：后面不要加文件名**

## 示例右键效果

![这是右键效果](https://github.com/FelixHajimi/DesktopPet/blob/main/images/context_menu.png)
