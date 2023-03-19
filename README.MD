# requiere 
```bash
pip install --upgrade sip
pip install pyqt5
pip install sympy
```
# Compilar
Instalar PyInstaller
```bash
pip install pyinstaller
```
Crear un archivo .specsss
```bash
pyinstaller --name=ecuaciones_diferenciales --onefile indexss.py
```
Crear el archivo .exe
> Este comando creará una carpeta llamada "dist" en la misma ubicación que su archivo de Python. En la carpeta "dist" encontrará el archivo .exe de su programa.
```bash
pyinstaller ecuaciones_diferenciales.spec 
```
