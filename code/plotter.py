import re

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide2.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PySide2.QtGui import QDoubleValidator
import configuration as config


class FunctionPlotter(QMainWindow):
    def __init__(self):
        super(FunctionPlotter, self).__init__()
        self.setWindowTitle(config.WINDOW_TITLE)
        self.setGeometry(config.WINDOW_X, config.WINDOW_Y,
                         config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
        self.setup_ui()

    def setup_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.func_label = QLabel("Enter a function of x :")
        self.func_input = QLineEdit()

        self.range_label = QLabel("Enter the min and max values of x:")
        self.x_min_input = QLineEdit()
        self.x_min_input.setValidator(QDoubleValidator())
        self.x_min_input.setPlaceholderText("Minimum value of x")
        self.x_max_input = QLineEdit()
        self.x_max_input.setValidator(QDoubleValidator())
        self.x_max_input.setPlaceholderText("Maximum value of x")

        self.plot_button = QPushButton("Plot",)
        self.plot_button.clicked.connect(self.plot_function)

        self.layout.addWidget(self.func_label)
        self.layout.addWidget(self.func_input)
        self.layout.addWidget(self.range_label)
        self.layout.addWidget(self.x_min_input)
        self.layout.addWidget(self.x_max_input)
        self.layout.addWidget(self.plot_button)

        # Create a Figure and a Canvas for plotting
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

    def validate_input(self, func_str, x_min, x_max):
        if not func_str:
            return False, "Please enter a function."

        try:
            x = np.linspace(float(x_min), float(x_max), config.SAMPLING_FREQ)
            func_str = re.sub(r'\bx\b', '(x)', func_str)
            func_str = re.sub(r'\^', '**', func_str)
            y = eval(func_str)
        except SyntaxError as e:
            return False, f"Invalid function: {e}"
        except ValueError as e:
            return False, "Please enter both minimum and maximum values of x."
        except Exception as e:
            return False, f"Function evaluation error: {e}"

        if x_min >= x_max:
            return False, "Invalid x range: Minimum value must be less than maximum value."

        return True, x, y

    def plot_function(self):
        func_str = self.func_input.text()
        is_valid, x, y = self.validate_input(
            func_str, self.x_min_input.text(), self.x_max_input.text())

        if not is_valid:
            self.show_error_message(x)
            return

        # Clear the previous plot and plot the new one
        self.figure.clear()
        plt.plot(x, y)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(f"Plot of: y = {func_str}")

        # Refresh the canvas to update the plot
        self.canvas.draw()

    def show_error_message(self, msg):
        error_msg_box = QMessageBox()
        error_msg_box.setIcon(QMessageBox.Critical)
        error_msg_box.setWindowTitle("Error")
        error_msg_box.setText(msg)
        error_msg_box.exec_()
