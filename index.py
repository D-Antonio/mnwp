from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout, QWidget, QLabel, QLineEdit, QVBoxLayout, QComboBox
from sympy import *
from sympy.abc import x, y

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ecuaciones Diferenciales')
        self.setGeometry(100, 100, 400, 200)
        # Crear el combobox para escoger el grado de la ecuación diferencial
        self.combobox_grado = QComboBox()
        self.combobox_grado.addItem('Primer grado')
        self.combobox_grado.addItem('Segundo grado')
        self.combobox_grado.addItem('Tercer grado')
        # Crear el label y el campo de texto para escribir la ecuación diferencial
        self.label_ecuacion = QLabel('Escribe la ecuación diferencial:')
        self.textbox_ecuacion = QLineEdit()
        self.label2 = QLabel("La fórmula de la ecuación diferencial es:")
        self.label3 = QLabel()
        # Crear el botón de validar
        self.boton_validar = QPushButton('Validar')
        # Conectar el botón de validar con la función correspondiente
        self.boton_validar.clicked.connect(self.validar_ecuacion)
        # Crear los layouts y añadir los widgets correspondientes
        layout_vertical = QVBoxLayout()
        layout_horizontal = QHBoxLayout()
        layout_vertical.addWidget(self.combobox_grado)
        layout_vertical.addWidget(self.label_ecuacion)
        layout_vertical.addWidget(self.textbox_ecuacion)
        layout_vertical.addWidget(self.label2)
        layout_vertical.addWidget(self.label3)
        layout_vertical.addWidget(self.boton_validar)
        layout_horizontal.addLayout(layout_vertical)
        # Crear el diseño de la ventana
        
        # Conectar la señal del cambio de texto en la entrada con la función actualizar_ecuacion
        self.textbox_ecuacion.textChanged.connect(self.actualizar_ecuacion)
        
        self.setLayout(layout_horizontal)


    def validar_ecuacion(self):
        # Obtener el grado de la ecuación diferencial escogido
        grado = self.combobox_grado.currentText()

        # Obtener la ecuación diferencial ingresada
        ecuacion = self.textbox_ecuacion.text()

        # Validar la ecuación diferencial
        if grado == 'Primer grado':
            # Aquí podrías implementar la validación para una ecuación diferencial de primer grado
            print('Validación para ecuación de primer grado')

        elif grado == 'Segundo grado':
            # Aquí podrías implementar la validación para una ecuación diferencial de segundo grado
            print('Validación para ecuación de segundo grado')

        elif grado == 'Tercer grado':
            # Aquí podrías implementar la validación para una ecuación diferencial de tercer grado
            print('Validación para ecuación de tercer grado')
        
        # Conectar la señal del cambio de texto en la entrada con la función actualizar_ecuacion
        
    def actualizar_ecuacion(self):
        # Obtener el texto de la entrada
        ecuacion = self.textbox_ecuacion.text()
        
        # Parsear la ecuación diferencial usando sympy
        try:
            expr = Eq(Derivative(y, x), parse_expr(ecuacion))
        except:
            self.label3.setText("La ecuación no es válida")
            return
        
        # Mostrar la fórmula de la ecuación en la etiqueta de salida
        formula = latex(expr)
        self.label3.setText(formula)

if __name__ == "__main__":
    # Inicializar la aplicación y la ventana principal
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    
    # Ejecutar la aplicación
    app.exec_()
