class DuplicateOid(Exception):
    """
    Create DuplicateOid class.
    """
    def __init__(self, oid):
        super().__init__()
        self.oid = oid


class DuplicateEmail(Exception):
    """
    Create DuplicateEmail class.
    """
    def __init__(self, email):
        super().__init__()
        self.email = email
