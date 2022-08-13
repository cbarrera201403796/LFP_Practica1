class ParsedData:

    def __init__(self, data=None, errors=None):
        self.__data = data
        self.__errors = errors

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @data.deleter
    def data(self):
        del self.__data

    @property
    def errors(self):
        return self.__errors

    @errors.setter
    def errors(self, value):
        self.__errors = value

    @errors.deleter
    def errors(self):
        del self.__errors

