@echo off
title Hosts Updater (Admin Required)

:: بررسی دسترسی ادمین
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Requesting administrator privileges...
    :: اجرای مجدد با دسترسی ادمین با استفاده از PowerShell
    powershell -Command "Start-Process -Verb RunAs -Wait -FilePath '%~f0'"
    exit /b
)

:: رسیدن به اینجا یعنی دسترسی ادمین داریم
cd /d "%~dp0"
echo Running Python script with admin privileges...
python dns_fighter.py

echo.
echo Script finished. Press any key to exit...
pause >nul
exit /b