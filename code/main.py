import sys
from PySide2.QtWidgets import QApplication
from plotter import FunctionPlotter

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FunctionPlotter()
    window.show()
    sys.exit(app.exec_())
