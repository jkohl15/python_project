import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from module6.league_database import LeagueDatabase
from module6.team import Team
from module6.team_member import TeamMember

Ui_MainWindow, QtBaseWindow = uic.loadUiType("team_edit_dialog.ui")


class TeamEditDialog(QtBaseWindow, Ui_MainWindow):
    """
    Create TeamEditDialog class.
    """
    def __init__(self, league_selected, team_selected, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.league_in = league_selected
        self.team_in = team_selected
        self.add_button.clicked.connect(self.add_button_clicked)
        self.delete_button.clicked.connect(self.delete_button_clicked)
        self.update_button.clicked.connect(self.update_button_clicked)
        for tm in self.team_in.members:
            self.team_listWidget.addItem(str(tm))

    def add_button_clicked(self):
        """
        Create add_button_clicked method to add functionality to the add button.
        """
        name_string_in = self.name_lineEdit.text()
        if name_string_in == '':
            self.warn("Add Team Member", "Please give the team member a name")
        email_string_in = self.email_lineEdit.text()
        if email_string_in == '':
            self.warn("Add Team Member", "Please give the team member an email")
        if name_string_in != '' and email_string_in != '':
            # LeagueDatabase.instance()
            for l in LeagueDatabase.instance().leagues:
                if self.league_in == l:
                    for tm in l.teams:
                        if tm == self.team_in:
                            tm.add_member(TeamMember(LeagueDatabase.instance().next_oid(), name_string_in, email_string_in))
        self.update_ui()

    def update_ui(self):
        """
        Create update_ui method to update the listWidget at the end of a method.
        """
        self.team_listWidget.clear()
        # LeagueDatabase.instance()
        for l in LeagueDatabase.instance().leagues:
            if self.league_in == l:
                for l2 in l.teams:
                    if self.team_in == l2:
                        for tm in l2.members:
                            self.team_listWidget.addItem(str(tm))

    def find_selected_row(self):
        """
        Create find_selected_row method to pick the correct team member from the database.  Return -1 if no one is selected.
        """
        selection = self.team_listWidget.selectedItems()
        if len(selection) == 0:
            return -1
        assert len(selection) == 1
        selected_item = selection[0]
        for l in LeagueDatabase.instance().leagues:
            if self.league_in == l:
                for team in l.teams:
                    if team == self.team_in:
                        for i, c in enumerate(team.members):
                            if str(c) == selected_item.text():
                                return i
        return -1

    def warn(self, title, message):
        """
        Create warn method to warn the user of missing data.
        :param title:
        :param message:
        :return: dialog screen
        """
        mb = QMessageBox(QMessageBox.Icon.NoIcon, title, message, QMessageBox.StandardButton.Ok)
        return mb.exec()

    def delete_button_clicked(self):
        """
        Create delete_button_clicked method to add functionality to the delete button.
        """
        row = self.find_selected_row()
        if row == -1:
            self.warn("Select Team Member", "Please select a team member to delete")
        if row != -1:
            for l in LeagueDatabase.instance().leagues:
                if self.league_in == l:
                    for team in l.teams:
                        if self.team_in == team:
                            for i, tm in enumerate(team.members):
                                if row == i:
                                    team.remove_member(tm)
                                    break
        self.update_ui()

    def update_button_clicked(self):
        """
        Create update_button_clicked method to add functionality to the update button.
        :return:
        """
        row = self.find_selected_row()
        if row == -1:
            self.warn("Select Team Member", "Please select a team member to update")
        name_string_in = self.name2_lineEdit.text()
        email_string_in = self.email2_lineEdit.text()
        if name_string_in != '' and email_string_in != '':
            # LeagueDatabase.instance()
            for l in LeagueDatabase.instance().leagues:
                if self.league_in == l:
                    for team in l.teams:
                        if self.team_in == team:
                            for i, tm in enumerate(team.members):
                                if i == row:
                                    tm.name = name_string_in
                                    tm.email = email_string_in
        self.update_ui()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = TeamEditDialog()
    window.show()
    sys.exit(app.exec_())