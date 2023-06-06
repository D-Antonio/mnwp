from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout, QWidget, QLabel, QLineEdit, QVBoxLayout, QComboBox, QStackedWidget, QTextEdit
from PyQt5.QtGui import QColor
from PyQt5 import QtCore
import webbrowser
import sympy
from sympy import symbols, diff, Function, Eq, sympify, sin, Derivative, cos, exp, E, Symbol
from sympy.parsing.sympy_parser import parse_expr
import numpy as np
import re
import csv
import math
from sklearn.feature_extraction.text import CountVectorizer
from joblib import load


class MainWindow(QWidget):
    text = ""
    vectorizer = CountVectorizer()

    def __init__(self):
        super().__init__()
        ecuaciones = []
        with open('eq.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)  # Saltar la primera fila (los encabezados)
            for row in reader:
                ecuaciones.append(row)
        self.vectorizer.fit_transform([x[0] for x in ecuaciones])
        self.model = load('./modelo_ecuaciones.joblib')

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
        self.selector_combobox.addItem("sustitución de variables")
        self.selector_combobox.addItem("serie de potencias")
        self.selector_combobox.addItem("transformada de Laplace")
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

        self.input_line_edit.setText(self.text)

        # Mostrar la vista principal
        self.stacked_widget.setCurrentWidget(home_view)

    def show_tutorial_view(self):
        webbrowser.open("https://www.youtube.com/watch?v=lo1PzjuGxFg")

    def show_info_view(self):
        text = self.input_line_edit.text()
        self.text = text
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
        text = self.input_line_edit.text()
        self.text = text
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
        self.text = text
        solution_view = QWidget()
        solution_view.setStyleSheet("background-color: #FFFBFA;")
        layout = QVBoxLayout()

        # Título
        title_label = QLabel("Solución")
        title_label.setStyleSheet("color: #BF1363; font-size: 24px; font-weight: bold;")
        title_label.setAlignment(QtCore.Qt.AlignCenter)

        # Información de la ecuación
        equation_label = QLabel(f"Ecuación: {self.eq}\n{self.eq_contex}")
        equation_label.setStyleSheet("color: black; font-size: 16px;")

        # Detalles de la ecuación
        details_label = QLabel(f"* Orden: {self.order}\n* Tipo: {self.type}\n* Grado de homogeneidad: 3")
        details_label.setStyleSheet("color: black; font-size: 16px;")

        # Solución
        solution_label = QLabel(f"Resultado de la ecuación con: {method}\n")
        solution_label.setStyleSheet("color: black; font-size: 16px;")

       # Área de texto para mostrar la solución
        solution_text_edit = QTextEdit(f"{self.solution}")
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

    def show_error_view(self, msg):
        text = self.input_line_edit.text()
        self.text = text
        error_view = QWidget()
        error_view.setStyleSheet("background-color: #FFFBFA;")
        layout = QVBoxLayout()

        # Título
        title_label = QLabel("Error")
        title_label.setStyleSheet("color: #BF1363; font-size: 24px; font-weight: bold;")
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title_label)

        # Mensaje de error
        credits_label = QLabel(f" {msg}")
        layout.addWidget(credits_label, alignment=QtCore.Qt.AlignCenter)
        
        # Botón de regresar
        back_button = QPushButton("Regresar")
        back_button.setStyleSheet("background-color: #00BD9D; color: white;")
        layout.addWidget(back_button, alignment=QtCore.Qt.AlignCenter)
        back_button.clicked.connect(self.show_home_view)
        error_view.setLayout(layout)
        self.stacked_widget.addWidget(error_view)

        # Mostrar la vista de créditos
        self.stacked_widget.setCurrentWidget(error_view)


    ##############
    #   Lógica   #
    ##############

    def is_differential(self, eq):
        if "diff" in eq:
            return True
        else:
            return False

    def detect_order(self, eq):
        max_degree = 0
        terms = re.findall(r"y'+", eq)
        for term in terms:
            if "y" in term:
                degree = term.count("'")
            if degree > max_degree:
                max_degree = degree
        return max_degree

    def is_homogeneous(self):
       eq = self.vectorizer.transform([self.eq])
       return self.model.predict(eq)[0]

    def detect_homogeneity_degree(self, e):
        # Detecta el grado de homogeneidad de la ecuación diferencial 'e'
        # Devuelve el grado de homogeneidad como un número entero
        # Contar el número de veces que aparece la variable 'x' en los términos de la ecuación
        terms = e.split('+')  # Separar los términos de la ecuación
        degree = 0
        for term in terms:
            if 'x' in term:
                degree += term.count('x')
        return degree

    def solve_homogeneous_equation(self, e, method):
        # Resuelve la ecuación diferencial homogénea 'e' con el método 'method'
        # Devuelve la solución de la ecuación como una cadena de texto
        
        x = sympy.symbols('x')  # Variable simbólica
        
        # Construir la ecuación diferencial en términos de la variable simbólica
        equation = sympy.Eq(eval(e), 0)
        
        # Resolver la ecuación diferencial homogénea según el método seleccionado
        if method == 'Sustitución de variables':
            solution = sympy.dsolve(equation)
        elif method == 'Transformada de Laplace':
            solution = sympy.laplace_transform(equation, x, sympy.symbols('s'))[0]
        elif method == 'Serie de potencias':
            solution = sympy.series(equation.rhs, x)
        else:
            solution = None
        
        # Convertir la solución en una cadena de texto
        if solution is not None:
            solution = str(solution)
        else:
            solution = "No se encontró una solución para el método seleccionado"
        
        return solution
    
    def standar_eq(self, human_equation):
        pattern = r'\(d\^(\d+)\)y/d\(x\^\1\)|dy/dx'
        def replace(match):
            if match.group(0) == 'dy/dx':
                return 'y'
            else:
                num_derivatives = int(match.group(1))
                if num_derivatives == 1:
                    return 'y'
                elif num_derivatives == 2:
                    return "y'"
                elif num_derivatives == 3:
                    return "y''"
                elif num_derivatives >= 4:
                    return "y'''"
        human_equation = re.sub(pattern, replace, human_equation)
        return human_equation

    def parse_equation(self, human_equation):
        human_equation = re.sub(r'e\*\*x|e\^x', 'exp(x)', human_equation)
        human_equation = re.sub(r'y\'\'\'', 'y.diff(x, x, x)', human_equation)
        human_equation = re.sub(r'y\'\'', 'y.diff(x, x)', human_equation)
        human_equation = re.sub(r'y\'', 'y.diff(x)', human_equation)
        human_equation = re.sub(r'(\d+)', r'\1*', human_equation)
        human_equation = human_equation.replace("^", "**")
        human_equation = human_equation.replace("e", "E")
        human_equation = re.sub(r'(\w)\^(\d+)\s*\*\s*\(\(d\^\2\)y\)/d\((\w)\^\2\)', r'\1.diff(\3)**\2 * y.diff(\3, \3)', human_equation)
        human_equation = re.sub(r'(?<=[\dxy\)])-', '-1*', human_equation)

        if '=' in human_equation:
            sides = human_equation.split('=')
            sides[0] += ' - ' + '(' + sides[1].strip() + ')'
            human_equation = sides[0]

        if human_equation.endswith("*)"):
            human_equation = human_equation[:-2] + ")"
        
        return human_equation
    
    def is_equation(self, text):
        try:
            x = symbols('x')
            y = symbols('y', cls=Function)(x)
            eqStr = self.parse_equation(text)
            if (eval(eqStr)):
                return eqStr
            else:
                return False
        except (SyntaxError, TypeError, NameError):
            return False

    def solve(self):
        # Lógica para resolver el problema con el método seleccionado
        method = self.selector_combobox.currentText()  # sustitución de variables, transformada de Laplace, serie de potencias
        text = self.input_line_edit.text()
        self.text = text
        self.eq = self.standar_eq(self.text)
        eq = self.is_equation(self.eq)
        self.order = "No aplica"
        self.type = "No aplica"
        self.solution = f"Error: No se puede resolver esta ecuación {self.eq}"

        if eq:
            if self.is_differential(eq):
                self.eq_contex = "Sí es una ecuación diferencial."
                self.order = self.detect_order(self.eq)
                self.type = self.is_homogeneous()
                if self.order > 3:
                    self.order = f"{self.order}, no se pueden resolver ecuaciones de orden mayor a 3."
                else:
                    if self.type == "homogénea":
                        #degree = self.detect_homogeneity_degree(eq)
                        #solution = self.solve_homogeneous_equation(eq, method)
                        self.show_solution_view()
                    else:
                        self.solution = "Error: No se pueden resolver ecuaciones heterogéneas."
            else:
                self.eq_contex = "Error: La ecuación no es diferencial."
            self.show_solution_view()
        else: 
            self.show_error_view(f"La ecuacion no es válida")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

# (҂·_·)
# <,︻╦╤─ ҉ - - - -
# /﹋\