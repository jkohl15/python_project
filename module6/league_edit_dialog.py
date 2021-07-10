import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog
from module6.team_edit_dialog import TeamEditDialog
from module6.team import Team
from module6.league import League
from module6.league_database import LeagueDatabase


Ui_MainWindow, QtBaseWindow = uic.loadUiType("league_edit_dialog.ui")


class LeagueEditDialog(QtBaseWindow, Ui_MainWindow):
    """
    Create LeagueEditDialog class for editing selected leagues in the main window.
    """
    def __init__(self, league_selected, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.add_button.clicked.connect(self.add_button_clicked)
        self.edit_button.clicked.connect(self.edit_button_clicked)
        self.delete_button.clicked.connect(self.delete_button_clicked)
        self.league_in = league_selected
        self.export_button.clicked.connect(self.export_button_clicked)
        for l in league_selected.teams:
            self.league_listWidget.addItem(str(l))

    def export_button_clicked(self):
        """
        Create export_button_clicked method to export the selected league to a CSV file.
        """
        dialog = QFileDialog.getSaveFileName()
        exported_file_name = dialog[0]
        if exported_file_name:
            LeagueDatabase.instance().export_league(self.league_in.name, exported_file_name)
            print()

    def add_button_clicked(self):
        """
        Create add_button_clicked method to add functionality to the add button.
        """
        string_in = self.add_team_lineEdit.text()
        if string_in == '':
            return self.warn("Add Team", "Please give the added team a name")
        if string_in != '':
            # LeagueDatabase.instance()
            for l in LeagueDatabase.instance().leagues:
                if self.league_in == l:
                    team = Team(LeagueDatabase.instance().next_oid(), string_in)
                    l.add_team(team)
        self.update_ui()

    def update_ui(self):
        """
        Create update_ui method to update the listWidget at the end of a method.
        """
        self.league_listWidget.clear()
        # LeagueDatabase.instance()
        for l in LeagueDatabase.instance().leagues:
            if self.league_in == l:
                for l2 in l.teams:
                    self.league_listWidget.addItem(str(l2))

    def find_selected_row(self):
        """
        Create find_selected_row method to choose the correct team in the league database
        :return: corresponding team in the database or -1 if no team was selected
        """
        selection = self.league_listWidget.selectedItems()
        if len(selection) == 0:
            return -1
        assert len(selection) == 1
        selected_item = selection[0]
        for l in LeagueDatabase.instance().leagues:
            if self.league_in == l:
                for i, c in enumerate(l.teams):
                    if str(c) == selected_item.text():
                        return i
        return -1

    def warn(self, title, message):
        """
        Create warn method to inform the user of a needed action
        :param title:
        :param message:
        :return: warning message
        """
        mb = QMessageBox(QMessageBox.Icon.NoIcon, title, message, QMessageBox.StandardButton.Ok)
        return mb.exec()

    def edit_button_clicked(self):
        """
        Create edit_button_clicked method to add funtionality to the edit button.
        :return: warning message to select a team or the team edit dialog box
        """
        row = self.find_selected_row()
        if row == -1:
            return self.warn("Select Team", "Please select a team to edit")
        selected_team = self.league_in.teams[row]
        if row != -1:
            dialog = TeamEditDialog(self.league_in, selected_team)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                self.update_ui()
            else:
                return

    def delete_button_clicked(self):
        """
        Create delete_button_clicked to add functionality to the delete button.
        :return: warning message or updated listWidget
        """
        row = self.find_selected_row()
        if row == -1:
            return self.warn("Select Team", "Please select a team to delete")
        if row != -1:
            for l in LeagueDatabase.instance().leagues:
                if self.league_in == l:
                    l.delete_team(row)
        self.update_ui()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LeagueEditDialog()
    window.show()
    sys.exit(app.exec_())
