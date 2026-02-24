# 桌面宠物（Desktop Pet）

## 开始

### 依赖要求

- Python 3.8+
- PySide6
- 支持 GIF 动画的系统

### 目录要求

你的项目根目录应包含以下文件:

```text
your-project/
├── main.py                       主程序
├── setting.json                  启动设置
└── data/                         存放所有桌宠的文件夹
    ├── [桌宠文件夹]/              例如:my_cat
    │   ├── config.json           桌宠配置(名称、版本、作者、插件等)
    │   ├── plugin/               可选,存放当前桌宠插件的目录 
    │   │   ├── [插件1文件夹]/     例如:AI-Cat
    │   │   │   ├── ...           其他资源
    │   │   │   └── main.py       入口程序
    │   │   └── ...               其他插件
    │   └─res/                    桌宠素材
    │     ├── icon.gif            桌宠图标
    │     └── basic/
    │         ├── drop.gif        下落动画
    │         └── stand.gif       待机动画
    └── ...                       其他桌宠
```

### 示例 setting.json:
```json
{
  "desktopPet": "my_cat",
  "debug": false
}
```

### 示例 config.json:
```json
{
  "name": "小橘",
  "version": "1.0.0",
  "author": "ABC",
  "acc": [0.3, 0.5],
  "fri": [0.8, 0.8],
  "plugin": [ "main" ]
}
```