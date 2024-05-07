import subprocess
import re


def get_resolution_60fps(device):
    command = ['v4l2-ctl', '-d', device, '--list-formats-ext']
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        lines = result.stdout.split('\n')
        resolutions = []
        for line in lines:
            parts = line.split()
            if 'Size' in line:
                resolution = parts[2]
            elif 'fps' in line:
                fps_index = re.search(r'\d+\.\d+', parts[3]).group()
                fps = float(fps_index)
                if fps == 60:
                    resolutions.append(resolution)
        return resolutions
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None


def get_device():
    pass


if __name__ == "__main__":
    device = '/dev/video1'
    print(get_resolution_60fps(device))


