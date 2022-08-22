from FileParser import FileParser
from SemesterSummary import SemesterSummary


class DataHandler:
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
        found_course_new = False
        courses_list_size = len(self.__all_courses)
        index = 0
        while not found_course_new and index < courses_list_size:
            course = self.__all_courses[index]
            if course.code == new_course.code:
                self.__all_courses[index] = new_course
                found_course_new = True
            index += 1

        if not found_course_new:
            self.__all_courses.append(new_course)

        return self.__all_courses

    def edit_course(self, course_edit):
        found_course_edit = False
        courses_list_size = len(self.__all_courses)
        index = 0
        while not found_course_edit and index < courses_list_size:
            course = self.__all_courses[index]
            if course.code == course_edit.code:
                self.__all_courses[index] = course_edit
                found_course_edit = True
            index += 1
        return self.__all_courses

    def delete_course(self, course_delete):
        found_course_delete = False
        courses_list_size = len(self.__all_courses)
        index = 0
        while not found_course_delete and index < courses_list_size:
            course = self.__all_courses[index]
            if course.code == course_delete.code:
                self.__all_courses.pop(index)
                found_course_delete = True
            index += 1
        return self.__all_courses

    def sum_credits(self, semester):
        total_credits = 0
        for course in self.__all_courses:
            if int(course.semester) <= int(semester) and int(course.is_required) == 1:
                # print('semestre', course.semester)
                # print('Creditos', course.points)
                total_credits += int(course.points)
                # print('Suma', total_credits)
                # print('___________________________')
        return total_credits

    def sum_approved_credits(self):
        total_approved_credits = 0
        for course in self.__all_courses:
            if int(course.status) == 0:
                total_approved_credits += int(course.points)

        return total_approved_credits

    def count_current_courses_credits(self):
        total_current_courses_credits = 0
        for course in self.__all_courses:
            if int(course.status) == 1:
                total_current_courses_credits += int(course.points)

        return total_current_courses_credits

    def count_pending_courses_credits(self):
        total_current_courses_credits = 0
        for course in self.__all_courses:
            if int(course.status) == -1 and int(course.is_required) == 1:
                total_current_courses_credits += int(course.points)

        return total_current_courses_credits

    def get_semester_data(self, p_semester):
        return_data = SemesterSummary()
        passed_courses_total = 0
        assigned_courses_total = 0
        pending_credits_total = 0

        for course in self.__all_courses:
            if int(course.semester) == p_semester:
                if course.status == "0":
                    passed_courses_total += int(course.points)
                elif course.status == "1":
                    assigned_courses_total += int(course.points)
                elif course.status == "-1":
                    pending_credits_total += int(course.points)

        return_data.approved = passed_courses_total
        return_data.coursing = assigned_courses_total
        return_data.pending = pending_credits_total

        return return_data


# dataHandler = DataHandler(all_courses=FileParser("tester2.lpf").parse_file().data)
# print('Créditos aprobados', dataHandler.sum_approved_credits())
# print('Suma Creditos Semestre', dataHandler.sum_credits(semester=2))

# semester = 1

# print('Creditos de de semestre Pendientes', dataHandler.get_semester_data(p_semester=semester).pending)
# print('Creditos de de semestre Cursando', dataHandler.get_semester_data(p_semester=semester).coursing)
# print('Creditos de de semestre Aprobados', dataHandler.get_semester_data(p_semester=semester).approved)

