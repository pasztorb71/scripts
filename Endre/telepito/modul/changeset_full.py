class ChangeSet:

    def __init__(self):
        self._author = str()
        self._changeset_id = str()
        self._run_on_change = bool()
        self._dbms = str()
        self._fail_on_error = bool()
        self._strip_comments = bool()
        self._context = str()
        self._labels = str()
        self._comment = str()
        self._expected_result_num = int()
        self._sql_check = str()

    # -- author --
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    # -- changeset_id --
    @property
    def changeset_id(self):
        return self._changeset_id

    @changeset_id.setter
    def changeset_id(self, value):
        self._changeset_id = value

    # -- run_on_change --
    @property
    def run_on_change(self):
        return self._run_on_change

    @run_on_change.setter
    def run_on_change(self, value):
        self._run_on_change = value

    # -- dbms --
    @property
    def dbms(self):
        return self._dbms

    @dbms.setter
    def dbms(self, value):
        self._dbms = value

    # -- fail_on_error --
    @property
    def fail_on_error(self):
        return self._fail_on_error

    @fail_on_error.setter
    def fail_on_error(self, value):
        self._fail_on_error = value

    # -- strip_comments --
    @property
    def strip_comments(self):
        return self._strip_comments

    @strip_comments.setter
    def strip_comments(self, value):
        self._strip_comments = value

    # -- context --
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        self._context = value

    # -- labels --
    @property
    def labels(self):
        return self._labels

    @labels.setter
    def labels(self, value):
        self._labels = value

    # -- comment --
    @property
    def comment(self):
        return self._comment


    @comment.setter
    def comment(self, value):
        self._comment = value

    # -- expected_result_num --
    @property
    def expected_result_num(self):
        return self._expected_result_num

    @expected_result_num.setter
    def expected_result_num(self, value):
        self._expected_result_num = value

    # -- sql_check --
    @property
    def sql_check(self):
        return self._sql_check

    @sql_check.setter
    def sql_check(self, value):
        self._sql_check = value
