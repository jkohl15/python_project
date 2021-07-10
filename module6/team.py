from module6.identified_object import IdentifiedObject
from module6.custom_exceptions import DuplicateOid
from module6.custom_exceptions import DuplicateEmail
from module6.team_member import TeamMember
from module6.emailer import Emailer


class Team(IdentifiedObject):
    """
    Create Team class.
    """
    def __init__(self, oid, name):
        super().__init__(oid)
        self._name = name
        self._members = []

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
        Create setter.
        :param name:
        """
        if name is not None:
            self._name = name

    @property
    def members(self):
        """
        Create members property.
        :return: self._members
        """
        return self._members

    def add_member(self, member):
        """
        Create add_member method to add a team member to a team
        :param member:
        """
        if len(self.members) == 0:
            self.members.append(member)
        else:
            for tm in self.members:
                if tm.oid == member.oid:
                    raise DuplicateOid(member.oid)
                elif tm.email.lower() == member.email.lower():
                    raise DuplicateEmail(member.email)
            self.members.append(member)

    def remove_member(self, member):
        """
        Create remove_member method to remove a team member from a team
        :param member:
        :return:
        """
        if member in self.members:
            self.members.remove(member)
        else:
            return

    def send_email(self, emailer, subject, message):
        """
        Create send_email method to send an email to all team members.
        :param emailer:
        :param subject:
        :param message:
        :return: list of all team member email addresses on a team.
        """
        emailer.send_plain_email([tm.email for tm in self.members], subject, message)
        return [tm.email for tm in self.members]

    def __str__(self):
        """
        Override str.
        :return: Formatted string with name and number of team members on the team.
        """
        capitalized_name = self.name.title()
        number_of_team_members = len(self.members)
        return f"Team {capitalized_name}: {number_of_team_members} members"

if __name__ == '__main__':
    t1 = TeamMember(1, "Jeff Kohl", "jeffreyalankohl89@gmail.com")
    t2 = TeamMember(2, "Jeff Kohl 2", "jak0097@auburn.edu")
    team1 = Team(1, "Team 1")
    team1.add_member(t1)
    team1.add_member(t2)
    em = Emailer()
    em.configure("pythonclassemailtest@gmail.com")
    team1.send_email(em, "Team Test", "Success.")
