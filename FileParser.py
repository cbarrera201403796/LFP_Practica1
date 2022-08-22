from Course import Course
from Error import Error
from ParsedData import ParsedData
from Prerequisite import Prerequisite
import re

class FileParser:

    def __init__(self, file_location=None):
        self.__file_location = file_location
        self.code_pattern = re.compile("\\d+")
        self.name_pattern = re.compile("[A-Za-z0-9\\s]+")
        self.prerequisite_pattern = re.compile("\\d+")
        self.is_required_pattern = re.compile("1|0")
        self.status_pattern = re.compile("-?1|0")
        self.semester_pattern = re.compile("\\d+")
        self.points_pattern = re.compile("\\d+")

    @property
    def file_location(self):
        return self.__file_location

    @file_location.setter
    def file_location(self, value):
        self.__file_location = value

    @file_location.deleter
    def file_location(self):
        del self.__file_location

    def parse_file(self):

        parsed_data = []
        error_data = []
        if self.__file_location is None:
            print("Debe indicar un archivo")
        else:
            file = open(self.__file_location, 'r+')
            file_lines = file.readlines()
            index = 1
            for line in file_lines:

                separated_data = line.rstrip("\n").split(",")
                separated_data_size = len(separated_data)
                if separated_data_size < 7 or separated_data_size > 7:
                    print("Error, datos inválidos en la línea: \n", index)
                else:

                    t_code = separated_data[0].lstrip()
                    t_name = separated_data[1].lstrip()
                    t_prerequisites = []
                    t_is_required = separated_data[3].lstrip()
                    t_semester = separated_data[4].lstrip()
                    t_points = separated_data[5].lstrip()
                    t_status = separated_data[6].lstrip()

                   # print("STATUS RAW", t_status)
                   # print("SEMESTER RAW", t_semester)

                    found_code_issue = not self.code_pattern.match(t_code)
                    if found_code_issue:
                        error_data.append(Error("Formato de código incorrecto", index))
                    found_name_issue = not self.name_pattern.match(t_name)

                    if found_name_issue:
                        error_data.append(Error("Formato de nombre incorrecto", index))
                    found_is_required_issue = not self.is_required_pattern.match(t_is_required)

                    if found_is_required_issue:
                        error_data.append(Error("Formato de obligatorio incorrecto", index))
                    found_semester_issue = not self.semester_pattern.match(t_semester)

                    if found_semester_issue:
                        error_data.append(Error("Formato de semestre incorrecto", index))
                    found_points_issue = not self.points_pattern.match(t_points)

                    if found_points_issue:
                        error_data.append(Error("Formato de créditos incorrecto", index))

                    found_status_issue = not self.status_pattern.match(t_status)
                    if found_status_issue:
                        error_data.append(Error("Formato de estado incorrecto", index))

                    t_separated_pre_requisites = separated_data[2].rstrip("\n").rstrip(" ").lstrip().split(";")
                    #print(t_separated_pre_requisites)
                    found_prerequisites_issues = False
                    if len(t_separated_pre_requisites) > 1:
                        for t_course_code in t_separated_pre_requisites:
                            if t_course_code.isnumeric():
                                t_prerequisites.append(Prerequisite(t_course_code))
                            else:
                                found_prerequisites_issues = True
                    elif len(t_separated_pre_requisites) == 1:
                        if t_separated_pre_requisites[0].isnumeric():
                            t_prerequisites.append(Prerequisite(t_separated_pre_requisites[0]))
                        elif not t_separated_pre_requisites[0].isnumeric() and len(t_separated_pre_requisites[0]) > 0:
                            found_prerequisites_issues = True

                    if found_prerequisites_issues:
                        error_data.append(Error("Formato de pre-requisitos incorrecto", index))
                    tmp_course = Course(t_code, t_name, t_prerequisites, t_is_required, t_status, t_semester,
                                        t_points)
                    parsed_data.append(tmp_course)

                index = index + 1
        return ParsedData(parsed_data, error_data)


#parser = FileParser("tester2.lpf")

#parsed_data_1 = parser.parse_file()

#if len(parsed_data_1.errors) > 0:
#    print("Hay errores en el archivo")
#    for error in parsed_data_1.errors:
#        print("Línea", error.line)
#        print("Descripción", error.description)

#else:
#    for parse in parsed_data_1.data:
#        print("Código de curso:", parse.code)
#        print("Nombre de curso:", parse.name)
#        print("Prerequisitos:", parse.prerequisites)
#        print("Es obligatorio?:", parse.is_required)
#        print("Estado de curso:", parse.status)
#        print("Semestre:", parse.semester)
#        print("Creditos:", parse.points)
#        print("________________________________\n")
