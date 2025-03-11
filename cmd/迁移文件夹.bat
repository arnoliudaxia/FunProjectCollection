REM curl https://raw.githubusercontent.com/arnoliudaxia/FunProjectCollection/main/cmd/%E8%BF%81%E7%A7%BB%E6%96%87%E4%BB%B6%E5%A4%B9.bat > temp.cmd & temp.cmd & del temp.cmd

@echo off
echo 迁移文件夹 v2.1
set /p folder1="请输入要迁移的文件夹路径："
set /p folder2="请输入要迁移到的文件夹路径："

for %%I in ("%folder1%") do set "foldername=%%~nI"
echo %foldername%
echo 正在复制文件夹...
robocopy "%folder1%" "%folder2%\%foldername%" /E
@echo 请检查复制文件夹是否出现了问题，如果没有问题按回车进入下一步
pause

:delete_folder
echo 删除源文件夹... 
rmdir /s /q "%folder1%"
if errorlevel 1 (
    echo 删除源文件夹失败，请检查文件夹是否存在或是否被占用。
) else (
    echo 建立链接...
    mklink /J "%folder1%" "%folder2%\%foldername%" 
    echo 完成啦！！
)

:retry
set /p retry="是否要重试删除源文件夹并建立连接？(y/n): "
if /i "%retry%"=="y" (
    goto delete_folder
) else (
    echo 操作结束。
    pause
)