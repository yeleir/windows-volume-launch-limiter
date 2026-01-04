# Windows Limiter

> A simple Python script that ensures any newly launched applications start with a safe, preset volume level (default 10%).

---

## 📋 Table of Contents
- [About the Project](#about-the-project)
- [Built With](#built-with)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contact](#contact)

---

## 📖 About the Project
Me and my friend were discussing how annoying it is that certain applications don't hold their previous audio levels. When relaunching them, you get hit with an immediate *BOOM* of 100% audio, destroying your eardrums. 

Running this script via the command window ensures any applications launched afterward start at a value of 10% volume instead of 100%. Currently, this version uses the **Pycaw (Python Computer Audio Control)** library to interface with the Windows Core Audio API to monitor and adjust active sessions in real-time.

Currently this version uses 15.2 MB when running. 

### Screenshots
![Project Screenshot](images/vl-screenshot.png)

---

## 🛠 Built With
- **Language:** Python 3.x
- **Libraries:** - 
[Pycaw](https://github.com/AndreMiras/pycaw) (Core Audio Control) 
[Comtypes](https://pythonhosted.org/comtypes/) (COM interface)
- **Tools:** Git, VS Code

---

## ✨ Features
- **Automatic Volume Capping**: Automatically detects new audio sessions and caps them at 10% volume instantly.
- **Background Monitoring**: Runs as a lightweight process in your terminal, monitoring for application launches without heavy CPU usage.
- **Ear Protection**: Eliminates "volume jumps" from apps that don't remember user settings or default to maximum volume.

---

## 🚀 Getting Started

### Prerequisites
* **Windows OS**: This script relies on Windows-specific APIs.
* **Python 3.7+**: Ensure Python is installed and added to your PATH.

### Installation
1. Clone the repo:
   ```bash
   git clone [https://github.com/your-username/windows-limiter.git](https://github.com/your-username/windows-limiter.git)

### ⚙️ Run on Startup (Optional)
To ensure your ears are protected every time you boot your PC, you can set the script to run automatically in the background:

1. **Create a Shortcut**:
   - Right-click your `limiter.py` file and select **Create shortcut**.
2. **Open the Windows Startup Folder**:
   - Press `Win + R` on your keyboard.
   - Type `shell:startup` and hit **Enter**.
3. **Move the Shortcut**:
   - Drag the shortcut you created into the folder that just opened.
4. **Run Silently (Background Mode)**:
   - If you don't want a command prompt window to stay open, rename your script from `limiter.py` to `limiter.pyw`. 
   - Windows will then run the script invisibly in the background using `pythonw.exe`.

---

