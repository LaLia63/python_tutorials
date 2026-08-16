# Typecasting = the process of converting a variable from one data type to another 
#                        str(), int(), float(), bool()

name = "Hsu Yati Zaw" #if not have data in it it become false
age = 21
gpa = 3.5
is_student = True

gpa = int(gpa)
# age = float(age)
is_student = str(is_student)
age = str(age)

age += "1"

name = bool(name)

type(name)
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))
# print(age)
print(name)
