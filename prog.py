from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
                              QHBoxLayout, QMessageBox, QRadioButton)
from PyQt6.QtCore import Qt, QTimer

app = QApplication([])
win = QWidget()

win.setWindowTitle("Program")

win.resize(600, 400)

question = QLabel("Як звали першого ютуб-блогера, який набрав 100000000 підписників?")

answer_1 = QRadioButton("PewDiePie")
answer_2 = QRadioButton("Рет і Лінк")
answer_3 = QRadioButton("SlivkiShow")
answer_4 = QRadioButton("TheBrianMaps")
answer_5 = QRadioButton("Mister Max")
answer_6 = QRadioButton("EeOneGuy")



main_layout = QVBoxLayout()

main_layout.addWidget(question, alignment = Qt.AlignmentFlag.AlignCenter)

h_line_1 = QHBoxLayout()
h_line_2 = QHBoxLayout()
h_line_3 = QHBoxLayout()

h_line_1.addWidget(answer_1, alignment = Qt.AlignmentFlag.AlignCenter)
h_line_1.addWidget(answer_2, alignment = Qt.AlignmentFlag.AlignCenter)
h_line_2.addWidget(answer_3, alignment = Qt.AlignmentFlag.AlignCenter)
h_line_2.addWidget(answer_4, alignment = Qt.AlignmentFlag.AlignCenter)
h_line_3.addWidget(answer_5, alignment = Qt.AlignmentFlag.AlignCenter)
h_line_3.addWidget(answer_6, alignment = Qt.AlignmentFlag.AlignCenter)

main_layout.addLayout(h_line_1)
main_layout.addLayout(h_line_2)
main_layout.addLayout(h_line_3)

def show_winer():
    message_box = QMessageBox()
    message_box.setText("Ви виграли зустріч з творцями каналу!")
    message_box.exec()
    QTimer.singleShot(3000, app.quit)

def show_lose():
    message_box = QMessageBox()
    message_box.setText("Пощастить іншим разом!")
    message_box.exec()
    QTimer.singleShot(3000, app.quit)

answer_1.clicked.connect(show_winer)
answer_2.clicked.connect(show_lose)
answer_3.clicked.connect(show_lose)
answer_4.clicked.connect(show_lose)
answer_5.clicked.connect(show_lose)
answer_6.clicked.connect(show_lose)

win.setLayout(main_layout)

win.show()
app.exec()