@echo off
set /p folder1=������ҪǨ�Ƶ��ļ���·����
set /p folder2=������ҪǨ�Ƶ����ļ���·����

for %%I in ("%folder1%") do set "foldername=%%~nI"
echo %foldername%
echo ���ڸ����ļ���...
robocopy %folder1% "%folder2%\%foldername%" /MIR
@echo ���鸴���ļ����Ƿ���������⣬���û�����ⰴ�س�������һ��
pause
rmdir /s /q %folder1%

mklink /J %folder1% "%folder2%\%foldername%" 
pause