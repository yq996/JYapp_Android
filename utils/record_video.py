import subprocess
import pytest


@pytest.fixture(scope="session", autouse=True)
def start_recording():
    cmd=f"adb shell screenrecord --time-limit 1800 /sdcard/demo.mp4"
    process=subprocess.Popen(cmd, shell=True)
    yield
    # 1. 让远程进程优雅退出
    subprocess.run("adb shell pkill -l2 screenrecord", shell=True)

    # 2. 等待本地 adb 进程退出
    process.wait()

    # 3. 拉取文件
    local_path = "./report/jyapp_video.mp4"
    subprocess.run(f"adb pull /sdcard/demo.mp4 {local_path}", shell=True)
    # 4. 删除远程文件
    subprocess.run("adb shell rm /sdcard/demo.mp4", shell=True)

