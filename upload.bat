@echo off
cd /d "d:\coding-personal\python learning"
if not exist .git (
    git init
    git remote add origin https://github.com/WenxuanWu123/python-learning-notes.git
)
git add -A
git commit -m "更新内容" 2>nul
git push -f origin main 2>nul
echo 上传完成！