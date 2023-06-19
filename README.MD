
# requiere 
```bash
pip install --upgrade sip
pip install pyqt5
pip install sympy
pip install webbrowser
pip install numpy
pip install scikit-learn
pip install joblib

```
# input example

![GIF](https://i.pinimg.com/originals/3e/f9/45/3ef945a40a3ea8e041722449bb57d59e.gif)


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
# Modelo 
> La aplicación utiliza un modelo MultinomialNB entrenado para identificar automáticamente si una ecuación es homogénea o heterogénea

[Ver en Google Colab](https://colab.research.google.com/drive/1yizO_KnHTPrrD76QGiIyHgYWCIS_R8tl?usp=sharing)


# Compilar
Instalar PyInstaller
```bash
pip install pyinstaller
```

```bash
pyinstaller index.spec
```
