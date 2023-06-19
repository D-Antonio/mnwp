from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout, QWidget, QLabel, QLineEdit, QVBoxLayout, QComboBox, QStackedWidget, QTextEdit, QScrollArea
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtCore
import webbrowser
import sympy as sp
from sympy import symbols, diff, Function, pretty, Eq, sympify, sin, apart, latex, Derivative, LaplaceTransform, cos, exp, log, E, Symbol, dsolve, series, O, collect, factorial, pprint
from sympy.parsing.sympy_parser import parse_expr
from sympy.solvers.ode import dsolve
import numpy as np
import re
import math
from sklearn.feature_extraction.text import CountVectorizer
from joblib import load
import csv
import os
import sys

class MainWindow(QWidget):
    text = ""
    creditos = ""
    info = ""
    link = ""
    vectorizer = CountVectorizer()

    def __init__(self):
        super().__init__()
        ruta_ejecutable = os.path.dirname(sys.executable)
        ecuaciones = []
        with open("creditos.html", "r", encoding="utf-8") as file:
            self.creditos = file.read()
        with open("info.html", "r", encoding="utf-8") as file:
            self.info = file.read()
        with open("link.txt", "r", encoding="utf-8") as file:
            self.link = file.read()
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
        info_button.setStyleSheet("background-color: #00BD9D; color: white; font-size: 24px; font-weight: bold;")
        tutorial_button = QPushButton("Tutorial")
        tutorial_button.setStyleSheet("background-color: #00BD9D; color: white; font-size: 24px; font-weight: bold;")
        credits_button = QPushButton("Créditos")
        credits_button.setStyleSheet("background-color: #00BD9D; color: white; font-size: 24px; font-weight: bold;")
        buttons_layout.addWidget(credits_button)
        buttons_layout.addWidget(tutorial_button)
        buttons_layout.addWidget(info_button)

        # Título
        title_label = QLabel("JEdyCalc")
        title_label.setStyleSheet("color: #BF1363; font-size: 32px; font-weight: bold;")
        title_label.setAlignment(QtCore.Qt.AlignCenter)

        # Input
        self.input_line_edit = QLineEdit()
        self.input_line_edit.setStyleSheet("background-color: white; border: 1px solid #ccc; padding: 5px; font-size: 24px;")

        # Selector
        self.selector_combobox = QComboBox()
        self.selector_combobox.addItem("sustitución de variables")
        self.selector_combobox.addItem("serie de potencias")
        self.selector_combobox.addItem("transformada de Laplace")
        self.selector_combobox.setStyleSheet("background-color: white;color: black; border: 1px solid #ccc; font-size: 24px; padding: 5px; selection-background-color: #00BD9D;")
        self.selector_combobox.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.selector_combobox.view().setStyleSheet("color: black;")

        # Botón Resolver
        solve_button = QPushButton("Resolver")
        solve_button.setStyleSheet("background-color: #00BD9D; color: white; font-size: 24px; font-weight: bold;")

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

        def disable_solve_button():
            solve_button.setStyleSheet("background-color: #ffc501; color: white; font-size: 24px;")
            solve_button.setEnabled(False)
            solve_button.setText("Cargando...")
            QApplication.processEvents()
            self.solve()

        solve_button.clicked.connect(disable_solve_button)

        self.input_line_edit.setText(self.text)

        home_view.setFixedSize(800, 520)

        # Mostrar la vista principal
        self.stacked_widget.setCurrentWidget(home_view)

    def show_tutorial_view(self):
        webbrowser.open(self.link)

    def show_info_view(self):
        text = self.input_line_edit.text()
        self.text = text
        info_view = QWidget()
        info_view.setStyleSheet("background-color: #FFFBFA;")
        info_view.setFixedSize(800, 520)  # Establecer tamaño fijo
        layout = QVBoxLayout()

        # Título
        title_label = QLabel("Información")
        title_label.setStyleSheet("color: #BF1363; font-size: 32px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Contenido de la vista de información
        info_scroll_area = QScrollArea() 
        info_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        info_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        info_scroll_area.setWidgetResizable(True)

        info_label = QLabel(f"{self.info}")
        # info_label.setAlignment(Qt.AlignCenter)
        info_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        info_label.setWordWrap(True)
        info_scroll_area.setWidget(info_label)

        info_scroll_area.setStyleSheet(
            "QScrollBar:vertical {"
            "    width: 10px;"
            "    background-color: #F0F0F0;"
            "}"
            "QScrollBar::handle:vertical {"
            "    background-color: #CCCCCC;"
            "}"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {"
            "    height: 0px;"
            "}"
            "QScrollArea {"
            "    padding: 0;"
            "    border: 0;"
            "}"
        )

        layout.addWidget(info_scroll_area)

        # Botón de regresar
        back_button = QPushButton("Regresar")
        back_button.setStyleSheet("background-color: #00BD9D; color: white; font-size: 24px; font-weight: bold;")
        layout.addWidget(back_button)
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
        credits_view.setFixedSize(800, 520)
        layout = QVBoxLayout()

        # Título
        title_label = QLabel("Créditos")
        title_label.setStyleSheet("color: #BF1363; font-size: 32px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Contenido de la vista de créditos
        credits_scroll_area = QScrollArea() 
        credits_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        credits_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        credits_scroll_area.setWidgetResizable(True)

        credits_scroll_area.setStyleSheet(
            "QScrollBar:vertical {"
            "    width: 10px;"
            "    background-color: #F0F0F0;"
            "}"
            "QScrollBar::handle:vertical {"
            "    background-color: #CCCCCC;"
            "}"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {"
            "    height: 0px;"
            "}"
            "QScrollArea {"
            "    padding: 0;"
            "    border: 0;"
            "}"
        )

        credits_label = QLabel(f"{self.creditos}")
        credits_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        credits_label.setWordWrap(True)

        credits_scroll_area.setWidget(credits_label)
        layout.addWidget(credits_scroll_area)

        # Botón de regresar
        back_button = QPushButton("Regresar")
        back_button.setStyleSheet("background-color: #00BD9D; color: white; font-size: 24px; font-weight: bold;")
        layout.addWidget(back_button)
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
        title_label.setStyleSheet("color: #BF1363; font-size: 32px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignCenter)

        # Información de la ecuación
        equation_label = QLabel(f"Ecuación: {self.eq}\n{self.eq_contex}")
        equation_label.setStyleSheet("color: black; font-size: 24px;")

        # Detalles de la ecuación
        details_label = QLabel("<ul>" 
                                    f"<li> Orden: {self.order} </li>" 
                                    f"<li> Tipo: {self.type} </li>" 
                                    f"<li> Grado de homogeneidad: {self.degree}</li>"
                                "</ul>")
        details_label.setStyleSheet("color: black; font-size: 24px;")

        # Solución
        title_solution = QLabel(f"Resultado de la ecuación por {method}")
        title_solution.setStyleSheet("color: black; font-size: 24px;")
        
        solution_scroll_area = QScrollArea()
        #solution_scroll_area.setWidgetResizable(True)
        solution_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        solution_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # print(self.solution)
        solution_label = QLabel(f"{self.solution}")
        solution_label.setStyleSheet("color: #444444; font-size: 16px; background-color: #FFFFFF; padding: 10px;")
        solution_label.setAlignment(Qt.AlignTop)
        solution_label.setMinimumWidth(760)
        #solution_label.setWordWrap(True)
        font = solution_label.font()
        font.setFamily("Consolas")
        solution_label.setFont(font)
        solution_scroll_area.setWidget(solution_label)
        solution_scroll_area.setFixedHeight(200)
        solution_scroll_area.setContentsMargins(0, 0, 0, 0)
        solution_scroll_area.setStyleSheet(
            "QScrollBar:horizontal {"
            "    height: 10px;"
            "    background-color: #F0F0F0;"
            "}"
            "QScrollBar::handle:horizontal {"
            "    background-color: #CCCCCC;"
            "}"
            "QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {"
            "    width: 0px;"
            "}"
            "QScrollBar:vertical {"
            "    width: 10px;"
            "    background-color: #F0F0F0;"
            "}"
            "QScrollBar::handle:vertical {"
            "    background-color: #CCCCCC;"
            "}"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {"
            "    height: 0px;"
            "}"
            "QScrollArea {"
            "    padding: 0;"
            "    border: 0;"
            "}"
        )
        # Obtener el tamaño preferido de solution_label
        # Ajustar el ancho de solution_scroll_area
        solution_scroll_area.setFixedWidth(770)

        # Botón Regresar
        back_button = QPushButton("Regresar")
        back_button.setStyleSheet("background-color: #00BD9D; color: white; font-size: 24px; font-weight: bold;")

        # Conexión del botón Regresar
        back_button.clicked.connect(self.show_home_view)

        # Agregar widgets al diseño
        layout.addWidget(title_label)
        layout.addWidget(equation_label)
        layout.addWidget(details_label)
        layout.addWidget(title_solution)
        layout.addWidget(solution_scroll_area)
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
        title_label.setStyleSheet("color: #BF1363; font-size: 32px; font-weight: bold;")
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title_label)

        # Mensaje de error
        credits_label = QLabel(f" {msg}")
        layout.addWidget(credits_label, alignment=QtCore.Qt.AlignCenter)
        
        # Botón de regresar
        back_button = QPushButton("Regresar")
        back_button.setStyleSheet("background-color: #00BD9D; color: white; font-size: 24px; font-weight: bold;")
        layout.addWidget(back_button)
        back_button.clicked.connect(self.show_home_view)
        error_view.setLayout(layout)
        self.stacked_widget.addWidget(error_view)

        # Mostrar la vista de créditos
        self.stacked_widget.setCurrentWidget(error_view)


    ##############
    #   Lógica   #
    ##############

    def resolver_ed_homogenea_laplace(self, ecuacion):
        s, t = symbols('s t')
        y = Function('y')(t)
        # Aplicar la transformada de Laplace a ambos lados de la ecuación
        transformada_ecuacion = apart(LaplaceTransform(ecuacion.lhs, t, s).doit() - LaplaceTransform(ecuacion.rhs, t, s).doit(), s)

        # Resolver la ecuación transformada
        solucion_transformada = y * transformada_ecuacion


        # Mostrar el resumen paso a paso
        resumen = "Paso a paso de la solución:\n"
        resumen += "---------------------------\n"
        resumen += "1. Aplicar la transformada de Laplace a ambos lados de la ecuación:\n\n"
        resumen += pretty(transformada_ecuacion, use_unicode=True, wrap_line=False) + "\n\n\n"
        resumen += "2. Resolver la ecuación transformada:\n\n"
        resumen += pretty(solucion_transformada, use_unicode=True, wrap_line=False)

        return resumen

    def resolver_ed_homogenea_serie_potencias(self, ecuacion, orden):

        x = symbols('x')
        y = Function('y')(x)

        #ecuacion = eval(eq)
        
        # Expresar la ecuación diferencial en términos de la serie de potencias
        ecuacion_series = collect(ecuacion.subs(y, sum(x**n/factorial(n) for n in range(orden + 1))), x)

        # Obtener las ecuaciones para cada término de la serie
        ecuaciones_individuales = ecuacion_series.as_ordered_terms()

        # Resolver cada ecuación individual
        soluciones_individuales = []
        for i, ecuacion_individual in enumerate(ecuaciones_individuales):
            solucion_individual = ecuacion_individual / x**i
            soluciones_individuales.append(solucion_individual)

        # Construir la solución general a partir de las soluciones individuales
        solucion_general = sum(soluciones_individuales)

        # Mostrar el resumen paso a paso
        resumen = "Paso a paso de la solución:\n"
        resumen += "---------------------------\n"
        resumen += "1. Expresar la ecuación diferencial en términos de la serie de potencias:\n"
        resumen += pretty(ecuacion_series, use_unicode=True, wrap_line=False) + "\n"
        resumen += "2. Obtener las ecuaciones para cada término de la serie:\n\n"
        for i, ecuacion_individual in enumerate(ecuaciones_individuales):
            resumen += "Término " + str(i + 1) + ": \n"
            resumen += pretty(ecuacion_individual, use_unicode=True, wrap_line=False) + "\n\n"
            resumen += "Solución: \n" 
            resumen += pretty(soluciones_individuales[i]) + "\n\n"
        resumen += "---------------------------\n"
        resumen += "Solución general:\n"
        resumen += pretty(solucion_general, use_unicode=True, wrap_line=False)

        return resumen

    def resolver_ed_homogenea_sustitucion(self, ecuacion):
        x = symbols('x')
        y = Function('y')(x)

        #ecuacion = eval(eq)
        
        # Expresar la ecuación en forma normalizada
        y_new = Function('y_new')(x)
        ecuacion_normalizada = ecuacion.subs(y.diff(x), y_new)

        # Resolver la ecuación normalizada
        solucion = dsolve(ecuacion_normalizada)
        
        # Realizar la sustitución inversa y = exp(mx)
        m = symbols('m')
        sustitucion_inversa = solucion.subs(y_new, Function('C')(x) * pow(Function('E')(x), m*x))
        solucion_final = sustitucion_inversa.subs(Function('C')(x), y)
        
        # Mostrar el resumen paso a paso
        #return f'1. Expresar la ecuación en forma normalizada:<br>{ecuacion_normalizada}<br><br>2. Resolver la ecuación normalizada:<br>{solucion}<br><br>3. Realizar la sustitución inversa y = exp(mx):<br>{sustitucion_inversa}<br><br>Solución general:<br>{solucion_final}'
        # Construir el resumen paso a paso como cadena de texto
        resumen = "Paso a paso de la solución:\n"
        resumen += "---------------------------\n"
        resumen += "1. Expresar la ecuación en forma normalizada:\n"
        resumen += pretty(ecuacion_normalizada, use_unicode=True, wrap_line=False) + "\n\n"
        resumen += "2. Resolver la ecuación normalizada:\n"
        resumen += pretty(solucion, use_unicode=True, wrap_line=False) + "\n\n"
        resumen += "3. Realizar la sustitución inversa y = exp(mx):\n"
        resumen += pretty(sustitucion_inversa, use_unicode=True, wrap_line=False) + "\n\n"
        resumen += "---------------------------\n"
        resumen += "Solución general:\n"
        resumen += pretty(solucion_final, use_unicode=True, wrap_line=False) + "\n"

        return resumen

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

    def detect_homogeneity_degree(self, eq):
        x, y = symbols('x y')
        ecuacion = eval(eq)
        variables = ecuacion.free_symbols
        grados = []
        
        for variable in variables:
            grados_variable = set()
            
            for term in ecuacion.args:
                if variable in term.free_symbols:
                    grados_variable.add(term.as_poly(variable).degree())
            
            if grados_variable:
                grados.append(max(grados_variable))
        
        if grados:
            return max(grados)
        else:
            return 0  # Si no se encontraron variables con grados definidos, asumimos grado 0

    def solve_homogeneous_equation(self, eq, method):
        x = symbols('x')
        y = Function('y')(x)
        eq = eval(eq)

        if method == 'sustitución de variables':
            solution = self.resolver_ed_homogenea_sustitucion(eq)
        elif method == 'serie de potencias':
            solution = self.resolver_ed_homogenea_serie_potencias(eq, self.order)
        elif method == 'transformada de Laplace':
            solution = self.resolver_ed_homogenea_laplace(Eq(eq, 0))
        else:
            solution = "No se encontró una solución para el método seleccionado"
                
        return solution
    
    def standar_eq(self,equation):
        pattern = r'd\*\*(\d+)\s*y\s*/\s*dx\*\*(\1+)\s*|dy/dx'
        def replace(match):
            if match.group(0) == 'dy/dx':
                return "y'"
            else:
                num_derivatives = int(match.group(1))
                return "y" + "'" * num_derivatives
        # Reemplazar la notación de derivadas en la ecuación
        equation = re.sub(pattern, replace, equation)
        # print(equation)
        return equation

    def parse_equation(self, human_equation):
        x = symbols('x')
        y = symbols('y', cls=Function)(x)

        human_equation = re.sub(r"'+", lambda x: ".diff(x" + ", x" * (len(x.group()) - 1) + ")", human_equation)
        human_equation = re.sub(r'e\*\*x|e\^x', 'exp(x)', human_equation)
        human_equation = re.sub(r'([xy])(\d+)', r'\1*\2', human_equation)
        human_equation = re.sub(r'(\d+)([xy])', r'\1*\2', human_equation)
        human_equation = re.sub(r'([xy])\'', r'\1.diff(x)', human_equation)
        human_equation = re.sub(r'([xy])([xy])', r'\1*\2', human_equation)
        human_equation = human_equation.replace("–", "-")
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

    def getEqSimbol(self, eq):
        x = symbols('x')
        y = symbols('y', cls=Function)(x)
        eq = eval(eq)
        return eq
    
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
        self.degree = "No aplica"
        if eq:
            if self.is_differential(eq):
                self.eq_contex = "Sí es una ecuación diferencial."
                self.order = self.detect_order(self.eq)
                self.type = self.is_homogeneous()
                if self.type == "homogénea":
                    self.degree = self.detect_homogeneity_degree(eq)
                    if self.order > 3:
                        self.order = f"{self.order}, no se pueden resolver ecuaciones de orden mayor a 3."
                    else:
                        self.solution = self.solve_homogeneous_equation(eq, method)
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