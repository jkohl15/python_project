class IdentifiedObject:
    """
    Create IdentifiedObject class that will be used for team members, teams, competitions, and leagues.
    """

    def __init__(self, oid):
        super().__init__()
        self._oid = oid

    @property
    def oid(self):
        """
        Create OID property.
        :return: self._oid
        """
        return self._oid

    def __eq__(self, other):
        """
        Create __eq__ method for equality.
        :param other:
        :return: true or false depending on equality
        """
        if self is other:
            return True
        if hasattr(other, "_oid"):
            return self._oid == other.oid and type(self) == type(other)
        else:
            return False

    def __hash__(self):
        """
        Create hash method.
        :return: hash(self._oid)
        """
        return hash(self._oid)


