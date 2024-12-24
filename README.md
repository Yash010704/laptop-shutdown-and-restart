# Shutdown App

This is a Python-based graphical user interface (GUI) application built using the Tkinter library. The app provides simple buttons to perform system-level actions such as restart, timed restart, logout, and shutdown.

## Features

- **Restart:** Immediately restarts the system.
- **Restart with Timer:** Restarts the system after a 20-second delay.
- **Logout:** Logs out the current user.
- **Shutdown:** Immediately shuts down the system.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python)

## Usage

1. **Clone or Download the Repository**
   Save the Python script (`shutdown_app.py`) to your local machine.

2. **Run the Script**
   Open a terminal or command prompt, navigate to the directory containing the script, and execute:
   ```bash
   python shutdown_app.py
   ```

3. **Interface**
   - The app will open a GUI window with four buttons:
     - `Restart`
     - `Restart time`
     - `Log-out`
     - `Shutdown`

   - Click the appropriate button to perform the desired action.

## Code Description

- **Functions:**
  - `restart()`: Executes a command to restart the system immediately.
  - `restart_time()`: Executes a command to restart the system after 20 seconds.
  - `logout()`: Executes a command to log out the current user.
  - `shutdown()`: Executes a command to shut down the system immediately.

- **UI Components:**
  - The GUI uses Tkinter buttons styled with fonts, relief effects, and custom dimensions.
  - Each button is tied to its respective function to perform the action when clicked.

## Note

- This script is intended for Windows systems as it uses Windows-specific `os.system` commands.
- Ensure you have the necessary permissions to execute system-level commands.
- Use this app with caution as these commands can immediately affect your system state.

## Disclaimer

This app is for educational purposes. The creator is not responsible for any unintended consequences arising from the use of this application.

