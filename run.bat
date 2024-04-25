@echo off
color 0a
chcp 65001
cd file/
cls

goto end


:main
echo Запуск Программы
echo Нажмите q для выхода
main.py
pause
exit

:face_gen
cd filtres
echo Запуск Программы
face_gen.py
pause
exit

:tren
cd filtres
echo Запуск Программы
tren.py
pause
exit

:end
echo Выберите действие:
echo 1 - Запуск
echo 2 - Создать пользователя
echo 3 - Запуск обучения
echo.
set /p settings="> "
set /a settings = %settings% + 0

if %settings% EQU 1 goto main
if %settings% EQU 2 goto face_gen
if %settings% EQU 3 goto tren
	