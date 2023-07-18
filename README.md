# FunctionPlotter

FunctionPlotter is a simple PyQt-based GUI application that allows users to plot mathematical functions of x. It provides an interactive interface to input a function and the range of x values, and then plots the function on a graph.

## Features

- Enter a mathematical function of x and plot it.
- Specify the range of x values to be plotted.
- Handles basic mathematical functions using Python's `eval` function.
- GUI built with PySide2 (Qt for Python).

## Requirements

- Python 3.x
- PySide2 (Qt for Python)
- Matplotlib
- NumPy
## Installation

1. Clone the repository:


```terminal
git clone https://github.com/AbdelrahmanSalem9/FunctionPlotter.git
cd FunctionPlotter
```

2. Install the required packages using `pip`:
```terminal
pip install PySide2 numpy matplotlib
```
3. Run Program
```terminal
python code/main.py
```
The GUI window will appear, allowing you to input a function and x range, and then click the "Plot" button to visualize the function plot.

## Code Structure
The project's code structure is organized as follows:
code/: Contains the source code for the `FunctionPlotter` program.

- `main.py`: The Program starting point
- `plotter.py`: The main program file with the FunctionPlotter class.
configuration.py: Configuration file containing constants for the GUI.
- `test_plotter.py`: End-to-end tests for the FunctionPlotter program using pytest and pytest-qt.

## Automated Tests
The program includes automated tests for some of the main features using `pytest` and `pytest-qt`. These tests simulate user interactions and verify the expected behavior of the program. To run the tests, use the following command:
```terminal
python code/test_plotter.py
```

## Design
The FunctionPlotter program follows a simple design pattern using the Model-View-Controller (MVC) architecture:

- Model: The model is responsible for the mathematical calculations and data handling. In this case, it evaluates the user's input function using Python's `eval` function.

- View: The view represents the GUI components and handles user interactions. The GUI is implemented using `PySide2` (Qt for Python).

- Controller: The controller is the bridge between the model and the view. It handles the logic of the application, including user input `validation` and `plotting` the function.

## Test Cases

### Correct 
![Image Alt Text](test%20cases/correct/example1.png)
![Image Alt Text](test%20cases/correct/example2.png)
![Image Alt Text](test%20cases/correct/example3.png)
![Image Alt Text](test%20cases/correct/example4.png)

### Wrong
![Image Alt Text](test%20cases/wrong/Invalid%20function.png)
![Image Alt Text](test%20cases/wrong/Invalid%20range.png)
![Image Alt Text](test%20cases/wrong/Missing%20function.png)
![Image Alt Text](test%20cases/wrong/Missing%20min%20and%20max.png)
![Image Alt Text](test%20cases/wrong/Missing%20range.png)