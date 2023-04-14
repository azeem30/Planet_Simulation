import datetime
import testgui
from PyQt5 import QtCore, QtGui, QtWidgets
total_days = 0
string_date_input = ""

class Ui_calendar_window(object):
    def setupUi(self, calendar_window):
        calendar_window.setObjectName("calendar_window")
        calendar_window.resize(389, 275)
        calendar_window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.calendar = QtWidgets.QCalendarWidget(calendar_window)
        self.calendar.setGeometry(QtCore.QRect(0, 0, 391, 241))
        self.calendar.setMaximumSize(QtCore.QSize(16777200, 16777200))
        self.calendar.setStyleSheet("color: rgb(0, 0, 0);\n""background-color: rgb(255, 255, 255);")
        self.calendar.setObjectName("calendar")
        #self.calendar.selectionChanged.connect(self.grab_date)
        self.ok = QtWidgets.QPushButton(calendar_window, clicked=self.grab_date)
        self.ok.setObjectName("ok")
        self.ok.setGeometry(QtCore.QRect(355, 243, 31, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ok.setFont(font)
        self.ok.setStyleSheet("background-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")
        self.retranslateUi(calendar_window)
        QtCore.QMetaObject.connectSlotsByName(calendar_window)

    def retranslateUi(self, calendar_window):
        _translate = QtCore.QCoreApplication.translate
        calendar_window.setWindowTitle(_translate("calendar_window", "Calendar"))
        self.ok.setText(_translate("calendar_window", "OK"))

    def grab_date(self):
        try:
            global string_date_input
            global total_days
            # taking the input date
            date_input = self.calendar.selectedDate()
            string_date_input = str(date_input.toPyDate())

            # calculating number of days between current date and entered date
            now = datetime.date.today()
            then = date_input.toPyDate()
            total_days = (then - now).days

            if total_days > 0:
                pass
            else:
                total_days = (now - then).days

            self.open_again()
        except Exception as e:
            print(e)

    def open_again(self):
        self.home_window = QtWidgets.QWidget()
        self.home_ui = testgui.Ui_main_window()
        self.home_ui.setupUi(self.home_window)
        self.home_window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calendar_window = QtWidgets.QWidget()
    ui_calendar = Ui_calendar_window()
    ui_calendar.setupUi(calendar_window)
    calendar_window.show()
    sys.exit(app.exec_())
