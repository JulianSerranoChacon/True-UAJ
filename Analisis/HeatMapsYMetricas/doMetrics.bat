@echo off
setlocal

echo Iniciando creacion de heatmaps

if not exist ".venv" (
    echo [PASO 1] Creando entorno virtual...
    python -m venv .venv
    if %errorlevel% neq 0 (
        echo ERROR: No se pudo crear el entorno virtual. Asegurate de tener Python instalado.
        pause
        exit /b %errorlevel%
    )
) else (
    echo [PASO 1] El entorno virtual ya existe.
)

echo [PASO 2] Instalando dependencias desde requirements.txt...
call .\.venv\Scripts\activate.bat
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Hubo un problema al instalar las dependencias.
    pause
    exit /b %errorlevel%
)

echo [PASO 3] Creando heatmaps de playerHit...

echo Ejecutando Nivel 1...
call python analyzeNivel1.py

echo Ejecutando Nivel 2...
call python analyzeNivel2.py

echo Ejecutando Nivel 3...
call python analyzeNivel3.py

echo Creando Metricas...
call python Analisis.py

echo Creacion de heatmaps completada