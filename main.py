from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from mainPage import CalendarListApp


app = QApplication([])
window = CalendarListApp()
title = "Calendar List App"
window.setWindowTitle(title)
window.setWindowIcon(QIcon("vectors/calendarVector.png"))
window.show()
app.exec_()