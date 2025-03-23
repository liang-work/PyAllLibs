import ctypes
import os
import sys
import subprocess

def run_for_admin():
    if os.name == "nt":
        if ctypes.windll.shell32.IsUserAnAdmin():
            return True
        else:
            subprocess.Popen([ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)], shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)
            sys.exit()
    else:
        return False
    