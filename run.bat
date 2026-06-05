@echo off
start "My Python App" cmd /k "python "%~dp0main.py""
if errorlevel 1 pause
