from pathlib import Path
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog, QLabel, QPushButton
from Dialogs.DuplicateProgramP import DuplicateProgramPopup
from Dialogs.InputError import InputErrorPopup
import csv

class Ui_EditProgramPopup(object):
    def setupUi(self, EditProgramPopup):
        EditProgramPopup.setObjectName("EditProgramPopup")
        EditProgramPopup.setFixedSize(381, 210)
        EditProgramPopup.setStyleSheet(Path('Styles/EditPopup.qss').read_text())
        
        self.EditProgram = QtWidgets.QFrame(EditProgramPopup)
        self.EditProgram.setGeometry(QtCore.QRect(10, 10, 361, 191))
        self.EditProgram.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.EditProgram.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        
        self.UpdateProgramButton = QtWidgets.QPushButton(self.EditProgram)
        self.UpdateProgramButton.setGeometry(QtCore.QRect(10, 140, 341, 41))
        font = QtGui.QFont("Roboto", 14)
        self.UpdateProgramButton.setFont(font)
        self.UpdateProgramButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.UpdateProgramButton.setObjectName("UpdateProgramButton")
        
        self.PCollCodeText = QtWidgets.QLabel(self.EditProgram)
        self.PCollCodeText.setGeometry(QtCore.QRect(30, 100, 111, 21))
        font1 = QtGui.QFont("Roboto", 12)
        self.PCollCodeText.setFont(font1)
        self.PCollCodeText.setObjectName("PCollCodeTexte")
        
        self.PCodeTB = QtWidgets.QLineEdit(self.EditProgram)
        self.PCodeTB.setGeometry(QtCore.QRect(150, 40, 191, 21))
        font2 = QtGui.QFont("Roboto", 10)
        self.PCodeTB.setFont(font2)
        self.PCodeTB.setObjectName("PCodeTBe")
        
        self.AddProgramText = QtWidgets.QLabel(self.EditProgram)
        self.AddProgramText.setGeometry(QtCore.QRect(10, 10, 151, 21))
        font3 = QtGui.QFont("Roboto", 12, QtGui.QFont.Weight.Bold)
        self.AddProgramText.setFont(font3)
        self.AddProgramText.setObjectName("AddProgramTexte")
        
        self.PNameTB = QtWidgets.QLineEdit(self.EditProgram)
        self.PNameTB.setGeometry(QtCore.QRect(150, 70, 191, 21))
        self.PNameTB.setFont(font2)
        self.PNameTB.setObjectName("PNameTBe")
        
        self.PCodeText2 = QtWidgets.QLabel(self.EditProgram)
        self.PCodeText2.setGeometry(QtCore.QRect(30, 40, 111, 21))
        self.PCodeText2.setFont(font1)
        self.PCodeText2.setObjectName("PCodeText2e")
        
        self.PCollCodeDD = QtWidgets.QComboBox(self.EditProgram)
        self.PCollCodeDD.setGeometry(QtCore.QRect(150, 100, 81, 21))
        font4 = QtGui.QFont("Roboto")
        self.PCollCodeDD.setFont(font4)
        self.PCollCodeDD.setObjectName("PCollCodeDDe")
        
        self.PNameText = QtWidgets.QLabel(self.EditProgram)
        self.PNameText.setGeometry(QtCore.QRect(30, 70, 111, 21))
        self.PNameText.setFont(font1)
        self.PNameText.setObjectName("PNameTexte")
        
        self.retranslateUi(EditProgramPopup)
        QtCore.QMetaObject.connectSlotsByName(EditProgramPopup)

    def retranslateUi(self, EditProgramPopup):
        _translate = QtCore.QCoreApplication.translate
        EditProgramPopup.setWindowTitle(_translate("EditProgramPopup", "Edit Program"))
        self.UpdateProgramButton.setText(_translate("EditProgramPopup", "Update Program"))
        self.PCollCodeText.setText(_translate("EditProgramPopup", "College Code"))
        self.PCodeTB.setPlaceholderText(_translate("EditProgramPopup", "ex. BSCS"))
        self.AddProgramText.setText(_translate("EditProgramPopup", "Edit Program"))
        self.PNameTB.setPlaceholderText(_translate("EditProgramPopup", "ex. Bachelor of Science in Computer Science"))
        self.PCodeText2.setText(_translate("EditProgramPopup", "Code"))
        self.PNameText.setText(_translate("EditProgramPopup", "Program Name"))

# Main Window Class
class EditProgramPopup(QDialog):
    def __init__(self, main_window, selected_row):
        super().__init__()
        self.ui = Ui_EditProgramPopup()
        self.ui.setupUi(self)
        self.setWindowTitle("Edit Program")
        self.setWindowIcon(QIcon('Assets/StudentIcon.png'))
        self.main_window = main_window  
        self.selected_row = selected_row
        self.ui.UpdateProgramButton.clicked.connect(self.updateProgram)
        self.original_program_code = self.main_window.ui.ProgramTable.item(selected_row, 0).text()
        self.original_program_name = self.main_window.ui.ProgramTable.item(selected_row, 1).text()
        self.original_college_code = self.main_window.ui.ProgramTable.item(selected_row, 2).text()

    def updateProgram(self):
        new_code = self.ui.PCodeTB.text().strip().upper()
        new_program_name = self.ui.PNameTB.text().strip().title()
        new_programcollege_code = self.ui.PCollCodeDD.currentText()

        if not new_code or not new_program_name or not new_programcollege_code:
            input_error = InputErrorPopup()
            input_error.setModal(True)
            input_error.exec()
            return

        for row in range(self.main_window.ui.ProgramTable.rowCount()):
            existing_pcode = self.main_window.ui.ProgramTable.item(row, 0).text()
            if new_code == existing_pcode and row != self.selected_row:
                self.duplicate_popup = DuplicateProgramPopup()
                self.duplicate_popup.setModal(True)
                self.duplicate_popup.show()
                return

        self.main_window.ui.ProgramTable.item(self.selected_row, 0).setText(new_code)
        self.main_window.ui.ProgramTable.item(self.selected_row, 1).setText(new_program_name)
        pcollege_item = self.main_window.ui.ProgramTable.item(self.selected_row, 2)
        if pcollege_item is None:
            pcollege_item = QtWidgets.QTableWidgetItem(new_programcollege_code)
            self.main_window.ui.ProgramTable.setItem(self.selected_row, 2, pcollege_item)
        else:
                pcollege_item.setText(new_programcollege_code)

        if new_programcollege_code.strip().upper() == "NULL":
            pcollege_item.setForeground(QtGui.QColor("red"))
        else:
            pcollege_item.setForeground(QtGui.QColor("black"))

        self.saveUpdatedProgramToCSV()
        if new_code != self.original_program_code:
            self.updateStudentCSV(self.original_program_code, new_code)
        self.main_window.openProgramCSV()
        self.main_window.PopulateProgramCode()
        self.close()

    def saveUpdatedProgramToCSV(self):
        updated_code = self.ui.PCodeTB.text().strip().upper()
        updated_name = self.ui.PNameTB.text().strip().title()
        updated_college = self.ui.PCollCodeDD.currentText()
        
        with open("Database/Program.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

        for i in range(1, len(rows)):
            if rows[i][0] == self.original_program_code:
                rows[i] = [updated_code, updated_name, updated_college]
                break

        with open("Database/Program.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    def updateStudentCSV(self, old_code, new_code):
        with open("Database/Student.csv", "r") as file:
            reader = csv.reader(file)
            student_rows = list(reader)

        updated = False
        for row in student_rows[1:]:  
            if len(row) > 5 and row[5] == old_code: 
                row[5] = new_code
                updated = True
        
        if updated:
            with open("Database/Student.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(student_rows)
            
            self.main_window.openStudentCSV()
            self.main_window.PopulateProgramCode() 