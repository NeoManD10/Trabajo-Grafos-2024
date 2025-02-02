@echo off

REM Crea el entorno virtual
echo Creando entorno virtual...
python -m venv env

REM Activa el entorno virtual
call env\Scripts\activate
echo Entorno virtual ACTIVADO

REM Instala las librerías de requirements.txt
python -m pip install -r requirements.txt

REM Imprime las librerías instaladas
pip freeze

REM Desactiva el entorno virtual
deactivate
echo Entorno virtual DESACTIVADO
