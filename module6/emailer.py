import yagmail
import keyring


class Emailer:
    """
    Create Emailer class to send emails.
    """
    sender_address = None
    _sole_instance = None

    @classmethod
    def instance(cls):
        """
        Create instance class method to instantiate the class.
        :return: cls._sole_instance
        """
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance

    @classmethod
    def configure(cls, sender_address):
        """
        Create configure class method to configure the Emailer sender address.
        :param sender_address:
        """
        Emailer.sender_address = sender_address

    def send_plain_email(self, recipients, subject, message):
        """
        Create send_plain_email method to send out an email to a list of recipients.
        :param recipients:
        :param subject:
        :param message:
        """
        recipient_list = recipients
        subject_out = subject
        message_out = message
        yag_smtp_connection = yagmail.SMTP(user=Emailer.sender_address)
        yag_smtp_connection.send(to=recipient_list, subject=subject_out, contents=message_out)


if __name__ == '__main__':
    # I used the command line to set my keyring password
    a = Emailer.instance()
    Emailer.configure("pythonclassemailtest@gmail.com")
    a.send_plain_email(["jeffreyalankohl89@gmail.com"], "Practice", "Success")
