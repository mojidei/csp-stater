import time
import pyautogui
import pygetwindow as gw
import subprocess

# 启动软件
subprocess.Popen(r"C:\Program Files\CELSYS\CLIP STUDIO 1.5\CLIP STUDIO PAINT\CLIPStudioPaint.exe")
time.sleep(2)  # 等待软件启动

# 查找窗口
window_title = "Application requires password to start"
windows = gw.getWindowsWithTitle(window_title)

if windows:
    win = windows[0]
    win.activate()  # 激活窗口
    time.sleep(1)

    # 发送密码
    pyautogui.write(
        "lai2 zi4 bbs.itzmx.com mian3 fei4 fen1 xiang3 fa1 xian4 fan4 mai4 tui4 kuan3 cha4 ping2 ju3 bao4 bbs.itzmx.com Always Free",
        interval=0.05)
    pyautogui.press("enter")
