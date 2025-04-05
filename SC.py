import ctypes
import os
import sys

def run_for_admin():
    if os.name == "nt":
        if ctypes.windll.shell32.IsUserAnAdmin():
            return True
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            sys.exit()
    else:
        return False
    