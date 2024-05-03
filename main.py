from streaming.app import main as s_main
import os
import subprocess


path = os.getcwd()
ui_path = os.path.join(path, "ui", "ui_program.py")

ui_process = subprocess.Popen(["python", ui_path], cwd=os.path.dirname(ui_path))
ui_process.wait()

s_main()
