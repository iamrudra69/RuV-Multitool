# RuV Tools v1 - Basic Console Multitool with Authentication
![asset1](https://github.com/user-attachments/assets/bf69fa65-3025-4e3d-9190-7c26fd407909)

RuV Tools is a simple console-based multitool application for Windows and Unix-like systems. It features user authentication (register, login, change password) using MongoDB for credential storage, and provides basic system information utilities.
___
## Features

- **User Authentication:** Register, login, and change password with credentials securely stored in MongoDB.
- **System Information:** Display hostname, IP address, CPU architecture, and current user.
- **Colored ASCII Logo:** Stylish colored logo and user interface.
- **Cross-Platform:** Designed for Windows, with partial support for Unix-like systems.

  
![asset2](https://github.com/user-attachments/assets/5fc90ad3-3632-4f06-8910-1a01e8938362)
___
## Requirements

- Python 3.8+
- [MongoDB](https://www.mongodb.com/) running locally (`mongodb://localhost:27017/`)
- Python packages: `pymongo`
___
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
___
## Notes

- Passwords are hashed using SHA-256 before storing in MongoDB.
- The application uses `msvcrt` and `ctypes` for Windows-specific features.
- For best experience, run on Windows. Some features may not work on all Unix terminals.
___
## Disclaimer

This is a basic demonstration project for educational purposes. Do not use for storing sensitive data in production environments.
