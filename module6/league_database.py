import pickle
import csv
import os

from module6.league import League
from module6.team import Team
from module6.team_member import TeamMember
from module6.team import DuplicateEmail


class LeagueDatabase:
    _sole_instance = None

    @classmethod
    def instance(cls):
        """
        Create instance class method using a singleton model.
        :return: cls._sole_instance
        """
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance

    def __init__(self):
        self._leagues = []
        self._last_oid = 0

    @classmethod
    def load(cls, file_name):
        """
        Create load class method to bring in a file to the program.
        :param file_name:
        :return: cls._sole_instance
        """
        file_name_backup = file_name + ".backup"
        try:
            with open(file_name, mode="rb") as f:
                cls._sole_instance = pickle.load(f)
                return cls._sole_instance
        except FileNotFoundError:
            print(f"File {file_name} not found, looking for a backup file.")
            try:
                with open(file_name_backup, mode="rb") as g:
                    cls._sole_instance = pickle.load(g)
                    return cls._sole_instance
            except FileNotFoundError:
                print(f"The backup file for {file_name} was not found either.")
                return
            except (pickle.UnpicklingError, IOError):
                print("Unpickling error occurred.")
        except (pickle.UnpicklingError, IOError):
            print("Unpickling error occurred.")

    @property
    def leagues(self):
        """
        Create leagues property
        :return: self._leagues
        """
        return self._leagues

    def add_league(self, league):
        """
        Create add_league method to add a league to the database
        :param league:
        """
        self._leagues.append(league)

    # Jeff added on July 1
    def delete_league(self, index):
        """
        Create delete_league method to delete a league from the database.
        :param index:
        """
        del self._leagues[index]

    def next_oid(self):
        """
        Create next_oid to increment the OID.
        :return: self._last_oid
        """
        self._last_oid = self._last_oid + 1
        return self._last_oid

    def save(self, file_name):
        """
        Create save method to save the database.
        :param file_name:
        """
        try:
            # check if original file name exists
            if os.path.exists(file_name):

                # check if backup file name exists, and if it does, delete it
                if os.path.exists(file_name + '.backup'):
                    os.remove(file_name + '.backup')

                # if original file name exists, rename it with "backup" added to the end
                os.rename(file_name, file_name + '.backup')
                f = open(file_name, mode="wb")
                pickle.dump(self._sole_instance, f)

            # use this code block if the file name did NOT exist
            else:
                f = open(file_name, mode="wb")
                pickle.dump(self._sole_instance, f)
        except (pickle.PickleError, IOError):
            print("Error while saving.")

    def import_league(self, league_name, file_name):
        """
        Create import_league method to import a league into the database.
        :param league_name:
        :param file_name:
        """
        league_to_add = League(self._last_oid, league_name)
        self.next_oid()
        try:
            with open(file_name, encoding="utf-8") as csvfile:
                # keep track of which team names are in the file
                team_tracker_in_file = []
                # keep track of which unique teams have actually been created
                team_added_tracker = []

                rowreader = csv.reader(csvfile, delimiter=',')
                # skip the header row
                next(rowreader)

                # iterate through each value in the row
                for row in rowreader:
                    team_in = row[0]

                    # when a new team name appears in the list, add it to the team_tracker_in_file
                    if team_in not in team_tracker_in_file:
                        team_tracker_in_file.append(team_in)

                        # make a new Team object
                        t = Team(self._last_oid, team_in)
                        self.next_oid()

                        # add newly created Team object to the team_added_tracker and add Team to league list
                        team_added_tracker.append(t)
                        league_to_add.add_team(t)

                    team_member_name = row[1]
                    team_member_email = row[2]

                    # loop over the team_added_tracker and match the team member to their correct team and add them
                    for tm in team_added_tracker:
                        if tm.name == team_in:
                            tmember = TeamMember(self._last_oid, team_member_name, team_member_email)
                            tm.add_member(tmember)
                            self.next_oid()

            # add league to the database object
            self.add_league(league_to_add)

        except FileNotFoundError:
            print("Error while importing - file was not found.")

        except DuplicateEmail:
            print("File contains two team members with the same email address.")

    def export_league(self, league, file_name):
        """
        Create export_league method to export an existing league in the database to a CSV file.
        :param league:
        :param file_name:
        """
        found_flag = False
        found_league = None
        for lg in self._leagues:
            if league == lg.name:
                found_flag = True
                found_league = lg
                break
        if found_flag:
            try:
                with open(file_name, mode="w", encoding="utf-8", newline="") as csvfile:
                    rowwriter = csv.writer(csvfile, delimiter=',')
                    first_row = ["Team Name", "Member Name", "Member Email"]
                    rowwriter.writerow(first_row)
                    for tm in found_league.teams:
                        for tmember in tm.members:
                            team_member_row = [tm.name, tmember.name, tmember.email]
                            rowwriter.writerow(team_member_row)

            except IOError:
                print("Error occurred while writing.")
        else:
            print("League not found")
