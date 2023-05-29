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
        self.selector_combobox.addItem("sustitución de variables")
        self.selector_combobox.addItem("transformada de Laplace")
        self.selector_combobox.addItem("serie de potencias")
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
        solve_button.clicked.connect(self.show_solution_view)

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

    def is_differential(self, e):
        return False
    
    def detect_order(self, e):
        return 4
    
    def is_homogeneous(self,e):
        return False
    
    def detect_homogeneity_degree(self):
        return 4
    
    def solve_homogeneous_equation(self, e, m):
        return "result"

    def solve(self):
        # Lógica para resolver el problema con el método seleccionado
        method = self.selector_combobox.currentText()  # sustitución de variables, transformada de Laplace, serie de potencias
        text = self.input_line_edit.text()
        
        # Realizar la operación correspondiente
        if self.is_differential(text):
            # Si la ecuación es diferencial:
            # Detectar el tipo de orden de la ecuación
            order = self.detect_order(text)
            
            if order > 3:
                # Si el tipo de orden es mayor a 3:
                # Mostrar mensaje de error indicando que el programa no puede resolver ecuaciones de orden mayor a 3
                print("Error: No se pueden resolver ecuaciones de orden mayor a 3.")
            else:
                # Sino:
                # Detectar si la ecuación es homogénea o heterogénea
                if self.is_homogeneous(text):
                    # Si la ecuación es homogénea:
                    # Detectar el grado de homogeneidad
                    degree = self.detect_homogeneity_degree(text)
                    # Resolver la ecuación homogénea según el método seleccionado
                    solution = self.solve_homogeneous_equation(text, method)
                    # Mostrar la solución obtenida
                    
                else:
                    # Sino:
                    # Mostrar mensaje de error indicando que el programa no puede resolver ecuaciones heterogéneas
                    print("Error: No se pueden resolver ecuaciones heterogéneas.")
        else:
            # Sino:
            # Mostrar mensaje de error indicando que la ecuación no es diferencial
            print("Error: La ecuación no es diferencial.")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()