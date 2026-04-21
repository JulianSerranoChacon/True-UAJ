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

echo [PASO 3] Creando Heatmaps de playerHit...

echo Ejecutando analisis heatmap niveles 1, 2 y 3...
call python createHeatMaps.py

echo Creando Metricas...
call python Analisis.py

echo Creacion de heatmaps y metricas completada