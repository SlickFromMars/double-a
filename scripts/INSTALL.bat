@echo off
cd ../
title Library Installation
echo Setting up virtual environment...
echo.
python -m venv venv
echo.
echo Installing libraries...
echo.
pip install -r requirements.txt
echo.
echo Installation complete.
pause