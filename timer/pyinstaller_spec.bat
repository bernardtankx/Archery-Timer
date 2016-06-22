pyinstaller.exe __main__.spec

REM Modify the section where it says exe EXE = (pyz, and add on the next line:
REM Tree('data', prefix='data'),
