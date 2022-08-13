class Error:

    def __init__(self, description=None, line=None):
        self.__description = description
        self.__line = line

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @description.deleter
    def description(self):
        del self.__description

    @property
    def line(self):
        return self.__line

    @line.setter
    def line(self, value):
        self.__line = value

    @line.deleter
    def line(self):
        del self.__line
