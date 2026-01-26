# Desktop Pet

A cute, interactive, and plugin-enabled desktop pet built with Python + PySide6. It falls to the bottom of your screen, can be dragged, thrown, and moves with realistic physics!

## Features

- 🎮 **Physics Engine**: Simulates gravity, collision, and friction for natural motion
- 🖱️ **Interactive Controls**: Drag, throw, and pause the pet
- 🧩 **Plugin System**: Extend functionality via plugins (e.g., expressions, voice, mini-games)
- 🧪 **Debug Mode**: Toggle collision boxes for development
- 🛠️ **Borderless & Always-on-Top Window**: Stays above all apps without interfering
- 📦 **Configurable**: Customize behavior via `config.json` and `setting.json`

## 🚀 Quick Start

### Requirements

- Python 3.8+
- PySide6
- System support for GIF animation

### Install Dependencies

``` bash
pip install PySide6
```

### Required Directory Structure

Your project root should contain:

``` 
your-project/
├── main.py                 # Main program
├── setting.json            # Global settings (pet path, debug mode)
└── pets/my_cat/            # Example pet folder
    ├── config.json         # Pet configuration
    ├── icon.gif            # Application icon
    └── basic/
        ├── stand.gif       # Idle animation
        └── drop.gif        # Falling/moving animation
```

### Example `setting.json`

``` json
{
  "desktopPetPath": "pets/my_cat",
  "debug": false
}
```

### Example `config.json`

``` json
{
  "name": "Xiao Ju",
  "version": "1.0.0",
  "author": "Your Name",
  "imagePath": "pets/my_cat",
  "acc": [0.3, 0.5],
  "fri": [0.8, 0.8],
  "plugin": []
}
```

### Run the Program

``` bash
python main.py
```

The pet will appear at the bottom center of your screen in a transparent, full-screen window.

## 🎮 Usage

- **Left-click & drag**: Move the pet; release to throw it with momentum
- **Right-click**: Open context menu
  - Exit
  - About
  - Plugin actions (if any)
  - Toggle Collision Box (in debug mode)
- **Auto-start plugins**: Plugins with `__autoStart__ = True` load automatically

## 🔌 Plugin Development (Advanced)

Plugins must include a `main.py` that defines:
- `pluginName`: Plugin name
- `menu`: A dict like `{display_name: object}`

Each menu object must have:
- A `create(...)` method (receives `image`, `timers`, `state`, `window`, etc.)
- Optional: `__autoStart__ = True` for auto-loading

> Plugins can dynamically change animations, behaviors, or add new interactions.

## ⚠️ Disclaimer

This project is licensed under the **MIT License**.  
You are free to **modify, distribute, and use commercially**, provided you **retain the original author's name in the source code**.  
**Use at your own risk. The author is not liable for any direct or indirect damages.**

## 📄 License

See the full license in the [`LICENSE`](./LICENSE) file.

## 🙇‍ Special thanks
### Artist: 
- 残月
- 星源