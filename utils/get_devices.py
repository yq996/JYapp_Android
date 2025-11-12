import socket
import subprocess
import allure

def get_devices_id():
    cmd ="adb devices"
    result=subprocess.run(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output=result.stdout.decode("utf-8").strip().splitlines()
    devices = []
    for line in output:
        if line.strip()=="" or "List of devices" in line:
            continue
        device_id=line.split()[0]
        devices.append(device_id)
    return devices

def get_free_port(start, end):
    """扫描端口池，返回第一个可用端口"""
    for port in range(start, end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    raise RuntimeError("没有可用的 systemPort 了！")

def make_devices_list(start_port, system_port_start):
    devices_ids = get_devices_id()
    devices = []

    for udid in devices_ids:
        system_port = get_free_port(system_port_start, system_port_start + 99)  # 假设最多 100 个设备
        devices.append({
            "udid": udid,
            "port": start_port,      # Appium server 主端口
            "systemPort": system_port  # 自动选择可用 systemPort
        })
        # 下一个设备从下一个端口开始搜索，避免重复
        system_port_start = system_port + 1
    return devices
