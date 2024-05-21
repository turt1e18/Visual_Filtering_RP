# from streaming.app import main as s_main
# import os
# import subprocess


# path = os.getcwd()
# ui_path = os.path.join(path, "ui", "ui_program.py")

# ui_process = subprocess.Popen(["python", ui_path], cwd=os.path.dirname(ui_path))
# ui_process.wait()

# s_main()

import os
import subprocess
from streaming.app import main as s_main

def run_ui_and_main():
    # 현재 작업 디렉토리를 가져옴
    path = os.getcwd()

    # UI 파일의 경로 설정
    ui_path = os.path.join(path, "ui", "ui_program.py")

    # UI 파일 실행
    ui_process = subprocess.Popen(["python", ui_path], cwd=os.path.dirname(ui_path))
    ui_process.wait()

    # s_main 함수 실행
    s_main()

if __name__ == "__main__":
    run_ui_and_main()