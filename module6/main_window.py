import sys

from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox
from PyQt5 import uic, QtWidgets

from module6.team_member import TeamMember
from module6.team import Team
from module6.league import League
from module6.league_database import LeagueDatabase
from module6.league_edit_dialog import LeagueEditDialog


Ui_MainWindow, QtBaseWindow = uic.loadUiType("main_window.ui")


class MainWindow(QtBaseWindow, Ui_MainWindow):
    """
    Create MainWindow class to serve as the top level of the GUI.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.addLeague_button.clicked.connect(self.add_button_clicked)
        self.deleteLeague_button.clicked.connect(self.delete_button_clicked)
        self.editLeague_button.clicked.connect(self.edit_button_clicked)
        self.load_button.clicked.connect(self.load_button_clicked)
        self.save_button.clicked.connect(self.save_button_clicked)
        self.import_button.clicked.connect(self.import_button_clicked)

    def import_button_clicked(self):
        """
        Create import_button_clicked method to add functionality to the import button.
        :return: self.update_ui
        """
        dialog = QFileDialog()
        result = dialog.exec()
        league_name_in = self.import_lineEdit.text()
        if league_name_in == '':
            return self.warn("Import League", "Please give imported league a name")
        if result == QDialog.DialogCode.Accepted and league_name_in != '':
            file_name_list = dialog.selectedFiles()
            selected_file_name = file_name_list[0]
            LeagueDatabase.instance().import_league(league_name_in, selected_file_name)
            return self.update_ui()

    def save_button_clicked(self):
        """
        Create save_button_clicked method to add functionality to the save button.
        """
        dialog = QFileDialog.getSaveFileName()
        exported_file_name = dialog[0]
        if exported_file_name:
            LeagueDatabase.instance().save(exported_file_name)

    def load_button_clicked(self):
        """
        Create load_button_clicked method to add functionality to the load button.
        """
        dialog = QFileDialog()
        result = dialog.exec()
        if result == QDialog.DialogCode.Accepted:
            file_name_list = dialog.selectedFiles()
            selected_file_name = file_name_list[0]
            LeagueDatabase.instance().load(selected_file_name)
            self.update_ui()

    def add_button_clicked(self):
        """
        Create add_button_clicked method to add functionality to the add button.
        """
        string_in = self.addLeague_lineEdit.text()
        if string_in == '':
            return self.warn("Add League", "Please give added league a name")
        if string_in != '':
            LeagueDatabase.instance().add_league(League(LeagueDatabase.instance().next_oid(), string_in))
            self.update_ui()

    def update_ui(self):
        """
        Create update_ui method to update the listWidget after a method is performed.
        """
        self.league_listWidget.clear()
        for l in LeagueDatabase.instance().leagues:
            self.league_listWidget.addItem(str(l))

    def delete_button_clicked(self):
        """
        Create delete_button_clicked method to add functionality to the delete button.
        """
        selected_row = self.find_selected_row()
        if selected_row == -1:
            return self.warn("Select League", "Please select a league to delete")
        if selected_row != -1:
            LeagueDatabase.instance().delete_league(selected_row)
            self.update_ui()

    def warn(self, title, message):
        """
        Create a warn method to let the user know to select a line from the listWidget.
        :param title:
        :param message:
        :return: message box with warning
        """
        mb = QMessageBox(QMessageBox.Icon.NoIcon, title, message, QMessageBox.StandardButton.Ok)
        return mb.exec()

    def edit_button_clicked(self):
        """
        Create edit_button_clicked method to add functionality to the edit button.
        :return: warning or control back to the main window
        """
        row = self.find_selected_row()
        if row == -1:
            return self.warn("Select League", "Please select a league to edit")
        league_selected = LeagueDatabase.instance().leagues[row]
        if row != -1:
            dialog = LeagueEditDialog(league_selected)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                self.update_ui()
            else:
                return

    def find_selected_row(self):
        """
        Create find_selected_row method to select the correct row in the league database that corresponds to the
        selected line in the listWidget or -1 if no league was selected.
        """
        selection = self.league_listWidget.selectedItems()
        if len(selection) == 0:
            return -1
        assert len(selection) == 1
        selected_item = selection[0]
        for i, c in enumerate(LeagueDatabase.instance().leagues):
            if str(c) == selected_item.text():
                return i
        return -1


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
