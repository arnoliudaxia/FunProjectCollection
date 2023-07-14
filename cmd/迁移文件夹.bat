@echo off
set /p folder1=请输入要迁移的文件夹路径：
set /p folder2=请输入要迁移到的文件夹路径：

for %%I in ("%folder1%") do set "foldername=%%~nI"
echo %foldername%
echo 正在复制文件夹...
robocopy %folder1% "%folder2%\%foldername%" /MIR
@echo 请检查复制文件夹是否出现了问题，如果没有问题按回车进入下一步
pause
rmdir /s /q %folder1%

mklink /J %folder1% "%folder2%\%foldername%" 
pause