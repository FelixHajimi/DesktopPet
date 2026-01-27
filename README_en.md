# Desktop Pet

A cute, interactive, and plugin-enabled desktop pet built with Python + PySide6.

## Features

🎮 **Physics Engine**: Simulates gravity, collision, and friction for natural motion  
🖱️ **Interactive Controls**: Drag, throw, and pause the pet  
🧩 **Plugin System**: Extend functionality via plugins (e.g., expression switching, voice, mini-games)  
🧪 **Debug Mode**: Toggle collision boxes for development  
🛠️ **Borderless & Always-on-Top Window**: Stays above all apps without interfering  
📦 **Configurable**: Customize appearance and behavior via `config.json` and `setting.json`

## 🚀 Quick Start

### Requirements

- Python 3.8+
- PySide6
- System support for animated GIFs

### Install Dependencies

```sh
pip install PySide6
```

### Required Directory Structure

Your project root should contain:

```txt
your-project/
├── main.py                 # Main program
├── setting.json            # Startup settings (debug mode, pet config path)
└── [your_pet_folder]/      # e.g., my_cat
    ├── config.json         # Pet configuration (name, author, icon, plugins, etc.)
    ├── icon.gif            # Pet icon
    └── basic/
        ├── stand.gif       # Idle animation
        └── drop.gif        # Falling animation
```

### Example `setting.json`:

```json
{
  "desktopPetPath": "data/my_cat",
  "debug": false
}
```

### Example `config.json`:

```json
{
  "name": "小橘",
  "version": "1.0.0",
  "author": "ABC",
  "imagePath": "data/my_cat/res/",
  "acc": [0.3, 0.5],
  "fri": [0.8, 0.8],
  "plugin": ["data/my_cats/plugin/main"]
}
```

### Run the Program

```sh
python main.py
```

The program runs in a full-screen transparent window, and the pet appears at the bottom center of the screen.

## 🎮 Usage

- **Left-click & drag**: Move the pet; release to throw it with momentum
- **Right-click**: Open context menu
  - Exit
  - About
  - Plugin 1 (if loaded)
  - Plugin 2 (if loaded)
  - ...
  - Toggle Collision Box (only visible in debug mode)

## Auto-start Plugins

Plugins marked with `__autoStart__ = True` will be loaded automatically on startup.

## 🔌 Plugin Development (Advanced)

A plugin must include a `main.py` file that defines:

- `pluginName`: Plugin name
- `menu`: Menu item dictionary in the format `{display_name: object}`

Each menu item object must have:

- A `create(...)` method that receives parameters such as `image`, `timers`, `state`, and `window`
- (Optional) `__autoStart__ = True` to enable auto-loading on startup

Plugins can dynamically change the pet’s animation, behavior logic, or add new interactions.

## ⚠️ Disclaimer

This project is licensed under the MIT License.  
You are free to modify, distribute, and use it commercially, provided you retain the original author information in the source code.  
Use at your own risk. The author is not liable for any direct or indirect damages.

## 📄 License

This project uses the MIT License — see the [LICENSE](./LICENSE) file for details.

## 🙇 Special Thanks

Artist:

- 残月
- 星源
