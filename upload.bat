@echo off
chcp 65001 >nul
cd /d "d:\coding-personal\python learning"

if not exist .git (
    echo Initializing Git repository...
    git init
    git remote add origin https://github.com/WenxuanWu123/python-learning-notes.git
)

echo Adding files...
git add -A

echo Committing changes...
git commit -m "Update content" --allow-empty >nul 2>&1

echo Pushing to GitHub...
git push -f origin main >nul 2>&1

if %ERRORLEVEL% EQU 0 (
    echo Upload successful!
) else (
    echo Upload failed, please check network connection
)

pause