class Ui_MainPage:
    def setupUi(self, MainPage):
        if MainPage.objectName() == "":
            MainPage.setObjectName("MainPage")
        MainPage.resize(1491, 751)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainPage.setFont(font)
        MainPage.setStyleSheet("#MainPage {\n"
                               "	background-color: #e0f7fa;\n"
                               "}\n"
                               "#AddStudent, #AddCollege, #AddProgram, #Database {\n"
                               "	background-color: #ffffff;\n"
                               "	border-radius: 18px;\n"
                               "	box-shadow: 10px 9px 7px 1px rgba(0,0,0,0.83);\n"
                               "}\n"
                               "#MainPage QPushButton {\n"
                               "	background-color: #1e88e5;\n"
                               "	border-radius: 13px;\n"
                               "	box-shadow: 10px 9px 7px 1px rgba(0,0,0,0.83);\n"
                               "	color: white;\n"
                               "}\n"
                               "#MainPage QPushButton:hover {\n"
                               "	background-color: rgb(27, 126, 212);\n"
                               "}\n"
                               "#MainPage QPushButton:pressed {\n"
                               "	border: 4px solid rgb(152, 205, 229);\n"
                               "}\n"
                               "#MainPage QLineEdit {\n"
                               "	border-radius: 5px;\n"
                               "	background-color: rgb(245, 245, 245);\n"
                               "	border: 1px solid rgb(235, 235, 235);\n"
                               "}\n"
                               "#MainPage QLineEdit:hover {\n"
                               "	border: rgb(250, 250, 250);\n"
                               "}\n"
                               "#MainPage QLineEdit:focus {\n"
                               "	border: rgb(210, 210, 210);\n"
                               "	background-color: rgb(231, 231, 231)\n"
                               "}\n"
                               "QTableWidget{\n"
                               "	border-radius: 15px;\n"
                               "	background-color: rgb(245, 245, 245);\n"
                               "	border: 1px solid rgb(235, 235, 235);\n"
                               "}\n"
                               "#Heading {\n"
                               "	background-color: rgb(252, 252, 252);\n"
                               "}")

        # Add Student Frame
        self.AddStudent = QtWidgets.QFrame(MainPage)
        self.AddStudent.setObjectName("AddStudent")
        self.AddStudent.setGeometry(QtCore.QRect(1050, 80, 411, 271))
        font1 = QtGui.QFont()
        font1.setFamily("Roboto")
        self.AddStudent.setFont(font1)
        self.AddStudent.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AddStudent.setFrameShadow(QtWidgets.QFrame.Raised)

        self.AddStudentText = QtWidgets.QLabel(self.AddStudent)
        self.AddStudentText.setObjectName("AddStudentText")
        self.AddStudentText.setGeometry(QtCore.QRect(10, 10, 151, 16))
        font2 = QtGui.QFont()
        font2.setFamily("Roboto")
        font2.setPointSize(12)
        font2.setBold(True)
        self.AddStudentText.setFont(font2)

        # Other UI elements for AddStudent
        self.IDText = self.create_label(self.AddStudent, "IDText", 30, 40, "ID #")
        self.FNameText = self.create_label(self.AddStudent, "FNameText", 30, 70, "First Name")
        self.LNameText = self.create_label(self.AddStudent, "LNameText", 30, 100, "Last Name")
        self.YLevelText = self.create_label(self.AddStudent, "YLevelText", 30, 160, "Year Level")

        self.IDTB = self.create_line_edit(self.AddStudent, "IDTB", 150, 40)
        self.GenderDD = self.create_combo_box(self.AddStudent, "GenderDD", 150, 130)
        self.GenderText = self.create_label(self.AddStudent, "GenderText", 30, 130, "Gender")
        self.YLevelDD = self.create_combo_box(self.AddStudent, "YLevelDD", 150, 160)
        self.FNameTB = self.create_line_edit(self.AddStudent, "FNameTB", 150, 70)
        self.LNameTB = self.create_line_edit(self.AddStudent, "LNameTB", 150, 100)
        self.PCodeText = self.create_label(self.AddStudent, "PCodeText", 30, 190, "Program Code")
        self.PCodeDD = self.create_combo_box(self.AddStudent, "PCodeDD", 150, 190)

        self.AddStudentButton = self.create_button(self.AddStudent, "AddStudentButton", 280, 230, "Add Student")

        # Add Program Frame
        self.AddProgram = QtWidgets.QFrame(MainPage)
        self.AddProgram.setObjectName("AddProgram")
        self.AddProgram.setGeometry(QtCore.QRect(1050, 540, 411, 181))
        self.AddProgram.setFont(font1)
        self.AddProgram.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AddProgram.setFrameShadow(QtWidgets.QFrame.Raised)

        self.AddProgramText = self.create_label(self.AddProgram, "AddProgramText", 10, 10, "Add Program")
        self.PCodeText2 = self.create_label(self.AddProgram, "PCodeText2", 30, 40, "Code")
        self.PCodeTB = self.create_line_edit(self.AddProgram, "PCodeTB", 150, 40)
        self.PNameText = self.create_label(self.AddProgram, "PNameText", 30, 70, "Program Name")
        self.PCollCodeText = self.create_label(self.AddProgram, "PCollCodeText", 30, 100, "College Code")
        self.PNameTB = self.create_line_edit(self.AddProgram, "PNameTB", 150, 70)
        self.AddProgramButton = self.create_button(self.AddProgram, "AddProgramButton", 280, 140, "Add Program")
        self.PCollCodeDD = self.create_combo_box(self.AddProgram, "PCollCodeDD", 150, 100)

        # Add College Frame
        self.AddCollege = QtWidgets.QFrame(MainPage)
        self.AddCollege.setObjectName("AddCollege")
        self.AddCollege.setGeometry(QtCore.QRect(1050, 370, 411, 151))
        self.AddCollege.setFont(font1)
        self.AddCollege.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AddCollege.setFrameShadow(QtWidgets.QFrame.Raised)

        self.AddCollegeText = self.create_label(self.AddCollege, "AddCollegeText", 10, 10, "Add College")
        self.CCodeText = self.create_label(self.AddCollege, "CCodeText", 30, 40, "Code")
        self.CCodeTB = self.create_line_edit(self.AddCollege, "CCodeTB", 150, 40)
        self.CNameText = self.create_label(self.AddCollege, "CNameText", 30, 70, "College Name")
        self.CNameTB = self.create_line_edit(self.AddCollege, "CNameTB", 150, 70)
        self.AddCollegeButton = self.create_button(self.AddCollege, "AddCollegeButton", 280, 110, "Add College")

        # Database Frame
        self.Database = QtWidgets.QFrame(MainPage)
        self.Database.setObjectName("Database")
        self.Database.setGeometry(QtCore.QRect(30, 80, 1001, 641))
        self.Database.setFont(font1)
        self.Database.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Database.setFrameShadow(QtWidgets.QFrame.Raised)

        self.SearchText = self.create_label(self.Database, "SearchText", 20, 20, "Search by:")
        self.SearchDD = self.create_combo_box(self.Database, "SearchDD", 100, 20)
        self.SearchTB = self.create_line_edit(self.Database, "SearchTB", 190, 20)
        self.SearchButton = self.create_button(self.Database, "SearchButton", 410, 20, "Search")
        self.SortText = self.create_label(self.Database, "SortText", 20, 50, "Sort by:")
        self.SortDD = self.create_combo_box(self.Database, "SortDD", 100, 50)
        self.tableWidget = QtWidgets.QTableWidget(self.Database)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 961, 491))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(["ID#", "First Name", "Last Name", "Year Level", "Gender", "Program Code"])
        self.EditStudentButton = self.create_button(self.Database, "EditStudentButton", 20, 590, "Edit Student")
        self.DeleteStudentButton = self.create_button(self.Database, "DeleteStudentButton", 150, 590, "Delete Student")

        # Heading Frame
        self.Heading = QtWidgets.QFrame(MainPage)
        self.Heading.setObjectName("Heading")
        self.Heading.setGeometry(QtCore.QRect(0, 0, 1491, 51))
        self.Heading.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Heading.setFrameShadow(QtWidgets.QFrame.Raised)

        self.HeadingTitle = QtWidgets.QLabel(self.Heading)
        self.HeadingTitle.setObjectName("HeadingTitle")
        self.HeadingTitle.setGeometry(QtCore.QRect(40, 10, 211, 31))
        self.HeadingTitle.setFont(font)

        self.retranslateUi(MainPage)
        QtCore.QMetaObject.connectSlotsByName(MainPage)

    def create_label(self, parent, name, x, y, text):
        label = QtWidgets.QLabel(parent)
        label.setObjectName(name)
        label.setGeometry(QtCore.QRect(x, y, 111, 21))
        label.setText(text)
        return label

    def create_line_edit(self, parent, name, x, y):
        line_edit = QtWidgets.QLineEdit(parent)
        line_edit.setObjectName(name)
        line_edit.setGeometry(QtCore.QRect(x, y, 231, 21))
        return line_edit

    def create_combo_box(self, parent, name, x, y):
        combo_box = QtWidgets.QComboBox(parent)
        combo_box.setObjectName(name)
        combo_box.setGeometry(QtCore.QRect(x, y, 81, 21))
        return combo_box

    def create_button(self, parent, name, x, y, text):
        button = QtWidgets.QPushButton(parent)
        button.setObjectName(name)
        button.setGeometry(QtCore.QRect(x, y, 121, 31))
        button.setText(text)
        return button

    def retranslateUi(self, MainPage):
        MainPage.setWindowTitle("Dialog")
        self.AddStudentText.setText("Add Student")
        self.IDText.setText("ID #")
        self.FNameText.setText("First Name")
        self.LNameText.setText("Last Name")
        self.YLevelText.setText("Year Level")
        self.GenderText.setText("Gender")
        self.PCodeText.setText("Program Code")
        self.AddStudentButton.setText("Add Student")
        self.AddProgramText.setText("Add Program")
        self.PCodeText2.setText("Code")
        self.PNameText.setText("Program Name")
        self.PCollCodeText.setText("College Code")
        self.AddProgramButton.setText("Add Program")
        self.AddCollegeText.setText("Add College")
        self.CCodeText.setText("Code")
        self.CNameText.setText("College Name")
        self.AddCollegeButton.setText("Add College")
        self.SearchText.setText("Search by:")
        self.SortText.setText("Sort by:")
        self.EditStudentButton.setText("Edit Student")
        self.DeleteStudentButton.setText("Delete Student")
        self.HeadingTitle.setText("Student Information System")
