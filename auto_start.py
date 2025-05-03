import time
import pyautogui
import pygetwindow as gw
import subprocess
import pyperclip

# 启动软件
subprocess.Popen(r"C:\Program Files\CELSYS\CLIP STUDIO 1.5\CLIP STUDIO PAINT\CLIPStudioPaint.exe")
time.sleep(0.6)  # 等待软件启动

# 查找窗口
window_title = "Application requires password to start"
windows = gw.getWindowsWithTitle(window_title)

# 检查当前输入法是否为英文模式
def ensure_english_input():
    # 复制当前剪贴板内容
    original_clipboard = pyperclip.paste()

    # 清空并尝试输入一个字母
    pyperclip.copy("")
    pyautogui.write('l')
    time.sleep(0.3)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    typed = pyperclip.paste()

    # 恢复剪贴板
    pyperclip.copy(original_clipboard)

    # 如果不是英文字母 'l'，说明当前是中文输入法
    if typed != 'l':
        pyautogui.press('shift')  # 切换输入法
        time.sleep(0.2)  # 等待切换生效

if windows:
    win = windows[0]
    win.activate()
    time.sleep(1)

    ensure_english_input()  # 确保使用英文输入法

    # 发送密码
    pyautogui.write(
        "ai2 zi4 bbs.itzmx.com mian3 fei4 fen1 xiang3 fa1 xian4 fan4 mai4 ju3 bao4 tui4 kuan3 cha4 ping2 bbs.itzmx.com Always Free")
    pyautogui.press("enter")
