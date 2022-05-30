import re


class Constraint:
    def __init__(self, command):
        self.command = command
        self.obj_data_dir = self._parse_command()

    def _parse_command(self):
        #'ALTER TABLE visual_check.check_package DROP CONSTRAINT ck_checkpack_status;'
        table = re.match('ALTER TABLE ([a-zA-Z._]+)', self.command)
        constraint =re.match('CONSTRAINT ([a-zA-Z._]+)', self.command)
        operation = re.match('(\w+) CONSTRAINT', self.command)