from modul.base_text import BaseText


class PreSqlCheck(BaseText):

    def __init__(self):
        super().__init__()
        print("PreSqlCheck init")
        self._expected_result_num = int()

    # -- expected_result_num --
    @property
    def expected_result_num(self):
        return self._expected_result_num

    @expected_result_num.setter
    def expected_result_num(self, value):
        self._expected_result_num = value
