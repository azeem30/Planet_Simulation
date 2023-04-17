import calendargui
from PyQt5.QtCore import QTimer, QTime
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main_window(object):
    def show_time(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString("hh:mm:ss")
        self.real_time.setText(label_time)

    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(777, 360)
        main_window.setStyleSheet("")
        self.img = QtWidgets.QLabel(main_window)
        self.img.setGeometry(QtCore.QRect(0, 0, 781, 381))
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap("space.jpg"))
        self.img.setScaledContents(True)
        self.img.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.img.setObjectName("img")
        self.timer = QTimer()
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)
        self.year_label = QtWidgets.QLabel(main_window)
        self.year_label.setGeometry(QtCore.QRect(260, 315, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.year_label.setFont(font)
        self.year_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.year_label.setAlignment(QtCore.Qt.AlignCenter)
        self.year_label.setObjectName("year_label")
        self.calc = QtWidgets.QPushButton(main_window, clicked=self.calculate)
        self.calc.setGeometry(QtCore.QRect(490, 310, 81, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calc.setFont(font)
        self.calc.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.calc.setObjectName("calc")
        self.real_time = QtWidgets.QLabel(main_window)
        self.real_time.setGeometry(QtCore.QRect(350, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.real_time.setFont(font)
        self.real_time.setStyleSheet("color: rgb(255, 255, 255);")
        self.real_time.setAlignment(QtCore.Qt.AlignCenter)
        self.real_time.setObjectName("real_time")
        self.open_calendar = QtWidgets.QPushButton(main_window, clicked=self.go_calendar)
        self.open_calendar.setGeometry(QtCore.QRect(450, 310, 31, 28))
        self.open_calendar.setStyleSheet("image: url(cal_logo.png);")
        self.open_calendar.setText("")
        self.open_calendar.setObjectName("open_calendar")
        self.year_input = QtWidgets.QLabel(main_window)
        self.year_input.setGeometry(QtCore.QRect(310, 310, 171, 31))
        self.year_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.year_input.setText(calendargui.string_date_input)
        self.year_input.setObjectName("year_input")
        self.year_input.setIndent(5)
        self.year_input.setEnabled(False)
        input_font = QtGui.QFont()
        input_font.setFamily("Arial")
        input_font.setPointSize(10)
        input_font.setBold(True)
        input_font.setWeight(75)
        self.year_input.setFont(input_font)
        self.img.raise_()
        self.year_label.raise_()
        self.calc.raise_()
        self.real_time.raise_()
        self.year_input.raise_()
        self.open_calendar.raise_()
        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Planet Position Prediction"))
        self.year_label.setText(_translate("main_window", "Year"))
        self.calc.setText(_translate("main_window", "Calculate"))

    def go_calendar(self):
        self.cal_window = QtWidgets.QWidget()
        self.cal_ui = calendargui.Ui_calendar_window()
        self.cal_ui.setupUi(self.cal_window)
        self.cal_window.show()

    def calculate(self):
        from Solarsystem import main as game
        home_total_days = calendargui.total_days
        game()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QWidget()
    ui_home = Ui_main_window()
    ui_home.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())

