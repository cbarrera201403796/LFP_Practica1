class Prerequisite:
    def __init__(self, code=None):
        self._code = code

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @code.deleter
    def code(self):
        del self._code

