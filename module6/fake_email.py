

class FakeEmailer:
    """
    Create FakeEmailer class.
    """
    def __init__(self):
        self.recipients = None
        self.subject = None
        self.message = None
        self.messages = []

    def send_plain_email(self, recipients, subject, message):
        """
        Create send_plain_email to mimic sending an email.
        :param recipients:
        :param subject:
        :param message:
        :return:
        """
        self.recipients = recipients
        self.subject = subject
        self.message = message

        for recipient in recipients:
            print(f"Sending mail to: {recipient}")
        self.messages.append((recipients, subject, message))
