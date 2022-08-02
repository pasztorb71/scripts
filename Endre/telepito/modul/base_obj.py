class BaseObj:

    def __init__(self, name, type, parent_id=None, obj_id=None):
        self._name = name
        self._type = type
        self._parent_id = parent_id
        self._obj_id = obj_id if obj_id else self._gen_obj_id()

    def __str__(self):
        return f":{self._name}({self._type})"

    # -- name --
    @property
    def name(self):
        return self._name

    # @name.setter
    # def name(self, value):
    #     self._name = value

    # -- type --
    @property
    def type(self):
        return self._type

    # @type.setter
    # def type(self, value):
    #     self._type = value

    # -- parent_id --
    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, value):
        self._parent_id = value

    # -- obj_id --
    @property
    def obj_id(self):
        return self._obj_id

    @obj_id.setter
    def obj_id(self, value):
        self._obj_id = value

    # default érték generálása
    def _gen_obj_id(self):
        return id(self)
