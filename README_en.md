# Desktop Pet

## Getting Started

### Dependencies

- Python 3.8+
- PySide6
- System with GIF animation support

### Directory Structure

Your project root directory should contain the following files:

```text
your-project/
├── main.py                       Main program
├── setting.json                  Startup configuration
└── data/                         Folder for all desktop pets
    ├── [pet folder]/             Example: my_cat
    │   ├── config.json           Pet configuration (name, version, author, plugins, etc.)
    │   ├── plugin/               Optional, directory for pet-specific plugins
    │   │   ├── [plugin1 folder]/ Example: AI-Cat
    │   │   │   ├── ...           Other resources
    │   │   │   └── main.py       Entry program
    │   │   └── ...               Other plugins
    │   └─res/                    Pet resources
    │     ├── icon.gif            Pet icon
    │     └── basic/
    │         ├── drop.gif        Falling animation
    │         └── stand.gif       Idle animation
    └── ...
```

### Example setting.json:
```json
{
  "desktopPetPath": "my_cat",
  "debug": false
}
```

### Example config.json:
```json
{
  "name": "Xiaoju",
  "version": "1.0.0",
  "author": "ABC",
  "acc": [0.3, 0.5],
  "fri": [0.8, 0.8],
  "plugin": [ "main" ]
}
```