from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout, QWidget, QLabel, QLineEdit, QVBoxLayout, QComboBox, QStackedWidget, QTextEdit
from PyQt5.QtGui import QColor
from PyQt5 import QtCore
import webbrowser

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JEdyCalc")
        self.stacked_widget = QStackedWidget()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.stacked_widget)
        self.show_home_view()

    ############
    #  DISEÑO  # 
    ############

    def show_home_view(self):
        home_view = QWidget()
        home_view.setStyleSheet("background-color: #FFFBFA;")
        layout = QVBoxLayout()

        # Botones superiores
        buttons_layout = QHBoxLayout()
        info_button = QPushButton("Información")
        info_button.setStyleSheet("background-color: #00BD9D; color: white;")
        tutorial_button = QPushButton("Tutorial")
        tutorial_button.setStyleSheet("background-color: #00BD9D; color: white;")
        credits_button = QPushButton("Créditos")
        credits_button.setStyleSheet("background-color: #00BD9D; color: white;")
        buttons_layout.addWidget(credits_button)
        buttons_layout.addWidget(tutorial_button)
        buttons_layout.addWidget(info_button)

        # Título
        title_label = QLabel("JEdyCalc")
        title_label.setStyleSheet("color: #BF1363; font-size: 24px; font-weight: bold;")
        title_label.setAlignment(QtCore.Qt.AlignCenter)

        # Input
        self.input_line_edit = QLineEdit()
        self.input_line_edit.setStyleSheet("background-color: white; border: 1px solid #ccc; padding: 5px; ")

        # Selector
        self.selector_combobox = QComboBox()
        self.selector_combobox.addItem("Método 1")
        self.selector_combobox.addItem("Método 2")
        self.selector_combobox.addItem("Método 3")
        self.selector_combobox.setStyleSheet("background-color: white;color: black; border: 1px solid #ccc;  padding: 5px; selection-background-color: #00BD9D;")
        self.selector_combobox.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.selector_combobox.view().setStyleSheet("color: black;")

        # Botón Resolver
        solve_button = QPushButton("Resolver")
        solve_button.setStyleSheet("background-color: #00BD9D; color: white;")

        # Agregar widgets al diseño
        layout.addLayout(buttons_layout)
        layout.addWidget(title_label)
        layout.addWidget(self.input_line_edit)
        layout.addWidget(self.selector_combobox)
        layout.addWidget(solve_button)
        home_view.setLayout(layout)
        self.stacked_widget.addWidget(home_view)

        # Conexiones de los botones
        info_button.clicked.connect(self.show_info_view)
        tutorial_button.clicked.connect(self.show_tutorial_view)
        credits_button.clicked.connect(self.show_credits_view)
        solve_button.clicked.connect(self.solve)

        # Mostrar la vista principal
        self.stacked_widget.setCurrentWidget(home_view)


    def show_tutorial_view(self):
        webbrowser.open("https://www.youtube.com/watch?v=lo1PzjuGxFg")

    def show_info_view(self):
        info_view = QWidget()
        info_view.setStyleSheet("background-color: #FFFBFA;")
        layout = QVBoxLayout()

        # Contenido de la vista de información
        info_label = QLabel("Aquí va la información de la aplicación.")
        layout.addWidget(info_label, alignment=QtCore.Qt.AlignCenter)

        # Botón de regresar
        back_button = QPushButton("Regresar")
        back_button.setStyleSheet("background-color: #00BD9D; color: white;")
        layout.addWidget(back_button, alignment=QtCore.Qt.AlignCenter)
        back_button.clicked.connect(self.show_home_view)
        info_view.setLayout(layout)
        self.stacked_widget.addWidget(info_view)

        # Mostrar la vista de información
        self.stacked_widget.setCurrentWidget(info_view)

    def show_credits_view(self):
        credits_view = QWidget()
        credits_view.setStyleSheet("background-color: #FFFBFA;")
        layout = QVBoxLayout()

        # Contenido de la vista de créditos
        credits_label = QLabel("Aquí van los créditos de la aplicación.")
        layout.addWidget(credits_label, alignment=QtCore.Qt.AlignCenter)

        # Botón de regresar
        back_button = QPushButton("Regresar")
        back_button.setStyleSheet("background-color: #00BD9D; color: white;")
        layout.addWidget(back_button, alignment=QtCore.Qt.AlignCenter)
        back_button.clicked.connect(self.show_home_view)
        credits_view.setLayout(layout)
        self.stacked_widget.addWidget(credits_view)

        # Mostrar la vista de créditos
        self.stacked_widget.setCurrentWidget(credits_view)

    def show_solution_view(self):
        method = self.selector_combobox.currentText()
        text = self.input_line_edit.text()
        solution_view = QWidget()
        solution_view.setStyleSheet("background-color: #FFFBFA;")
        layout = QVBoxLayout()

        # Título
        title_label = QLabel("Solución")
        title_label.setStyleSheet("color: #BF1363; font-size: 24px; font-weight: bold;")
        title_label.setAlignment(QtCore.Qt.AlignCenter)

        # Información de la ecuación
        equation_label = QLabel(f"Ecuación: {text}\nSí es una ecuación diferencial")
        equation_label.setStyleSheet("color: black; font-size: 16px;")

        # Detalles de la ecuación
        details_label = QLabel("* Orden: 2\n* Tipo: Homogénea\n* Grado de homogeneidad: 3")
        details_label.setStyleSheet("color: black; font-size: 16px;")

        # Solución
        solution_label = QLabel(f"Resultado de la ecuación con el {method}\n")
        solution_label.setStyleSheet("color: black; font-size: 16px;")

       # Área de texto para mostrar la solución
        solution_text_edit = QTextEdit("123... aquí la solucion")
        solution_text_edit.setStyleSheet("background-color: white; border: 1px solid #ccc; padding: 5px;")
        solution_text_edit.setFixedHeight(3 * solution_text_edit.fontMetrics().height())
        solution_text_edit.setReadOnly(True)  # Deshabilitar la edición del texto

        # Botón Regresar
        back_button = QPushButton("Regresar")
        back_button.setStyleSheet("background-color: #00BD9D; color: white;")

        # Conexión del botón Regresar
        back_button.clicked.connect(self.show_home_view)

        # Agregar widgets al diseño
        layout.addWidget(title_label)
        layout.addWidget(equation_label)
        layout.addWidget(details_label)
        layout.addWidget(solution_label)
        layout.addWidget(solution_text_edit)
        layout.addWidget(back_button)
        solution_view.setLayout(layout)
        self.stacked_widget.addWidget(solution_view)

        # Mostrar la vista de solución
        self.stacked_widget.setCurrentWidget(solution_view)


    ##############
    #   Lógica   #
    ##############

    def solve(self):
        # Lógica para resolver el problema con el método seleccionado
        method = self.selector_combobox.currentText()
        text = self.input_line_edit.text()
        def solve(self):
        # Lógica para resolver el problema con el método seleccionado
    method = self.selector_combobox.currentText()
    text = self.input_line_edit.text()
    
    # Realizar la operación correspondiente
    if text.startswith('d'):
        # Si la ecuación es diferencial
        order = detect_order(text)
        
        if order is None:
            # Mostrar mensaje de error indicando que la ecuación no es diferencial
            self.show_error_message("La ecuación ingresada no es una ecuación diferencial.")
        elif order > 3:
            # Mostrar mensaje de error indicando que el programa no puede resolver ecuaciones de orden mayor a 3
            self.show_error_message("El programa no puede resolver ecuaciones de orden mayor a 3.")
        else:
            is_homogeneous = detect_homogeneity(text)
            
            if is_homogeneous:
                # Si la ecuación es homogénea
                degree = detect_homogeneity_degree(text)
                solution = solve_homogeneous_equation(text, method)
                self.show_solution(solution)
            else:
                # Mostrar mensaje de error indicando que el programa no puede resolver ecuaciones heterogéneas
                self.show_error_message("El programa no puede resolver ecuaciones heterogéneas.")
    else:
        # Mostrar mensaje de error indicando que no se ingresó una ecuación diferencial
        self.show_error_message("No se ingresó una ecuación diferencial.")

def detect_order(equation):
    # Lógica para detectar el orden de la ecuación diferencial
    if '^' in equation:
        order_str = equation.split('^')[1].strip()
        if order_str.isdigit():
            return int(order_str)
    return None

def detect_homogeneity(equation):
    # Lógica para detectar si la ecuación diferencial es homogénea o heterogénea
    if 'y' in equation:
        return True
    return False

def detect_homogeneity_degree(equation):
    # Lógica para detectar el grado de homogeneidad de la ecuación diferencial
    degree_str = equation.split('y')[1].strip()
    if degree_str.isdigit():
        return int(degree_str)
    return None

import sympy as sp
import numpy as np

def solve_differential_equation(equation, method):
    # Lógica para resolver la ecuación diferencial según el método seleccionado
    if method == "Método 1":
        solution = solve_differential_equation_method_1(equation)
    elif method == "Método 2":
        solution = solve_differential_equation_method_2(equation)
    elif method == "Método 3":
        solution = solve_differential_equation_method_3(equation)
    else:
        solution = "Método no válido"
    return solution

def solve_differential_equation_method_1(equation):
    # se utiliza la biblioteca SymPy para resolver la ecuación diferencial simbólicamente. 
    # La función dsolve se encarga de resolver la ecuación diferencial y devuelve la solución simbólica.
    
    x = sp.symbols('x')
    y = sp.Function('y')(x)

    # Obtener la ecuación diferencial simbólica
    differential_eq = sp.Eq(equation, 0)

    # Resolver la ecuación diferencial simbólica
    solution = sp.dsolve(differential_eq, y)

    return solution

def solve_differential_equation_method_2(equation):
    # se utiliza la biblioteca NumPy para resolver la ecuación diferencial numéricamente mediante el método de integración numérica odeint. 
    # Se define la ecuación diferencial como una función y se especifica el valor inicial y0 y el rango de valores para x. 
    # La función odeint devuelve la solución numérica y para cada valor de x.
    
    x = np.linspace(0, 1, 100)  # Rango de valores para x
    y0 = 1  # Valor inicial de y en x=0

    # Definir la ecuación diferencial en forma de función
    def differential_eq(y, x):
        return equation

    # Resolver la ecuación diferencial numéricamente
    y = sp.odeint(differential_eq, y0, x)

    return y

def solve_differential_equation_method_3(equation):
    # En el método solve_differential_equation_method_3, también se utiliza la biblioteca SymPy para resolver la ecuación diferencial simbólicamente, 
    # pero en este caso se emplea el método de solución mediante series de potencias utilizando la función rsolve.
    
    x = sp.symbols('x')
    y = sp.Function('y')(x)

    # Obtener la ecuación diferencial simbólica
    differential_eq = sp.Eq(equation, 0)

    # Resolver la ecuación diferencial simbólica mediante series de potencias
    series_solution = sp.rsolve(differential_eq, y)

    return series_solution

 def show_solution(self, result):
        solution_view = QWidget()
        solution_view.setStyleSheet("background-color: #FFFBFA;")
        layout = QVBoxLayout()

        # Contenido de la vista de solución
        result_label = QLabel(f"El resultado es: {result}")
        result_label.setStyleSheet("color: #BF1363; font-size: 16px;")

        layout.addWidget(result_label)
        solution_view.setLayout(layout)
        self.stacked_widget.addWidget(solution_view)

        # Mostrar la vista de solución
        self.stacked_widget.setCurrentWidget(solution_view)

    def show_error_message(self, message):
        error_view = QWidget()
        error_view.setStyleSheet("background-color: #FFFBFA;")
        layout = QVBoxLayout()

        # Contenido de la vista de error
        error_label = QLabel(f"Error: {message}")
        error_label.setStyleSheet("color: #BF1363; font-size: 16px;")

        layout.addWidget(error_label)
        error_view.setLayout(layout)
        self.stacked_widget.addWidget(error_view)

        # Mostrar la vista de error
        self.stacked_widget.setCurrentWidget(error_view)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()