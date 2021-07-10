from module6.identified_object import IdentifiedObject
from module6.team_member import TeamMember
from module6.emailer import Emailer
from module6.team import Team


class Competition(IdentifiedObject):
    """
    Create Competition class.
    """
    def __init__(self, oid, teams, location, datetime):
        super().__init__(oid)
        self._teams_competing = teams
        self._location = location
        self._date_time = datetime

    @property
    def teams_competing(self):
        """
        Create teams_competing property.
        :return: self._teams_competing
        """
        return self._teams_competing

    @property
    def date_time(self):
        """
        Create date_time property
        :return: self._date_time
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """
        Create date_time setter.
        :param date_time:
        """
        self._date_time = date_time

    @property
    def location(self):
        """
        Create location property
        :return: self._location
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Create location setter.
        :param location:
        """
        self._location = location

    def send_email(self, emailer, subject, message):
        """
        Create send_email method to send an email to all competition participants.
        :param emailer:
        :param subject:
        :param message:
        :return: A set of unique email addresses.
        """
        # get teams playing in the competition
        team_list = self.teams_competing

        # add all the players from the first team into a list
        team_members = []
        for tm in team_list[0].members:
            team_members.append(tm)

        # add all the players from the second team into a list
        for tm in team_list[1].members:
            team_members.append(tm)

        # remove the duplicate players from the list with players from both teams
        team_members_no_duplicates = []
        for tm in team_members:
            flag = False
            a = tm.oid
            b = tm.name
            c = tm.email
            if len(team_members_no_duplicates) == 0:
                team_members_no_duplicates.append(tm)
            else:
                for tmnd in team_members_no_duplicates:
                    d = tmnd.oid
                    e = tmnd.name
                    f = tmnd.email
                    if (a == d) and (b == e) and (c == f):
                        flag = True
                    else:
                        continue
                if not flag:
                    team_members_no_duplicates.append(tm)

        # create a list of the emails using the unique player list for players in the competition
        unique_team_members_emails = [tmember.email for tmember in team_members_no_duplicates]

        # call the send_plain_email method on the emailer object and pass in the unique email list as a parameter
        emailer.send_plain_email(unique_team_members_emails, subject, message)

        return set(unique_team_members_emails)

    def __str__(self):
        """
        Override str.
        :return: Formatted string with location and number of teams.  Date and time may be included.
        """
        length_teams = len(self._teams_competing)
        if self.date_time is None:
            return f"Competition at {self.location} with {length_teams} teams"
        else:
            return f"Competition at {self.location} on {self.date_time} with {length_teams} teams"


if __name__ == '__main__':
    t1 = TeamMember(1, "Jeff Kohl", "jeffreyalankohl89@gmail.com")
    t2 = TeamMember(2, "Jeff Kohl 2", "jak0097@auburn.edu")
    team1 = Team(1, "Team 1")
    team2 = Team(2, "Team 2")
    team1.add_member(t1)
    team2.add_member(t2)
    team2.add_member(t1)
    comp = Competition(1, [team1, team2], "Here", None)
    em = Emailer()
    em.configure("pythonclassemailtest@gmail.com")
    comp.send_email(em, "Competition Test", "Success")
