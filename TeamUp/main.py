# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication

import Model.DataBase


if __name__ == "__main__":
    base=DataBase()
    f = base.connect()
    app = QApplication([])
    # ...

    sys.exit(app.exec_())


    print(mydb)
