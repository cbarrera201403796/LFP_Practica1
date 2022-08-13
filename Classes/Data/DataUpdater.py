class DataUpdater:
    def __init__(self, all_courses=None, new_courses=None):
        self.__all_courses = all_courses
        self.__new_courses = new_courses

    @property
    def all_courses(self):
        return self.__all_courses

    @all_courses.setter
    def all_courses(self, value):
        self.__all_courses = value

    @all_courses.deleter
    def all_courses(self):
        del self.__all_courses

    def add_courses(self, course_list):
        for new_course in course_list:
            found_course = False
            for index, course in enumerate(self.__all_courses):
                if course.code == new_course.code:
                    self.__all_courses[index] = new_course
                    found_course = True

            if not found_course:
                self.__all_courses.append(new_course)
        return self.__all_courses

    def add_single_course(self, new_course):
        found_course = False
        for index, course in enumerate(self.__all_courses):
            if course.code == new_course.code:
                self.__all_courses[index] = new_course
                found_course = True

        if not found_course:
            self.__all_courses.append(new_course)

        return self.__all_courses
