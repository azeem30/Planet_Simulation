from PyQt5 import QtCore, QtGui, QtWidgets
import random


with open("facts.txt", "r") as fact_file:
    string_fact = ""
    all_facts = fact_file.readlines()
    selected_facts = random.sample(all_facts, 5)
    for fact in selected_facts:
        string_f = selected_facts[selected_facts.index(fact)]
        string_fact += string_f

class Ui_facts_window(object):
    def setupUi(self, facts_window):
        facts_window.setObjectName("facts_window")
        facts_window.resize(624, 288)
        facts_window.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.facts_label = QtWidgets.QLabel(facts_window)
        self.facts_label.setGeometry(QtCore.QRect(20, 20, 581, 241))
        self.facts_label.setStyleSheet("color: rgb(255, 255, 255);")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.facts_label.setFont(font)
        self.facts_label.setText(string_fact)
        self.facts_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.facts_label.setWordWrap(True)
        self.facts_label.setObjectName("facts_label")

        self.retranslateUi(facts_window)
        QtCore.QMetaObject.connectSlotsByName(facts_window)

    def retranslateUi(self, facts_window):
        _translate = QtCore.QCoreApplication.translate
        facts_window.setWindowTitle(_translate("facts_window", "Facts"))
        facts_logo_map = QtGui.QPixmap("facts_logo.png")
        facts_logo = QtGui.QIcon(facts_logo_map)
        facts_window.setWindowIcon(facts_logo)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    facts_window = QtWidgets.QWidget()
    ui = Ui_facts_window()
    ui.setupUi(facts_window)
    facts_window.show()
    sys.exit(app.exec_())
