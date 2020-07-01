import sys

from functools import partial
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QHBoxLayout,
                             QVBoxLayout,
                             QGridLayout,
                             QMainWindow,
                             QPushButton,
                             QLineEdit,
                             QLabel,
                             QSizePolicy)


class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Calculator')
        self.setFixedSize(500, 200)
        widget = QWidget()
        self.display = QLineEdit('')
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.display)
        buttonLayout = QGridLayout()
        buttons = [
            {
                'name': '←',
                'row': 0,
                'col': 0
            },
            {
                'name': 'C',
                'row': 0,
                'col': 1
            },
            {
                'name': 'ꭓ2',
                'row': 0,
                'col': 2
            },
            {
                'name': '±',
                'row': 0,
                'col': 3
            },
            {
                'name': '√',
                'row': 0,
                'col': 4
            },
            {
                'name': '7',
                'row': 1,
                'col': 0
            },
            {
                'name': '8',
                'row': 1,
                'col': 1
            },
            {
                'name': '9',
                'row': 1,
                'col': 2
            },
            {
                'name': '/',
                'row': 1,
                'col': 3
            },
            {
                'name': '%',
                'row': 1,
                'col': 4,
            },
            {
                'name': '4',
                'row': 2,
                'col': 0,
            },
            {
                'name': '5',
                'row': 2,
                'col': 1,
            },
            {
                'name': '6',
                'row': 2,
                'col': 2,
            },
            {
                'name': '×',
                'row': 2,
                'col': 3,
            },
            {
                'name': '1/ꭓ',
                'row': 2,
                'col': 4,
            },
            {
                'name': '1',
                'row': 3,
                'col': 0,
            },
            {
                'name': '2',
                'row': 3,
                'col': 1,
            },
            {
                'name': '3',
                'row': 3,
                'col': 2,
            },
            {
                'name': '—',
                'row': 3,
                'col': 3,
            },
            {
                'name': '=',
                'row': 3,
                'col': 4,
                'rowSpan': 2
            },
            {
                'name': '0',
                'row': 4,
                'col': 0,
                'colSpan': 2,
            },
            {
                'name': '.',
                'row': 4,
                'col': 2,
            },
            {
                'name': '+',
                'row': 4,
                'col': 3,
            }
        ]
        self.buttons = {}
        for buttonConfig in buttons:
            name = buttonConfig.get('name', '')
            btn = QPushButton(name)
            self.buttons[name] = btn
            font = QFont()
            font.setBold(True)
            btn.setFont(font)
            #btn.setFlat(True)
            btn.setSizePolicy(QSizePolicy.Preferred,
                              QSizePolicy.Expanding)
            buttonLayout.addWidget(btn,
                                    buttonConfig['row'],
                                    buttonConfig['col'],
                                    buttonConfig.get('rowSpan', 1),
                                    buttonConfig.get('colSpan', 1))
            mainLayout.addLayout(buttonLayout)
            widget.setLayout(mainLayout)
            self.setCentralWidget(widget)

        for buttonName in self.buttons:
            btn = self.buttons[buttonName]
            if buttonName == '=':
                btn.clicked.connect(self.end)
            elif buttonName == 'C':
                btn.clicked.connect(self.end)
            else:
                btn.clicked.connect(partial(self.change_text, buttonName))
                if buttonName == '+':
                    history = self.display.text()
                    btn.clicked.connect(self.clear_display)
                    btn.clicked.connect(self.set_history)


    def set_history(self):
        self.display.setText(history)

    def clear_display(self):
        self.display.setText('')

    def change_text(self, text):
        self.display.setText(self.display.text() + text)

    def point(self):
        if '.' not in self.display.text():
            return self.display.setText(self.display.text() + '.')


    def calc_result(self):
        self.display.setText(self.display.text())

    #def addition(self):



    def sys_error(self):
        return 'Error'


    def end(self):
        self.display.setText('')





def main_window():
    app = QApplication(sys.argv)
    window = MyWindow()
    #view = calc_display()
    window.show()
    #graph_calc_control(view=view)
    return_code = app.exec()
    sys.exit(return_code)

if __name__ == '__main__':
    main_window()