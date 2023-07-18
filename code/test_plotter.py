import pytest
import sys
from PySide2.QtWidgets import QApplication
# Replace 'your_module_name' with the actual name of the module
from plotter import FunctionPlotter


@pytest.fixture(scope="module")
def app(request):
    qapp = QApplication.instance()
    if qapp is None:
        qapp = QApplication(sys.argv)

    def teardown():
        if qapp is not None and not QApplication.instance():
            qapp.quit()

    request.addfinalizer(teardown)
    return qapp


@pytest.fixture
def function_plotter(qtbot, app):
    widget = FunctionPlotter()
    qtbot.addWidget(widget)
    return widget, qtbot  # Return the widget and the qtbot


def test_validate_input_invalid_function(function_plotter):
    widget, qtbot = function_plotter  # Unpack the tuple
    # Test invalid function input
    func_str = "x**2 +"
    x_min = "0"
    x_max = "5"
    is_valid, _, _ = widget.validate_input(func_str, x_min, x_max)

    assert not is_valid


def test_validate_input_invalid_x_range(function_plotter):
    widget, qtbot = function_plotter

    # Test invalid x range (min > max)
    func_str = "-x"
    x_min = "5"
    x_max = "0"
    is_valid, _, _ = widget.validate_input(func_str, x_min, x_max)

    assert not is_valid


def test_validate_input_missing_values(function_plotter):
    widget, qtbot = function_plotter

    # Test missing x_min and x_max values
    func_str = "x+2"
    x_min = ""
    x_max = ""
    is_valid, _, _ = widget.validate_input(func_str, x_min, x_max)

    assert not is_valid


def test_validate_input_valid_input(function_plotter):
    widget, qtbot = function_plotter

    # Test valid input
    func_str = "x^2"
    x_min = "-10"
    x_max = "10"
    is_valid, _, _ = widget.validate_input(func_str, x_min, x_max)

    assert is_valid


def test_plot_function_valid_input(function_plotter):
    widget, qtbot = function_plotter

    # Test plotting with valid input
    func_str = "x**2"
    x_min = "0"
    x_max = "5"
    widget.func_input.setText(func_str)
    widget.x_min_input.setText(x_min)
    widget.x_max_input.setText(x_max)

    widget.plot_function()

    # Check if the plot was updated successfully
    assert widget.figure.get_axes()
    assert widget.canvas


def test_validate_input_invalid_syntax(function_plotter):
    widget, qtbot = function_plotter

    # Test invalid function input (invalid syntax)
    func_str = "x**2 + x)"
    x_min = "0"
    x_max = "5"
    is_valid, _, _ = widget.validate_input(func_str, x_min, x_max)

    assert not is_valid


def test_validate_input_invalid_value_error(function_plotter):
    widget, qtbot = function_plotter

    # Test invalid function input (invalid value error)
    func_str = "sqrt(x)"
    x_min = "-5"
    x_max = "5"
    is_valid, _, _ = widget.validate_input(func_str, x_min, x_max)

    assert not is_valid


def test_validate_input_valid_negative_values(function_plotter):
    widget, qtbot = function_plotter

    # Test valid input with negative values
    func_str = "x**3 - 2*x + 3"
    x_min = "-5"
    x_max = "5"
    is_valid, _, _ = widget.validate_input(func_str, x_min, x_max)

    assert is_valid


def test_plot_function_valid_plot(function_plotter):
    widget, qtbot = function_plotter

    # Test plotting with valid input and valid function
    func_str = "x**3"
    x_min = "-2"
    x_max = "2"
    widget.func_input.setText(func_str)
    widget.x_min_input.setText(x_min)
    widget.x_max_input.setText(x_max)

    widget.plot_function()

    # Check if the plot was updated successfully
    assert widget.figure.get_axes()
    assert widget.canvas


def test_plot_function_no_function_input(function_plotter):
    widget, qtbot = function_plotter

    # Test plotting without entering a function
    func_str = ""
    x_min = "-2"
    x_max = "2"
    widget.func_input.setText(func_str)
    widget.x_min_input.setText(x_min)
    widget.x_max_input.setText(x_max)

    is_valid, _, _ = widget.validate_input(func_str, x_min, x_max)

    assert not is_valid


def test_plot_function_invalid_range(function_plotter):
    widget, qtbot = function_plotter

    # Test plotting with invalid x range (min >= max)
    func_str = "x-1"
    x_min = "5"
    x_max = "5"
    widget.func_input.setText(func_str)
    widget.x_min_input.setText(x_min)
    widget.x_max_input.setText(x_max)

    is_valid, _, _ = widget.validate_input(func_str, x_min, x_max)

    assert not is_valid


if __name__ == "__main__":
    pytest.main()
