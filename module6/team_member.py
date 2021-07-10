from module6.identified_object import IdentifiedObject
from module6.emailer import Emailer


class TeamMember(IdentifiedObject):
    """
    Create a team member class that gives each team member a name and email address.
    """
    def __init__(self, oid, name, email):
        super().__init__(oid)
        self._name = name
        self._email = email

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
        if name is not None:
            self._name = name

    @property
    def email(self):
        """
        Create email property.
        :return: self._email
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Create email setter.
        :param email:
        """
        self._email = email

    def send_email(self, emailer, subject, message):
        """
        Create send_email method.
        :param emailer:
        :param subject:
        :param message:
        :return: self._email
        """
        emailer.send_plain_email([self._email], subject, message)
        return self._email

    def __str__(self):
        """
        Override str
        :return: formatted string with name and email
        """
        capital_name = self.name.title()
        capital_email = self.email.title()
        return f"{capital_name}<{capital_email}>"


if __name__ == '__main__':
    a = TeamMember(1, "Jeff Kohl", "jeffreyalankohl89@gmail.com")
    b = Emailer()
    b.configure("pythonclassemailtest@gmail.com")
    a.send_email(b, "Hello", "It worked!")
