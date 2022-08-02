from modul.changeset_header import ChangeSetHeader
from modul.precondition import Precondition
from modul.comment import Comment


class ChangeSet:

    def __init__(self):
        self._header = ChangeSetHeader()
        self._precondition = Precondition()
        self._comment = Comment()

    def __str__(self):
        return f"{self.header.__str__()} , {self.precondition.__str__()} , {self.comment.__str__()}"

    # -- header --
    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, value):
        self._header = value

    # -- precondition --
    @property
    def precondition(self):
        return self._precondition

    @precondition.setter
    def precondition(self, value):
        self._precondition = value

    # -- comment --
    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value
