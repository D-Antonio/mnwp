from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout, QWidget, QLabel, QLineEdit, QVBoxLayout, QComboBox, QStackedWidget
from PyQt5.QtGui import QColor
from PyQt5 import QtCore
import webbrowser

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JEdyCalc")
        self.setStyleSheet("background-color: #FFFBFA;")
        self.layout = QVBoxLayout()

        # Botones superiores
        buttons_layout = QHBoxLayout()
        self.info_button = QPushButton("Información")
        self.info_button.setStyleSheet("background-color: #00BD9D; color: white;")
        self.tutorial_button = QPushButton("Tutorial")
        self.tutorial_button.setStyleSheet("background-color: #00BD9D; color: white;")
        self.credits_button = QPushButton("Créditos")
        self.credits_button.setStyleSheet("background-color: #00BD9D; color: white;")

        buttons_layout.addWidget(self.credits_button)
        buttons_layout.addWidget(self.tutorial_button)
        buttons_layout.addWidget(self.info_button)

        self.layout.addLayout(buttons_layout)

        # Título
        self.title_label = QLabel("JEdyCalc")
        self.title_label.setStyleSheet("color: #BF1363; font-size: 24px; font-weight: bold;")
        self.layout.addWidget(self.title_label, alignment=QtCore.Qt.AlignCenter)

        # Input
        self.input_line_edit = QLineEdit()
        self.input_line_edit.setStyleSheet("background-color: white; border: 1px solid #ccc; padding: 5px; box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.1);")
        #self.input_line_edit.setStyleSheet("QLineEdit { background-color: white; border: 1px solid #ccc; padding: 5px; box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.1); }")
        self.layout.addWidget(self.input_line_edit)

        # Selector
        self.selector_combobox = QComboBox()
        self.selector_combobox.addItem("Metodo 1")
        self.selector_combobox.addItem("Metodo 2")
        self.selector_combobox.addItem("Metodo 3")
        #self.selector_combobox.setStyleSheet("QComboBox { background-color: white; border: 1px solid #ccc; padding: 5px; selection-background-color: #00BD9D; } QComboBox::drop-down { border: none; } QComboBox QAbstractItemView { border: 1px solid #ccc; } QComboBox::down-arrow { image: url(down_arrow.png); }")
        self.selector_combobox.setStyleSheet("background-color: white;color: black; border: 1px solid #ccc; box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.1); padding: 5px; selection-background-color: #00BD9D;")
        self.selector_combobox.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.selector_combobox.view().setStyleSheet("color: black;")
        self.layout.addWidget(self.selector_combobox, alignment=QtCore.Qt.AlignCenter)

        # Botón Resolver
        self.solve_button = QPushButton("Resolver")
        self.solve_button.setStyleSheet("background-color: #00BD9D; color: white;")
        self.layout.addWidget(self.solve_button, alignment=QtCore.Qt.AlignCenter)

        self.setLayout(self.layout)

        # Conexiones de los botones
        self.info_button.clicked.connect(self.show_info_view)
        self.tutorial_button.clicked.connect(self.show_tutorial_view)
        self.credits_button.clicked.connect(self.show_credits_view)
        self.solve_button.clicked.connect(self.solve)
        
        # Crear el stack de vistas
        #self.stacked_widget = QStackedWidget()
        #self.layout.addWidget(self.stacked_widget)

        # Agregar la vista __init__ al stack
        #self.stacked_widget.addWidget(self)

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
        back_button.clicked.connect(self.show_initial_view)

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
        back_button.clicked.connect(self.show_initial_view)

        credits_view.setLayout(layout)
        self.stacked_widget.addWidget(credits_view)

        # Mostrar la vista de créditos
        self.stacked_widget.setCurrentWidget(credits_view)

    def show_initial_view(self):
        # Mostrar la vista __init__
        self.stacked_widget.setCurrentWidget(self)

    def solve(self):
        # Lógica para resolver el problema con el método seleccionado
        method = self.selector_combobox.currentText()
        text = self.input_line_edit.text()
        # Realizar la operación correspondiente

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()