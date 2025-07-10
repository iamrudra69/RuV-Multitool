# 🔧 RuV-Multitool-v1

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-green)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> ⚙️ A modular, menu-driven Python utility that combines system tools, file operations, user authentication, and fun prank features — all in one place!

---

## 📚 Table of Contents

- [🧠 Features](#-features)
- [📂 Project Structure](#-project-structure)
- [⚙️ Installation & Usage](#️-installation--usage)
- [▶️ How to Run](#️-how-to-run)
- [🎬 Preview](#-preview)
- [🛠 Customization](#-customization)
- [💡 Future Improvements](#-future-improvements)
- [🙋‍♂️ Author](#-author)
- [📄 License](#-license)

---

## 🧠 Features

### ✅ General
- Modular, menu-based interface
- Intuitive terminal interaction
- Easily extensible with new modules

### 🔐 Authentication (`Auth.py`)
- Username/password login system
- Ideal for demos, local tools, or parental control

### 📁 File Management (`Files.py`)
- Create, read, and delete files
- Secure file handling with user prompts

### 🖥️ System Tools (`System.py`)
- View OS, CPU, and platform info
- Extendable to add network or memory tools

### 🎉 Pranks (`Pranks.py`)
- Play sound effects (`.mp3`/`.wav`)
- Perfect for harmless jokes with friends

### 🧩 Menu System (`SelectionMenu.py`)
- Centralized script navigation
- Smooth user flow with categorized options

---

## 📂 Project Structure

<details>
<summary>📁 <strong>Click to Expand: Project Directory Tree</strong></summary>

```text
RuV-Multitool-v1/
│
├── Multitool/
│   ├── assets/               # Sound files for pranks
│   ├── AppBuildCommand.txt   # Build/run instructions
│   ├── Auth.py               # Login system
│   ├── Files.py              # File utilities
│   ├── Functions.py          # Shared helper functions
│   ├── Pranks.py             # Sound pranks
│   ├── SelectionMenu.py      # Menu system
│   ├── System.py             # System info
│   └── main.py               # Entry point
│
├── icon/                     # App icons (for .exe or GUI)
├── README.md                 # Project documentation
└── LICENSE                   # MIT License
```

</details>

---

## ⚙️ Installation & Usage

### 🔽 Prerequisites

- **Python 3.8+**  
- **pip** installed
- For pranks:
  ```bash
  pip install playsound  # Or pygame if you use that
  ```

---

## ▶️ How to Run

```bash
# 1. Clone the repository
git clone https://github.com/iamrudra69/RuV-Multitool-v1.git

# 2. Navigate into the project
cd RuV-Multitool-v1/Multitool

# 3. Run the main program
python main.py
```

> 💡 Make sure your Python environment supports sound playback (on Windows, macOS, or Linux).

---

## 🎬 Preview

> **Here’s a sneak peek of the terminal interface:**

```
=======================
   RuV-Multitool-v1
=======================
1. File Management
2. System Tools
3. Pranks
Choose an option:
```

![Preview GIF or Screenshot](icon/demo.gif) <!-- Replace with actual screenshot path -->

---

## 🛠 Customization

### 🧩 Adding New Tools
- Create a new Python file in `Multitool/` (e.g. `MyTool.py`)
- Import it in `SelectionMenu.py`
- Add a new option in the menu and link your function

### 🎵 Changing Prank Sounds
- Replace files in the `assets/` folder with your custom `.wav` or `.mp3`
- Update filenames in `Pranks.py` if necessary

### 🖼 GUI Version (Coming Soon!)
- Planned support for tkinter and PyQt
- Icons in `icon/` can be used for GUI buttons or packaging

---

## 💡 Future Improvements

✅ Planned Features:

- [ ] GUI interface using **tkinter** or **PyQt**
- [ ] Add **network tools** (ping, IP lookup, etc.)
- [ ] Improve **password encryption**
- [ ] Add **logging and debugging** tools
- [ ] Package into `.exe` and `.apk` via `AppBuildCommand.txt`

---

## 🙋‍♂️ Author

Built with 💻 and 🎧 by [**iamrudra69**](https://github.com/iamrudra69)  
If you like this project, ⭐️ star it, fork it, or share it!

---

## 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute it with attribution.

See [LICENSE](LICENSE) for details.

---

**🚀 Enjoy using RuV-Multitool-v1!**  
Got ideas? Contributions and feedback are always welcome.
