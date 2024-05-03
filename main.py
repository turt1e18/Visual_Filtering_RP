from streaming.app import main as s_main
from ui.ui_program import start
import os
import subprocess


path = os.getcwd()
ui_path = os.path.join(path, "ui", "ui_program.py")

ui_process = subprocess.Popen(["python", ui_path], cwd=os.path.dirname(ui_path))
ui_process.wait()

s_main()
