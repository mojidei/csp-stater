# csp-stater
鄙人在安装了某盗版csp（一款绘画软件）后，每天的第一次启动都需要输入一长串字符串，这不优雅。为了优雅，搞了这个东西。
## 如何使用？
release里面下载exe文件。
新建一个快捷方式指向这个exe文件，然后设置图标为csp的图标即可。
## 出现错误？
给我提issue
## 打包？
我用的pyinstaller
```ps
pyinstaller --onefile --noconsole --icon=icon.ico auto_start.py
```