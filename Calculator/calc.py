from PyQt5 import QtCore, QtGui, QtWidgets
import math

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(246, 245)
        MainWindow.setStyleSheet("background-color: rgb(35, 42, 57);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(0, 0, 400, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_result.setObjectName("label_result")

        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 122, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(23, 255, 110);")
        self.btn_1.setObjectName("btn_1")

        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(41, 122, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(23, 255, 110);")
        self.btn_2.setObjectName("btn_2")

        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(82, 122, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(23, 255, 110);")
        self.btn_3.setObjectName("btn_3")

        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(82, 81, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(23, 255, 110);")
        self.btn_6.setObjectName("btn_6")

        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(41, 81, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(23, 255, 110);")
        self.btn_5.setObjectName("btn_5")

        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 81, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(23, 255, 110);")
        self.btn_4.setObjectName("btn_4")

        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(82, 40, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(23, 255, 110);")
        self.btn_9.setObjectName("btn_9")

        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(41, 40, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(23, 255, 110);")
        self.btn_8.setObjectName("btn_8")

        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 40, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(23, 255, 110);")
        self.btn_7.setObjectName("btn_7")

        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(0, 163, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(23, 255, 110);")
        self.btn_0.setObjectName("btn_0")

        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(123, 40, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
        self.btn_plus.setObjectName("btn_plus")

        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(123, 81, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
        self.btn_minus.setObjectName("btn_minus")

        self.btn_multy = QtWidgets.QPushButton(self.centralwidget)
        self.btn_multy.setGeometry(QtCore.QRect(123, 122, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_multy.setFont(font)
        self.btn_multy.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
        self.btn_multy.setObjectName("btn_multy")

        self.btn_divid = QtWidgets.QPushButton(self.centralwidget)
        self.btn_divid.setGeometry(QtCore.QRect(123, 163, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_divid.setFont(font)
        self.btn_divid.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
        self.btn_divid.setObjectName("btn_divid")

        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(41, 163, 81, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
        self.btn_equal.setObjectName("btn_equal")

        self.btn_clean = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clean.setGeometry(QtCore.QRect(41, 204, 81, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_clean.setFont(font)
        self.btn_clean.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 0, 0);")
        self.btn_clean.setObjectName("btn_clean")

        self.btn_dot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dot.setGeometry(QtCore.QRect(0, 204, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_dot.setFont(font)
        self.btn_dot.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
        self.btn_dot.setObjectName("btn_dot")

        self.btn_degree = QtWidgets.QPushButton(self.centralwidget)
        self.btn_degree.setGeometry(QtCore.QRect(123, 204, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_degree.setFont(font)
        self.btn_degree.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
        self.btn_degree.setObjectName("btn_degree")

        self.btn_bracket1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bracket1.setGeometry(QtCore.QRect(164, 204, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_bracket1.setFont(font)
        self.btn_bracket1.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
        self.btn_bracket1.setObjectName("btn_bracket1")

        self.btn_bracket2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bracket2.setGeometry(QtCore.QRect(205, 204, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_bracket2.setFont(font)
        self.btn_bracket2.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
        self.btn_bracket2.setObjectName("btn_bracket2")

        self.btn_sin = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sin.setGeometry(QtCore.QRect(164, 40, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_sin.setFont(font)
        self.btn_sin.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
        self.btn_sin.setObjectName("btn_sin")

        self.btn_cos = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cos.setGeometry(QtCore.QRect(164, 81, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_cos.setFont(font)
        self.btn_cos.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
        self.btn_cos.setObjectName("btn_cos")

        self.btn_tg = QtWidgets.QPushButton(self.centralwidget)
        self.btn_tg.setGeometry(QtCore.QRect(164, 122, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_tg.setFont(font)
        self.btn_tg.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
        self.btn_tg.setObjectName("btn_tg")

        self.btn_asin = QtWidgets.QPushButton(self.centralwidget)
        self.btn_asin.setGeometry(QtCore.QRect(205, 40, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_asin.setFont(font)
        self.btn_asin.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
        self.btn_asin.setObjectName("btn_asin")

        self.btn_acos = QtWidgets.QPushButton(self.centralwidget)
        self.btn_acos.setGeometry(QtCore.QRect(205, 81, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_acos.setFont(font)
        self.btn_acos.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
        self.btn_acos.setObjectName("btn_acos")

        self.btn_atg = QtWidgets.QPushButton(self.centralwidget)
        self.btn_atg.setGeometry(QtCore.QRect(205, 122, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_atg.setFont(font)
        self.btn_atg.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
        self.btn_atg.setObjectName("btn_atg")

        self.btn_pi = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pi.setGeometry(QtCore.QRect(164, 163, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_pi.setFont(font)
        self.btn_pi.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
        self.btn_pi.setObjectName("btn_pi")

        self.btn_e = QtWidgets.QPushButton(self.centralwidget)
        self.btn_e.setGeometry(QtCore.QRect(205, 163, 40, 40))
        font = QtGui.QFont()
        font.setFamily(self.btn_font_style())
        font.setPointSize(self.btn_font_size())
        self.btn_e.setFont(font)
        self.btn_e.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
        self.btn_e.setObjectName("btn_e")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label_result.setText(_translate("MainWindow", "0"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_multy.setText(_translate("MainWindow", "*"))
        self.btn_divid.setText(_translate("MainWindow", "/"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_clean.setText(_translate("MainWindow", "C"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_degree.setText(_translate("MainWindow", "**"))
        self.btn_bracket1.setText(_translate("MainWindow", "("))
        self.btn_bracket2.setText(_translate("MainWindow", ")"))
        self.btn_sin.setText(_translate("MainWindow", "sin"))
        self.btn_cos.setText(_translate("MainWindow", "cos"))
        self.btn_tg.setText(_translate("MainWindow", "tg"))
        self.btn_asin.setText(_translate("MainWindow", "asin"))
        self.btn_acos.setText(_translate("MainWindow", "acos"))
        self.btn_atg.setText(_translate("MainWindow", "atg"))
        self.btn_pi.setText(_translate("MainWindow", "π"))
        self.btn_e.setText(_translate("MainWindow", "e"))
        #self.btn_square.setText(_translate("MainWindow", "x^2"))
        #self.btn_cube.setText(_translate("MainWindow", "x^3"))

    def add_functions(self):
        self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))
        self.btn_minus.clicked.connect(lambda: self.write_number(self.btn_minus.text()))
        self.btn_multy.clicked.connect(lambda: self.write_number(self.btn_multy.text()))
        self.btn_divid.clicked.connect(lambda: self.write_number(self.btn_divid.text()))
        self.btn_dot.clicked.connect(lambda: self.write_number(self.btn_dot.text()))
        self.btn_degree.clicked.connect(lambda: self.write_number(self.btn_degree.text()))
        self.btn_bracket1.clicked.connect(lambda: self.write_number(self.btn_bracket1.text()))
        self.btn_bracket2.clicked.connect(lambda: self.write_number(self.btn_bracket2.text()))
        self.btn_equal.clicked.connect(self.results)
        self.btn_clean.clicked.connect(self.clean_results)
        self.btn_pi.clicked.connect(self.num_pi)
        self.btn_e.clicked.connect(self.num_e)
        self.btn_sin.clicked.connect(self.btn_sinus)
        self.btn_cos.clicked.connect(self.btn_cosinus)
        self.btn_tg.clicked.connect(self.btn_tangens)
        self.btn_asin.clicked.connect(self.btn_asinus)
        self.btn_acos.clicked.connect(self.btn_acosinus)
        self.btn_atg.clicked.connect(self.btn_atangens)

    def write_number(self, number):
        if self.label_result.text()=="0":
            self.label_result.setText(number)
        else:
            self.label_result.setText(self.label_result.text()+number)

    def results(self):
        res=eval(self.label_result.text())
        self.label_result.setText(str(res))

    def clean_results(self):
        self.label_result.setText("0")

    def btn_font_style(self):
        b_fnt_stl="Arial"
        return b_fnt_stl

    def btn_font_size(self):
        b_fnt_sze=12
        return b_fnt_sze

    def num_pi(self):
        self.label_result.setText(str(math.pi))

    def num_e(self):
        self.label_result.setText(str(math.e))

    def btn_sinus(self):
        pp=self.label_result.text()
        if self.label_result.text()=="0":
            self.label_result.setText("math.sin(")
        elif pp[-1]=="+" or pp[-1]=="-" or pp[-1]=="*" or pp[-1]=="/":
            self.label_result.setText(self.label_result.text()+"math.sin(")

    def btn_cosinus(self):
        pp=self.label_result.text()
        if self.label_result.text()=="0":
            self.label_result.setText("math.cos(")
        elif pp[-1]=="+" or pp[-1]=="-" or pp[-1]=="*" or pp[-1]=="/":
            self.label_result.setText(self.label_result.text()+"math.cos(")

    def btn_tangens(self):
        pp=self.label_result.text()
        if self.label_result.text()=="0":
            self.label_result.setText("math.tg(")
        elif pp[-1]=="+" or pp[-1]=="-" or pp[-1]=="*" or pp[-1]=="/":
            self.label_result.setText(self.label_result.text()+"math.tg(")

    def btn_asinus(self):
        pp=self.label_result.text()
        if self.label_result.text()=="0":
            self.label_result.setText("math.asin(")
        elif pp[-1]=="+" or pp[-1]=="-" or pp[-1]=="*" or pp[-1]=="/":
            self.label_result.setText(self.label_result.text()+"math.asin(")

    def btn_acosinus(self):
        pp=self.label_result.text()
        if self.label_result.text()=="0":
            self.label_result.setText("math.acos(")
        elif pp[-1]=="+" or pp[-1]=="-" or pp[-1]=="*" or pp[-1]=="/":
            self.label_result.setText(self.label_result.text()+"math.acos(")

    def btn_atangens(self):
        pp=self.label_result.text()
        if self.label_result.text()=="0":
            self.label_result.setText("math.atg(")
        elif pp[-1]=="+" or pp[-1]=="-" or pp[-1]=="*" or pp[-1]=="/":
            self.label_result.setText(self.label_result.text()+"math.atg(")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())