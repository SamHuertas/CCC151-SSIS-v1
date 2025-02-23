from pathlib import Path
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog, QLabel, QPushButton

class Ui_DeleteCollegePopup(object):
    def setupUi(self, DeleteCollegePopup):
        DeleteCollegePopup.setObjectName("DeleteCollegePopup")
        DeleteCollegePopup.setFixedSize(371, 201)
        DeleteCollegePopup.setStyleSheet(Path('Styles/DeletePopup.qss').read_text())

        # Confirmation Label
        self.Confirmation = QLabel(DeleteCollegePopup)
        self.Confirmation.setObjectName("Confirmation")
        self.Confirmation.setGeometry(QtCore.QRect(100, 20, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Confirmation.setFont(font)
        self.Confirmation.setAutoFillBackground(False)
        self.Confirmation.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.Confirmation.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Confirmation.setWordWrap(True)

        # Confirmation_2 Label
        self.Confirmation_2 = QLabel(DeleteCollegePopup)
        self.Confirmation_2.setObjectName("Confirmation_2")
        self.Confirmation_2.setGeometry(QtCore.QRect(30, 70, 311, 51))
        font1 = QtGui.QFont()
        font1.setFamily("Roboto")
        font1.setPointSize(11)
        self.Confirmation_2.setFont(font1)
        self.Confirmation_2.setAutoFillBackground(False)
        self.Confirmation_2.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.Confirmation_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Confirmation_2.setWordWrap(True)

        # Cancel Button
        self.CancelButton = QPushButton(DeleteCollegePopup)
        self.CancelButton.setObjectName("CancelButton")
        self.CancelButton.setGeometry(QtCore.QRect(60, 130, 121, 41))
        font2 = QtGui.QFont()
        font2.setFamily("Roboto")
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setWeight(50)
        self.CancelButton.setFont(font2)

        # Delete Button
        self.DeleteButton = QPushButton(DeleteCollegePopup)
        self.DeleteButton.setObjectName("DeleteButton")
        self.DeleteButton.setGeometry(QtCore.QRect(190, 130, 121, 41))
        self.DeleteButton.setFont(font2)

        self.retranslateUi(DeleteCollegePopup)
        QtCore.QMetaObject.connectSlotsByName(DeleteCollegePopup)

    def retranslateUi(self, DeleteCollegePopup):
        _translate = QtCore.QCoreApplication.translate
        DeleteCollegePopup.setWindowTitle(_translate("DeleteCollegePopup", "Dialog"))
        self.Confirmation.setText(_translate("DeleteCollegePopup", "Are you sure?"))
        self.Confirmation_2.setText(_translate("DeleteCollegePopup", "You are about to delete a college from the database"))
        self.CancelButton.setText(_translate("DeleteCollegePopup", "Cancel"))
        self.DeleteButton.setText(_translate("DeleteCollegePopup", "Delete"))

class DeleteCollegePopup(QDialog):
    def __init__(self, college_code, parent=None):
        super().__init__(parent)
        self.ui = Ui_DeleteCollegePopup()
        self.ui.setupUi(self)
        self.setWindowTitle('Confirm Delete')
        self.setWindowIcon(QIcon('Assets/StudentIcon.png'))

        self.college_code = college_code

        self.ui.CancelButton.clicked.connect(self.close)
        self.ui.DeleteButton.clicked.connect(self.delete_college)

    def delete_college(self, college_code):
        affected_programs = []
        program_lines = []
        with open("Database/Program.csv", "r") as file:
            program_lines = file.readlines()

        with open("Database/Program.csv", "w") as file:
            for line in program_lines:
                row = line.strip().split(",")
                if row[2] == self.college_code: 
                    affected_programs.append(row[0]) 
                    row[2] = "NULL"  
                file.write(",".join(row) + "\n")

        student_lines = []
        with open("Database/Student.csv", "r") as file:
            student_lines = file.readlines()

        with open("Database/Student.csv", "w") as file:
            for line in student_lines:
                row = line.strip().split(",")
                if row[5] in affected_programs: 
                    row[5] = "NULL"
                file.write(",".join(row) + "\n")

        college_lines = []
        with open("Database/College.csv", "r") as file:
            college_lines = file.readlines()

        with open("Database/College.csv", "w") as file:
            for line in college_lines:
                if not line.startswith(self.college_code + ","):
                    file.write(line)
        
        self.parent().openStudentCSV()
        self.parent().openProgramCSV()
        self.parent().openCollegeCSV()  
        self.parent().ui.ProgramTable.clearSelection()
        self.close()