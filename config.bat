@echo off
REM 使用 chcp 命令来更改 cmd 窗口的字符编码
chcp 65001 
setlocal EnableDelayedExpansion

set KEY_NAME=HKCU\Software\Microsoft\Windows\CurrentVersion\Run
set VALUE_NAME="njuptNet"
set VALUE_DATA=%cd%\start.bat

REM 判断注册表项是否存在
reg query %KEY_NAME% /v %VALUE_NAME% >nul 2>&1
if %errorlevel% == 0 (
    echo %VALUE_NAME% 已存在，不需要重复添加。
) else (
    REM 将程序路径写入注册表
    reg add %KEY_NAME% /v %VALUE_NAME% /t REG_SZ /d "%VALUE_DATA%" /f
    if !errorlevel! == 0 (
        echo "!VALUE_NAME!" 添加成功。
    ) else (
        echo "!VALUE_NAME!" 添加失败，请检查权限。
    )
)

pause
