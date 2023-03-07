@echo off
title Double A (Artificial Assistant)
echo Getting libraries (could take a while)...
pip install -r requirements.txt --q
echo.
cd src/
echo Starting Double A...
echo.
python __init__.py
pause