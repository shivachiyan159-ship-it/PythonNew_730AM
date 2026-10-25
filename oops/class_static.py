class Student:
    # attributes
    # instance attributes
    # class attributes
    # methods
    # instance methods
    # class method
    # static method

    college_name = "CBIT"  # 2 bytes

    def __init__(self, name, rollnum):
        self.name = name  # 2 bytes
        self.rollnum = rollnum  # 2 bytes
        self.marks=590
        # self.collegenmae = collegename

    def dispaly_info(self):  # srikanthobj
        print(
            f"student name is {self.name} and ronnum is {self.rollnum} and my college name is {Student.college_name}")

    @classmethod
    def change_name(cls, newname):  # Student
        cls.college_name = newname

    @staticmethod
    def average(a, b):
        return a/b


srikanthobj = Student("srikanth", 1)
# print(srikanthobj.name)  # 2 bytes
# print(srikanthobj.rollnum)  # 2 bytes
# print(Student.college_name)  # 2 bytes
srikanthobj.dispaly_info()


Student.change_name("CBIT New")
praveenobj = Student("praveen", 2)
# print(praveenobj.name)  # 2 bytes
# print(praveenobj.rollnum)  # 2 bytes
# print(Student.college_name)  # 2 bytes
praveenobj.dispaly_info()


likithaobj = Student("likitha", 3)
# print(likithaobj.name)  # 2 bytes
# print(likithaobj.rollnum)  # 2 bytes
# print(Student.college_name)  # 2 bytes
likithaobj.dispaly_info()
salary = likithaobj.salary
totalmarks=likithaobj.marks
print(Student.average(totalmarks, 6))

# 4*3= 12 bytes + 2 bytes = 14 bytes
