@echo off
echo Installing libraries...

python -m pip install spacy
python -m spacy download en

pause