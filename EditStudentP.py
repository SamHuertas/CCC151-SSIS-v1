from pathlib import Path
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog, QLabel, QPushButton

class Ui_EditStudentWindow(object):
    def setupUi(self, EditStudentWindow):
        EditStudentWindow.setObjectName("EditStudentWindow")
        EditStudentWindow.setFixedSize(381, 302)
        EditStudentWindow.setStyleSheet(Path('EditPopup.qss').read_text())

        # Main Frame
        self.EditStudent = QtWidgets.QFrame(parent=EditStudentWindow)
        self.EditStudent.setGeometry(QtCore.QRect(10, 10, 361, 281))
        self.EditStudent.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.EditStudent.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)

        # Labels
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)

        self.EditStudentText = QLabel("Edit Student", parent=self.EditStudent)
        self.EditStudentText.setGeometry(QtCore.QRect(10, 10, 151, 16))
        self.EditStudentText.setFont(font)
        self.EditStudentText.setObjectName("EditStudentText")

        font_normal = QtGui.QFont()
        font_normal.setFamily("Roboto")
        font_normal.setPointSize(12)

        self.IDText = QLabel("ID #", parent=self.EditStudent)
        self.IDText.setGeometry(QtCore.QRect(30, 40, 71, 21))
        self.IDText.setFont(font_normal)

        self.FNameText = QLabel("First Name", parent=self.EditStudent)
        self.FNameText.setGeometry(QtCore.QRect(30, 70, 81, 21))
        self.FNameText.setFont(font_normal)

        self.LNameText = QLabel("Last Name", parent=self.EditStudent)
        self.LNameText.setGeometry(QtCore.QRect(30, 100, 81, 21))
        self.LNameText.setFont(font_normal)

        self.GenderText = QLabel("Gender", parent=self.EditStudent)
        self.GenderText.setGeometry(QtCore.QRect(30, 130, 81, 21))
        self.GenderText.setFont(font_normal)

        self.YLevelText = QLabel("Year Level", parent=self.EditStudent)
        self.YLevelText.setGeometry(QtCore.QRect(30, 160, 81, 21))
        self.YLevelText.setFont(font_normal)

        self.PCodeText = QLabel("Program Code", parent=self.EditStudent)
        self.PCodeText.setGeometry(QtCore.QRect(30, 190, 111, 21))
        self.PCodeText.setFont(font_normal)

        # Input Fields
        font_input = QtGui.QFont("Roboto", 10)
        self.IDTB = QtWidgets.QLineEdit(parent=self.EditStudent)
        self.IDTB.setGeometry(QtCore.QRect(150, 40, 191, 21))
        self.IDTB.setFont(font_input)

        self.FNameTB = QtWidgets.QLineEdit(parent=self.EditStudent)
        self.FNameTB.setGeometry(QtCore.QRect(150, 70, 191, 21))
        self.FNameTB.setFont(font_input)

        self.LNameTB = QtWidgets.QLineEdit(parent=self.EditStudent)
        self.LNameTB.setGeometry(QtCore.QRect(150, 100, 191, 21))
        self.LNameTB.setFont(font_input)

        # Drop-down Fields
        font_dropdown = QtGui.QFont("Roboto")
        self.GenderDD = QtWidgets.QComboBox(parent=self.EditStudent)
        self.GenderDD.setGeometry(QtCore.QRect(150, 130, 81, 21))
        self.GenderDD.setFont(font_dropdown)
        self.GenderDD.addItems(["", "Male", "Female"])

        self.YLevelDD = QtWidgets.QComboBox(parent=self.EditStudent)
        self.YLevelDD.setGeometry(QtCore.QRect(150, 160, 81, 21))
        self.YLevelDD.setFont(font_dropdown)
        self.YLevelDD.addItems(["", "1", "2", "3", "4"])

        self.PCodeDD = QtWidgets.QComboBox(parent=self.EditStudent)
        self.PCodeDD.setGeometry(QtCore.QRect(150, 190, 81, 21))
        self.PCodeDD.setFont(font_dropdown)
        self.PCodeDD.addItem("")

        # Update Button
        font_button = QtGui.QFont("Roboto", 14)
        self.UpdateStudentButton = QPushButton("Update Student", parent=self.EditStudent)
        self.UpdateStudentButton.setGeometry(QtCore.QRect(10, 230, 341, 41))
        self.UpdateStudentButton.setFont(font_button)
        self.UpdateStudentButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        self.retranslateUi(EditStudentWindow)
        QtCore.QMetaObject.connectSlotsByName(EditStudentWindow)

    def retranslateUi(self, EditStudentWindow):
        _translate = QtCore.QCoreApplication.translate
        EditStudentWindow.setWindowTitle(_translate("EditStudentWindow", "Edit Student"))

# Main Window Class
class EditStudentWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_EditStudentWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Edit Student")
        self.setWindowIcon(QIcon('./StudentIcon.png'))

        self.ui.UpdateStudentButton.clicked.connect(self.close)

# Main Function to Run the Application
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = EditStudentWindow()
    window.show()
    sys.exit(app.exec())
