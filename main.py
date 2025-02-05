from PyQt5.QtWidgets import QApplication, QDialog, QFrame, QLabel, QLineEdit, QComboBox, QPushButton, QTableWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(1317, 786)
        font = QFont()
        font.setPointSize(8)
        Dialog.setFont(font)

        #start of add student frame
        self.addstudent = QFrame(Dialog)
        self.addstudent.setObjectName("addstudent")
        self.addstudent.setGeometry(920, 30, 361, 271)
        self.addstudent.setFrameShape(QFrame.StyledPanel)
        self.addstudent.setFrameShadow(QFrame.Raised)

        self.label = QLabel(self.addstudent)
        self.label.setObjectName("label")
        self.label.setGeometry(10, 10, 151, 16)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)

        self.label_2 = QLabel(self.addstudent)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(30, 40, 71, 21)
        font2 = QFont()
        font2.setPointSize(12)
        self.label_2.setFont(font2)

        self.label_3 = QLabel(self.addstudent)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(30, 70, 81, 21)
        self.label_3.setFont(font2)

        self.label_4 = QLabel(self.addstudent)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(30, 100, 81, 21)
        self.label_4.setFont(font2)

        self.label_6 = QLabel(self.addstudent)
        self.label_6.setObjectName("label_6")
        self.label_6.setGeometry(30, 160, 81, 21)
        self.label_6.setFont(font2)

        self.IDtextbox = QLineEdit(self.addstudent)
        self.IDtextbox.setObjectName("IDtextbox")
        self.IDtextbox.setGeometry(150, 40, 191, 21)
        self.IDtextbox.setFont(font2)

        self.genderdd = QComboBox(self.addstudent)
        self.genderdd.addItem("")
        self.genderdd.addItems(["Male", "Female"])
        self.genderdd.activated.connect(self.remove_empty_item)
        self.genderdd.setObjectName("genderdd")
        self.genderdd.setGeometry(150, 130, 81, 21)

        self.label_5 = QLabel(self.addstudent)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(30, 130, 81, 21)
        self.label_5.setFont(font2)

        self.yearleveldd = QComboBox(self.addstudent)
        self.yearleveldd.setObjectName("yearleveldd")
        self.yearleveldd.addItem("")
        self.yearleveldd.addItems(["1st Year", "2nd Year", "3rd Year", "4th Year"])
        self.yearleveldd.activated.connect(self.remove_empty_item)
        self.yearleveldd.setGeometry(150, 160, 81, 21)

        self.fnametextbox = QLineEdit(self.addstudent)
        self.fnametextbox.setObjectName("fnametextbox")
        self.fnametextbox.setGeometry(150, 70, 191, 21)
        self.fnametextbox.setFont(font2)

        self.lnametextbox = QLineEdit(self.addstudent)
        self.lnametextbox.setObjectName("lnametextbox")
        self.lnametextbox.setGeometry(150, 100, 191, 21)
        self.lnametextbox.setFont(font2)

        self.label_7 = QLabel(self.addstudent)
        self.label_7.setObjectName("label_7")
        self.label_7.setGeometry(30, 190, 111, 21)
        self.label_7.setFont(font2)

        self.pcodedd = QComboBox(self.addstudent)
        self.pcodedd.setObjectName("pcodedd")
        self.pcodedd.addItem("")
        self.pcodedd.addItems([])                                       ##add items in program csv data
        self.pcodedd.activated.connect(self.remove_empty_item)
        self.pcodedd.setGeometry(150, 190, 81, 21)

        self.addstudentbutton = QPushButton(self.addstudent)
        self.addstudentbutton.setObjectName("addstudentbutton")
        self.addstudentbutton.setGeometry(220, 230, 131, 31)
        font3 = QFont()
        font3.setPointSize(14)
        self.addstudentbutton.setFont(font3)
        self.addstudentbutton.setCursor(Qt.PointingHandCursor)
        #end of add student frame

        self.addprogram = QFrame(Dialog)
        self.addprogram.setObjectName("addprogram")
        self.addprogram.setGeometry(920, 470, 361, 181)
        self.addprogram.setFrameShape(QFrame.StyledPanel)
        self.addprogram.setFrameShadow(QFrame.Raised)

        self.label_8 = QLabel(self.addprogram)
        self.label_8.setObjectName("label_8")
        self.label_8.setGeometry(10, 10, 151, 21)
        self.label_8.setFont(font1)

        self.label_11 = QLabel(self.addprogram)
        self.label_11.setObjectName("label_11")
        self.label_11.setGeometry(30, 40, 111, 21)
        self.label_11.setFont(font2)

        self.codetextbox = QLineEdit(self.addprogram)
        self.codetextbox.setObjectName("codetextbox")
        self.codetextbox.setGeometry(150, 40, 191, 21)
        self.codetextbox.setFont(font2)

        self.label_9 = QLabel(self.addprogram)
        self.label_9.setObjectName("label_9")
        self.label_9.setGeometry(30, 70, 111, 21)
        self.label_9.setFont(font2)

        self.label_10 = QLabel(self.addprogram)
        self.label_10.setObjectName("label_10")
        self.label_10.setGeometry(30, 100, 111, 21)
        self.label_10.setFont(font2)

        self.pnametextbox = QLineEdit(self.addprogram)
        self.pnametextbox.setObjectName("pnametextbox")
        self.pnametextbox.setGeometry(150, 70, 191, 21)
        self.pnametextbox.setFont(font2)

        self.ccodetextbox = QLineEdit(self.addprogram)
        self.ccodetextbox.setObjectName("ccodetextbox")
        self.ccodetextbox.setGeometry(150, 100, 191, 21)
        self.ccodetextbox.setFont(font2)

        self.addprogrambutton = QPushButton(self.addprogram)
        self.addprogrambutton.setObjectName("addprogrambutton")
        self.addprogrambutton.setGeometry(220, 140, 121, 31)
        self.addprogrambutton.setFont(font3)
        self.addprogrambutton.setCursor(Qt.PointingHandCursor)

        self.addcollege = QFrame(Dialog)
        self.addcollege.setObjectName("addcollege")
        self.addcollege.setGeometry(920, 310, 361, 151)
        self.addcollege.setFrameShape(QFrame.StyledPanel)
        self.addcollege.setFrameShadow(QFrame.Raised)

        self.label_12 = QLabel(self.addcollege)
        self.label_12.setObjectName("label_12")
        self.label_12.setGeometry(10, 10, 151, 21)
        self.label_12.setFont(font1)

        self.label_13 = QLabel(self.addcollege)
        self.label_13.setObjectName("label_13")
        self.label_13.setGeometry(30, 40, 111, 21)
        self.label_13.setFont(font2)

        self.ccodetextbox_2 = QLineEdit(self.addcollege)
        self.ccodetextbox_2.setObjectName("ccodetextbox_2")
        self.ccodetextbox_2.setGeometry(150, 40, 191, 21)
        self.ccodetextbox_2.setFont(font2)

        self.label_14 = QLabel(self.addcollege)
        self.label_14.setObjectName("label_14")
        self.label_14.setGeometry(30, 70, 111, 21)
        self.label_14.setFont(font2)

        self.cnametextbox = QLineEdit(self.addcollege)
        self.cnametextbox.setObjectName("cnametextbox")
        self.cnametextbox.setGeometry(150, 70, 191, 21)
        self.cnametextbox.setFont(font2)

        self.addprogrambutton_2 = QPushButton(self.addcollege)
        self.addprogrambutton_2.setObjectName("addprogrambutton_2")
        self.addprogrambutton_2.setGeometry(220, 110, 121, 31)
        self.addprogrambutton_2.setFont(font3)
        self.addprogrambutton_2.setCursor(Qt.PointingHandCursor)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(50, 50, 831, 571)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName("label_15")
        self.label_15.setGeometry(20, 20, 81, 21)
        self.label_15.setFont(font2)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setGeometry(100, 20, 91, 22)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setGeometry(200, 20, 201, 21)
        self.lineEdit.setFont(font2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(410, 20, 61, 21)
        self.pushButton.setFont(font2)
        self.pushButton.setCursor(Qt.PointingHandCursor)

        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName("label_16")
        self.label_16.setGeometry(20, 50, 81, 21)
        self.label_16.setFont(font2)

        self.comboBox_2 = QComboBox(self.frame)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setGeometry(100, 50, 91, 22)

        self.tableWidget = QTableWidget(self.frame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setGeometry(20, 90, 791, 461)

        self.retranslateUi(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Add Student"))
        self.label_2.setText(_translate("Dialog", "ID #"))
        self.label_3.setText(_translate("Dialog", "First Name"))
        self.label_4.setText(_translate("Dialog", "Last Name"))
        self.label_6.setText(_translate("Dialog", "Year Level"))
        self.label_5.setText(_translate("Dialog", "Gender"))
        self.label_7.setText(_translate("Dialog", "Program Code"))
        self.addstudentbutton.setText(_translate("Dialog", "Add Student"))
        self.label_8.setText(_translate("Dialog", "Add Program"))
        self.label_11.setText(_translate("Dialog", "Code"))
        self.codetextbox.setPlaceholderText(_translate("Dialog", "ex. BSCS"))
        self.label_9.setText(_translate("Dialog", "Program Name"))
        self.label_10.setText(_translate("Dialog", "College Code"))
        self.pnametextbox.setPlaceholderText(_translate("Dialog", "ex. Bachelor of Science in Computer Science"))
        self.ccodetextbox.setPlaceholderText(_translate("Dialog", "ex. CCS"))
        self.addprogrambutton.setText(_translate("Dialog", "Add Program"))
        self.label_12.setText(_translate("Dialog", "Add College"))
        self.label_13.setText(_translate("Dialog", "Code"))
        self.ccodetextbox_2.setPlaceholderText(_translate("Dialog", "ex. CCS"))
        self.label_14.setText(_translate("Dialog", "College Name"))
        self.cnametextbox.setPlaceholderText(_translate("Dialog", "ex. College of Computer Studies"))
        self.addprogrambutton_2.setText(_translate("Dialog", "Add College"))
        self.label_15.setText(_translate("Dialog", "Search by:"))
        self.pushButton.setText(_translate("Dialog", "Search"))
        self.label_16.setText(_translate("Dialog", "Sort by:"))

    def remove_empty_item(self):
        if self.genderdd.itemText(0) == "":
            self.genderdd.removeItem(0)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())