# RuV Tools v1 - Basic Console Multitool with Authentication

![Logo](https://raw.githubusercontent.com/iamrudra69/RuV-Tools/main/assets/logo.png)
![Screenshot](https://raw.githubusercontent.com/iamrudra69/RuV-Tools/main/assets/screenshot.png)

RuV Tools is a simple console-based multitool application for Windows and Unix-like systems. It features user authentication (register, login, change password) using MongoDB for credential storage, and provides basic system information utilities.

## Features

- **User Authentication:** Register, login, and change password with credentials securely stored in MongoDB.
- **System Information:** Display hostname, IP address, CPU architecture, and current user.
- **Colored ASCII Logo:** Stylish colored logo and user interface.
- **Cross-Platform:** Designed for Windows, with partial support for Unix-like systems.

## Requirements

- Python 3.8+
- [MongoDB](https://www.mongodb.com/) running locally (`mongodb://localhost:27017/`)
- Python packages: `pymongo`

## Usage

1. **Install dependencies:**
    ```
    pip install pymongo
    ```

2. **Start MongoDB locally.**

3. **Run the script:**
    ```
    python main.py
    ```

4. **Follow the on-screen menu to register, login, or use the system utilities.**

## Notes

- Passwords are hashed using SHA-256 before storing in MongoDB.
- The application uses `msvcrt` and `ctypes` for Windows-specific features.
- For best experience, run on Windows. Some features may not work on all Unix terminals.

## Disclaimer

This is a basic demonstration project for educational purposes. Do not use for storing sensitive data in production environments.
