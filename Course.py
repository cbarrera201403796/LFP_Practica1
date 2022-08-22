class Course:

    def __init__(self,
                 code=None,
                 name=None,
                 prerequisites=None,
                 is_required=None,
                 status=None,
                 semester=None,
                 points=None):
        self._code = code
        self._name = name
        self._prerequisites = prerequisites
        self._is_required = is_required
        self._status = status
        self._semester = semester
        self._points = points

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @code.deleter
    def code(self):
        del self._code

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    @property
    def prerequisites(self):
        return self._prerequisites

    @prerequisites.setter
    def prerequisites(self, value):
        self._prerequisites = value

    @prerequisites.deleter
    def prerequisites(self):
        del self._prerequisites

    @property
    def is_required(self):
        return self._is_required

    @is_required.setter
    def is_required(self, value):
        self._prerequisites = value

    @is_required.deleter
    def is_required(self):
        del self._prerequisites

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        self._points = value

    @points.deleter
    def points(self):
        del self.points

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @status.deleter
    def status(self):
        del self._status

    @property
    def semester(self):
        return self._semester

    @semester.setter
    def semester(self, value):
        self._semester = value

    @semester.deleter
    def semester(self):
        del self._semester

