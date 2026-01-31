# Desktop Pet

> An interactive, plugin-supported desktop pet made with PySide6

## Features

- 🎮 **Physics Engine**: Simulates gravity, collisions, and friction, making behavior natural
- 🖱️ **Interaction Operations**: Click and drag, throw
- 🧩 **Plugin System**: Supports dynamic loading of plugins to extend functionality (such as expression switching, voice, mini-games, etc.)
- 🛠️ **Borderless Topmost Window**: Does not interfere with work and remains at the top of the desktop
- 📦 **Configuration Driven**: Configures appearance and behavior through `config.json` and `setting.json`

## 🚀 Quick Start

### Dependency Requirements

- Python 3.8+
- PySide6
- A system that supports GIF animations

### Install Dependencies

```bash
pip install PySide6
```

### Directory Requirements

Your project root directory should include the following files:

```text
your-project/
├── main.py                 Main program
├── setting.json            Startup settings (currently can modify debug mode, pet configuration path)
└── [Your pet folder]/        For example: my_cat
    ├── config.json         Pet configuration (name, author, icon, plugins, etc.)
    ├── icon.gif            Pet icon
    └── basic/
        ├── stand.gif       Standing animation
        └── drop.gif        Dropping animation
```

### Example setting.json:
```json
{
  "desktopPetPath": "my_cat",             // Pet directory name
  "debug": false                          // Debug mode
}
```

### Example config.json:
```json
{
  "name": "Xiao Ju",                      // Pet name
  "version": "1.0.0",                     // Pet version
  "author": "ABC",                        // Author
  "acc": [0.3, 0.5],                      // Gravity (x, y)
  "fri": [0.8, 0.8],                      // Friction (x, y, only on walls)
  "plugin": [                             // List of plugins to load
    "main"                                // Plugin directory name to load
  ]
}
```

### Running the Program

```bash
python main.py
```

The program will run as a full-screen transparent window, with the pet appearing at the bottom center of the screen.

## 🎮 Usage Instructions

- **Left-click and drag**: Move the pet, releasing it will throw it based on your throw speed
- **Right-click**: Open the menu
  - Exit
  - About
  - Plugin 1 (if available)
  - Plugin 2 (if available)
  - ...
  - Toggle collision box (available in debug mode)
- **Plugins Auto-Start**: If the plugin is marked `__autoStart__ = True`, it will be automatically loaded when the program starts

## ⚠️ Disclaimer

> This project is licensed under the **MIT License**.  
> **Feel free to modify, distribute, and use commercially**, but please retain the original author's information in the code.  
> **Use this software at your own risk; the author is not responsible for any direct or indirect losses.**

## 📄 License

This project uses the MIT License —— see the [`LICENSE`](./LICENSE) file for details.

## 🙇‍ Special Thanks

### Artists:
- Chan Yue
- Xing Yuan