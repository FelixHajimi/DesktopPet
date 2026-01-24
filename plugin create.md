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
        "./data/Hajimi/plugin/插件1/",
        ...
        ],
    ...
}
```
**注意：后面不要加文件名**

## 示例右键效果

```
┌───────────────┐
│ 退出          │
│ 关于          │
│ 插件1      ▶ ├───────────────┐
│ 显示碰撞箱     │ 功能1         │
└───────────────┥ 功能2         │
                │ ...           │
                └───────────────┘

```
