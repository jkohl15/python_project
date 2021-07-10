from module6.identified_object import IdentifiedObject
from module6.custom_exceptions import DuplicateOid


class League(IdentifiedObject):
    """
    Create League class.
    """
    def __init__(self, oid, name):
        super().__init__(oid)
        self._name = name
        self._teams = []
        self._competitions = []

    @property
    def teams(self):
        """
        Create teams property.
        :return: self._teams
        """
        return self._teams

    @property
    def competitions(self):
        """
        Create competitions property
        :return: self._competitions
        """
        return self._competitions

    @property
    def name(self):
        """
        Create name property.
        :return: self._name
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Create name setter.
        :param name:
        """
        self._name = name

    def add_team(self, team):
        """
        Create add_team method to add a team to the league.
        :param team:
        """
        if len(self.teams) == 0:
            self._teams.append(team)
        else:
            for team_in_list in self.teams:
                if team_in_list.oid == team.oid:
                    raise DuplicateOid(team.oid)
            self._teams.append(team)

    # Jeff added this 7.2.2021
    def delete_team(self, index):
        """
        Crate delete_team method to remove a team from the league.
        :param index:
        """
        del self._teams[index]

    def add_competition(self, competition):
        """
        Create add_competition method to add a competition to the leadue.
        :param competition:
        """
        if len(self.competitions) == 0:
            self._competitions.append(competition)
        else:
            for comp in self.competitions:
                if comp.oid == competition.oid:
                    raise DuplicateOid(competition.oid)
            self.competitions.append(competition)

    def teams_for_member(self, member):
        """
        Create teams_for_member method to identify which teams a member is playing for.
        :param member:
        :return: returned_list
        """
        returned_list = [t for t in self.teams if member in t.members]
        return returned_list

    def competitions_for_team(self, team):
        """
        Create competitions_for_team method to identify which competitions a team is playing in.
        :param team:
        :return: returned_set
        """
        returned_set = {comp for comp in self.competitions if
                        comp.teams_competing[0] == team or comp.teams_competing[1] == team}

        return returned_set

    def competitions_for_member(self, member):
        """
        Create competitions_for_member method to identify which competitions a team member is playing in.
        :param member:
        :return: returned_set
        """
        returned_set = {comp for comp in self.competitions if
                        (member in comp.teams_competing[0].members)
                        or (member in comp.teams_competing[1].members)}
        return returned_set

    def __str__(self):
        """
        Override str.
        :return: Formatted string with team name, number of teams, and number of competitions for that team.
        """
        number_of_teams = len(self._teams)
        number_of_competitions = len(self._competitions)
        return f"League {self.name.title()}: {number_of_teams} teams, {number_of_competitions} competitions"
