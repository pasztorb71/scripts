class BaseText:

    def __init__(self):
        print("BaseText init")
        self._text = str()

    # -- text --
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
