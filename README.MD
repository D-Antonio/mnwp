# requiere 
```bash
pip install --upgrade sip
pip install pyqt5
pip install sympy
```
# input example
Grado 1: 
~~~
y' + 3y = 2x
~~~

Grado 2:
~~~
y'' - 4y' + 4y = 0
~~~

Grado 3:
~~~
y''' - 5y'' + 7y' - 3y = 0
~~~

# Compilar
Instalar PyInstaller
```bash
pip install pyinstaller
```
Crear un archivo .specsss
```bash
pyinstaller --name=ecuaciones_diferenciales --onefile index.py
```
Crear el archivo .exe
> Este comando creará una carpeta llamada "dist" en la misma ubicación que su archivo de Python. En la carpeta "dist" encontrará el archivo .exe de su programa.
```bash
pyinstaller ecuaciones_diferenciales.spec 
```
# con librerias
~~~ bash
pyinstaller --name=ecuaciones_diferenciales --onefile --hidden-import=PyQt5 --hidden-import=PyQt5.QtWidgets --hidden-import=PyQt5.QtGui --hidden-import=PyQt5.QtCore --hidden-import=webbrowser --hidden-import=sympy --hidden-import=sympy.parsing.sympy_parser --hidden-import=numpy --hidden-import=re --hidden-import=csv --hidden-import=math --hidden-import=sklearn.feature_extraction.text --hidden-import=joblib --hidden-import=os --hidden-import=sys --add-data="eq.csv;." --add-data="modelo_ecuaciones.joblib;." index.py
~~~