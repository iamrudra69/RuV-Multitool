# 🚀 RuV-Multitool

**RuV-Multitool** is a powerful, modular, menu-driven terminal utility written in Python. It offers essential system tools, file management utilities, user authentication, and even prank features—all wrapped in a clean and engaging terminal UI.

---

## 🧠 Features at a Glance

### 🔐 Authentication
- **Register new users** with username/password
- **Secure login system**
- **Change password** functionality
- All data handled locally (ideal for demos and internal tools)

### 🕹️ Basic Operations Menu
- **Get Exhange Rate** exchange rate for currency in real time
- **Password Generator** creates a password upon the given limit
- **Timer** a interactive timer  
- Real Time data conversion through APIs

### 📁 File Management
- **Rename files** easily via the interface
- **Download files** from a specified path or location
- **Search files** from a folder with extensions
- Designed to be expandable (move, delete, zip etc. possible in future versions)

### 🖥️ System Utilities
- Get **Hostname and IP Address**
- Detect **CPU architecture**
- Check **Current Logged-in User**
- Extendable with more system functions (disk info, memory usage, etc.)

### 🎭 Prank Tools (For Fun)
- **Rotate Screen** (on compatible OS)
- **Play Random Sounds** from assets
- **Keyboard Glitch Prank**
- **CMD Window Overload** (for jokes only!)
> ⚠️ Use prank tools responsibly. They are for entertainment, not harm.

### 📋 Interactive Menus
- ASCII-styled UI with vibrant colors and icons
- Intuitive menus with back/exit shortcuts
- Designed for ease of navigation

---

## 🖼️ Screenshots

### 🔐 Authentication Menu
<img width="1069" height="571" alt="1" src="https://github.com/user-attachments/assets/30c6df36-ddc8-468f-aba3-537671405651" />

### 🔓 Login Success
<img width="1069" height="571" alt="2" src="https://github.com/user-attachments/assets/a504a41b-bc2e-4d2b-942c-884286a201c2" />

### 🧩 Selection Menu (Main Tools)
<img width="1069" height="571" alt="3" src="https://github.com/user-attachments/assets/9474b8af-4380-45d6-8493-1365355c1c55" />

### 🕹️ Basic Operations Menu
<img width="1115" height="628" alt="basic menu" src="https://github.com/user-attachments/assets/c6ab0419-4725-4cea-8587-5a53416f00cb" />

### 📁 File Operations Menu
<img width="1115" height="628" alt="4" src="https://github.com/user-attachments/assets/b0814e7f-7344-4266-8de0-7edc8dd3f722" />

### 🤪 Pranks Menu (For Fun)
<img width="1069" height="571" alt="5" src="https://github.com/user-attachments/assets/53cbe053-fe7f-434f-81a5-0fe73235d187" />

### 🖥️ System Information Menu
<img width="1069" height="571" alt="6" src="https://github.com/user-attachments/assets/d9ee9a6f-c723-45db-8f11-51043b38e21b" />

---

## 🛠️ How It Works

The core of **RuV-Multitool-v1** is modular. Each tool is stored in its own `.py` file and imported through a unified menu system (`SelectionMenu.py`). This makes it easy to maintain or expand.

### ✅ Program Flow
1. Launch `main.py`
2. Authenticate (register/login)
3. Access main menu
4. Navigate to Basic, File, System, or Pranks
5. Perform actions
6. Exit or return

---

## 📂 Project Structure

```bash
RuV-Multitool-v1/
├── Multitool/
│   ├── assets/              # Sound files for pranks
│   ├── AppBuildCommand.txt  # Build/run instructions
│   ├── auth.py              # Login system
│   ├── basicMenu.py         # Basic Operations like currency converter, password generator
│   ├── files.py             # File utilities
│   ├── functions.py         # Shared functions
│   ├── pranks.py            # Sound pranks
│   ├── selectionMenu.py     # Menu system
│   ├── system.py            # System info
│   └── main.py              # Entry point
├── icon/                    # App icons (for .exe or GUI)
├── README.md                # This file
└── LICENSE                  # MIT License
```

---

## ⚙️ Installation Guide

### Requirements

- Python 3.8 or higher
- OS: Windows (Windows 11 recommended for Best UI and Experience)

### Steps

1. Clone the repo:

```bash
git clone https://github.com/iamrudra69/RuV-Multitool-v1.git
cd RuV-Multitool-v1/Multitool
```

2. Install dependencies:

```bash
pip install playsound pyfiglet termcolor
```

3. Run the tool:

```bash
python main.py
```

---

## 🧪 Planned Features

- Logging system (debug + user logs)
- Password encryption & hash storage
- Add file zip/delete/move features
- GUI-based prank control
- `.exe` builder integration for 1-click run

---

## 📜 License

This project is licensed under the **MIT License**. You're free to use, modify, and distribute this software with proper credit.

📄 [View Full License](./LICENSE)

---

## 🙋‍♂️ Author & Credits

Developed by [@VoldRax](https://github.com/VoldRax) — contributions welcome!

---

If you enjoy using this project, ⭐️ the repo or share your ideas for improvements!
