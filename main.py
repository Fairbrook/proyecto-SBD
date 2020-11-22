if __name__ == "__main__":
    import sys
    from PySide2.QtWidgets import QApplication
    from controllers.main import MainWindow

    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
