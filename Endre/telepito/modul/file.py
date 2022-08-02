from modul.base_obj import BaseObj


class File(BaseObj):

    def __init__(self, name, parent_id=None):
        super().__init__(name=name, parent_id=parent_id, type="F")
