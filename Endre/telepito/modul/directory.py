from modul.base_obj import BaseObj
from modul.file import File


class Dir(BaseObj):

    def __init__(self, name, parent_id=None):
        obj_id = 0 if parent_id == 0 else None
        print(obj_id)
        super().__init__(name=name, parent_id=parent_id, obj_id=obj_id, type="D")
        self._files = list()
        self._dirs = list()

    # -- files --
    @property
    def files(self):
        return self._files

    def add_file(self, name):
        self._files.append(self._add_obj(value, File))

    # -- dirs --
    @property
    def dirs(self):
        return self._dirs

    def add_dir(self, value):
        self._dirs.append(self._add_obj(value, Dir))

    # -- tools --
    def _add_obj(self, value, objClass):
        if isinstance(value, objClass):
            new_obj = value
            new_obj.parent_id = self.obj_id
        elif isinstance(value, str):
            new_obj = objClass(name=value, parent_id=self.obj_id)
        else:
            raise Exception("Sikertelen objektum létrehozás, nem megfelelő az objektum típusa!")

        return new_obj

    # -- all_obj --
    @property
    def all_obj(self):
        ret = self._dirs
        ret.extend(self._files)
        return ret
