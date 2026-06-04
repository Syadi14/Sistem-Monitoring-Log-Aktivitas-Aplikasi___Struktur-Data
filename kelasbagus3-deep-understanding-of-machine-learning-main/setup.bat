@echo off
REM ==========================
REM Setup YOLOv5 Environment - Windows (CMD)
REM ==========================

REM 1. Buat virtual environment
python -m venv yolov5_venv
IF %ERRORLEVEL% NEQ 0 (
  echo Gagal membuat virtual environment. Pastikan Python ter-install dan ada di PATH.
  exit /b 1
)
echo Virtual environment "yolov5_venv" dibuat.

REM 2. Aktifkan venv
call yolov5_venv\Scripts\activate.bat
IF NOT DEFINED VIRTUAL_ENV (
  echo Gagal mengaktifkan virtual environment.
  exit /b 1
)
echo Virtual environment aktif.

REM 3. Upgrade pip
python -m pip install --upgrade pip

REM 4. Install dependencies
pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
  echo Instalasi dependencies gagal. Periksa file requirements.txt.
  exit /b 1
)
echo Semua dependencies terinstall.

REM 5. Instruksi setelah setup
echo.
echo Setup selesai. Untuk menjalankan training:
echo 1. Aktifkan venv: call yolov5_venv\Scripts\activate.bat
echo 2. Jalankan script training: python train_yolo.py
