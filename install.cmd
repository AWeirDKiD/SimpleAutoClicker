@echo off

echo Ignore any errors that might pop-up.
:x

pip install keyboard
pip install win32con
pip install win32api
pip install time

echo Re-running install.cmd is recommended.
echo Press any key to rerun or close the application

PAUSE
goto x