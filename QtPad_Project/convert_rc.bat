@echo off

rem 引数の数を確認
if "%1"=="" goto :show_usage
if "%2"=="" goto :show_usage

rem プロジェクトディレクトリのパスを設定
set PROJECT_DIR=C:\Your\Project\Directory

rem リソースファイルの変換
pyside6-rcc "%PROJECT_DIR%\%1" -o "%PROJECT_DIR%\%2"

goto :end

:show_usage
echo Usage: convert_rc.bat <input_qrc_relative_to_project> <output_rc_py_relative_to_project>
exit /b 1

:end