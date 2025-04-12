# 🔐 Auto-WiFi Tool
A simple Python tool that allows you to view saved Wi-Fi (SSID) names and their passwords using the Windows `netsh` command — all through a clean terminal interface!

---

## ✨ Features

- View all saved Wi-Fi network names on your PC.
- Get the password for any saved Wi-Fi network (SSID).
- Opens a new colored Command Prompt window for each task.
- Easy-to-use interactive CLI interface.
- Cross-verified with native Windows commands.

---

## ⚙️ Manual CMD Commands (if you prefer CLI)
 **You can also run these commands directly in Command Prompt**:
 
`netsh wlan show profiles`

`netsh wlan show profile name="YourSSID" key=clear`

---

## 📦 Cloning the Repository

To clone this repository locally:

```bash
git clone https://github.com/Naeem-360/Auto-wifi-tool.git
