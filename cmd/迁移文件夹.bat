REM curl https://raw.githubusercontent.com/arnoliudaxia/FunProjectCollection/main/cmd/%E8%BF%81%E7%A7%BB%E6%96%87%E4%BB%B6%E5%A4%B9.bat > temp.cmd & temp.cmd & del temp.cmd

@echo off
echo Ǩ���ļ��� v2.1
set /p folder1="������ҪǨ�Ƶ��ļ���·����"
set /p folder2="������ҪǨ�Ƶ����ļ���·����"

for %%I in ("%folder1%") do set "foldername=%%~nI"
echo %foldername%
echo ���ڸ����ļ���...
robocopy "%folder1%" "%folder2%\%foldername%" /E
@echo ���鸴���ļ����Ƿ���������⣬���û�����ⰴ�س�������һ��
pause

:delete_folder
echo ɾ��Դ�ļ���... 
rmdir /s /q "%folder1%"
if errorlevel 1 (
    echo ɾ��Դ�ļ���ʧ�ܣ������ļ����Ƿ���ڻ��Ƿ�ռ�á�
) else (
    echo ��������...
    mklink /J "%folder1%" "%folder2%\%foldername%" 
    echo ���������
)

:retry
set /p retry="�Ƿ�Ҫ����ɾ��Դ�ļ��в��������ӣ�(y/n): "
if /i "%retry%"=="y" (
    goto delete_folder
) else (
    echo ����������
    pause
)