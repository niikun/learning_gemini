import os
import subprocess
import winreg

def is_chrome_installed():
    # Default paths where Chrome might be installed
    default_paths = [
        "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
        "C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
    ]
    
    # Check default paths
    for path in default_paths:
        if os.path.isfile(path.replace("%USERNAME%", os.getlogin())):
            return True
    
    # Check the registry for installation path
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\chrome.exe") as key:
            path = winreg.QueryValueEx(key, "")[0]
            if os.path.isfile(path):
                return True
    except FileNotFoundError:
        pass
    
    # If Chrome is not found in the default paths or registry
    return False

# Check if Chrome is installed
if is_chrome_installed():
    print("Google Chrome is installed on this system.")
else:
    print("Google Chrome is not installed on this system.")