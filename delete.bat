REM 使用 chcp 命令来更改 cmd 窗口的字符编码
chcp 65001 
reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v "njuptNet" /f
echo 删除成功
pause