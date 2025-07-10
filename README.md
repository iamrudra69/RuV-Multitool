# 🚀 RuV-Multitool

**RuV-Multitool** is a powerful, modular, menu-driven terminal utility written in Python. It offers essential system tools, file management utilities, user authentication, and even prank features—all wrapped in a clean and engaging terminal UI.

---

## 🧠 Features at a Glance

### 🔐 Authentication
- **Register new users** with username/password
- **Secure login system**
- **Change password** functionality
- All data handled locally (ideal for demos and internal tools)

### 📁 File Management
- **Rename files** easily via the interface
- **Download files** from a specified path or location
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
![1](https://github.com/user-attachments/assets/ec2bc837-5a08-4530-9aeb-48722277b282)

### 🔓 Login Success
![2](https://github.com/user-attachments/assets/98028dd1-370b-47f0-91a8-d68b9b0eaaac)

### 🧩 Selection Menu (Main Tools)
![3](https://github.com/user-attachments/assets/4c7c4899-d0cd-4800-968b-ac7433cc8e97)

### 📁 File Operations Menu
![4](https://github.com/user-attachments/assets/28e05411-59d7-41f7-b49a-4a8d14c6fb59)

### 🤪 Pranks Menu (For Fun)
![5](https://github.com/user-attachments/assets/633e58f6-bc2b-4285-af97-955bbe028eba)

### 🖥️ System Information Menu
![6](https://github.com/user-attachments/assets/803402d4-e049-4633-a2e4-b8f163d741f7)


---

## 🛠️ How It Works

The core of **RuV-Multitool-v1** is modular. Each tool is stored in its own `.py` file and imported through a unified menu system (`SelectionMenu.py`). This makes it easy to maintain or expand.

### ✅ Program Flow
1. Launch `main.py`
2. Authenticate (register/login)
3. Access main menu
4. Navigate to File, System, or Pranks
5. Perform actions
6. Exit or return

---

## 📂 Project Structure

```bash
RuV-Multitool-v1/
├── Multitool/
│   ├── assets/              # Sound files for pranks
│   ├── AppBuildCommand.txt  # Build/run instructions
│   ├── Auth.py              # Login system
│   ├── Files.py             # File utilities
│   ├── Functions.py         # Shared functions
│   ├── Pranks.py            # Sound pranks
│   ├── SelectionMenu.py     # Menu system
│   ├── System.py            # System info
│   └── main.py              # Entry point
├── icon/                    # App icons (for .exe or GUI)
├── README.md                # This file
└── LICENSE                  # MIT License
```

---

## ⚙️ Installation Guide

### Requirements

- Python 3.8 or higher
- OS: Windows, Linux, macOS (Windows recommended for full prank support)

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

- GUI Version using **Tkinter** or **PyQt**
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

Developed by [@iamrudra69](https://github.com/iamrudra69) — contributions welcome!

> ASCII banners powered by **pyfiglet**  
> Colorful CLI interface using **termcolor**

---

If you enjoy using this project, ⭐️ the repo or share your ideas for improvements!
