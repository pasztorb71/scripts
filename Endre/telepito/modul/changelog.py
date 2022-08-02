class ChangeLog:

    def __init__(self):
        self._changeset_list = list()

    def add_chagset(self, changeset):
        self._changeset_list.extend(changeset)
        # return self._changeset_list
