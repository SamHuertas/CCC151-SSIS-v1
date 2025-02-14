    for col in range(self.ui.tableWidget.columnCount()):
            header.setSectionResizeMode(col, QHeaderView.ResizeMode.ResizeToContents)  # Adjust to content first
        
        header.setSectionResizeMode(self.ui.tableWidget.columnCount() - 1, QHeaderView.ResizeMode.Stretch)  # Stretch last column

        self.ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        self.ui.tableWidget.horizontalHeader().setHighlightSections(False)
        self.ui.tableWidget.verticalHeader().setHighlightSections(False)
        self.ui.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.ui.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.tableWidget.setAlternatingRowColors(True)