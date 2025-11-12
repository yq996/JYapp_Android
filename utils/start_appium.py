import subprocess
import psutil
import pytest
import allure
def is_port_in_use(port):
    """判断本地端口是否被占用"""
    #psutil.net_connections(kind='inet')会返回所有 TCP/UDP 网络连接信息
    #conn.laddr.port是本地端口
    #conn.status == psutil.CONN_LISTEN,表示这个端口处于 监听状态，即已经被某个进程占用。
    for conn in psutil.net_connections(kind='inet'):
        if conn.laddr.port == port and conn.status == psutil.CONN_LISTEN:
            return True
    return False
@pytest.fixture(scope="session",autouse=True)
def start_appium(port=4723):
    if not is_port_in_use(port):
        print(f"\n这次测试第一次打开appium服务{port}")
        cmd = f"appium -p {port}"
        subprocess.Popen(cmd, shell=True)
    else:
        print(f"\n这次测试的appium服务{port}已经打开过了！无需重复打开！")
