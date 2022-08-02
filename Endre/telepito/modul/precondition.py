from modul.presqlcheck import PreSqlCheck


class Precondition:
    on_fail_list = ["HALT", "CONTINUE", "MARK_RAN", "WARN"]
    on_error_list = on_fail_list

    def __init__(self):
        print("Precondition init")
        self._on_fail = str()
        self._on_error = str()
        self._sql_check = PreSqlCheck()

    # -- on_fail --
    @property
    def on_fail(self):
        return self._on_fail

    @on_fail.setter
    def on_fail(self, value):
        if value in Precondition.on_fail_list:
            self._on_fail = value
        else:
            print("Hibás on_fail adat!")

    # -- on_error --
    @property
    def on_error(self):
        return self._on_error

    @on_error.setter
    def on_error(self, value):
        if value in Precondition.on_error_list:
            self._on_error = value
        else:
            print("Hibás on_error adat!")

    # -- sql_check --
    @property
    def sql_check(self):
        return self._sql_check

    @sql_check.setter
    def sql_check(self, value):
        self._sql_check = value
