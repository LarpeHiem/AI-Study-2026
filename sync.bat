@echo off
git add .
git commit -m "auto: update daily log %date%"
git push origin main
echo 同步完成！
pause