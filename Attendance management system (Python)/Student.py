# student_id first_name middle_name last_name course_name batch_name roll_number
# A1-7 A2-8 B1-4
class Student:
    student=[]
    def __init__(self,fname,mname,lname,cn,bn,rn):
        self.student_id=self.generateId()
        self.first_name=fname
        self.middle_name=mname
        self.last_name=lname
        self.course_name=cn
        self.batch_name=bn
        self.roll_number=rn
        Student.student.append(self)
        self.stroing_student_data()

    def generateId(self):
        try: 
            with open("Student.txt",'r') as student_file:
                data = student_file.readlines()
                id=-1
                if(data):
                    last_id = int(data[-1].split()[0])
                    id = last_id+1
                else:
                    id = 0
                return id
        except(FileNotFoundError):
            return 0

    def __str__(self):
        return f"{self.student_id} {self.first_name} {self.middle_name} {self.last_name} {self.course_name} {self.batch_name} {self.roll_number}"

    def stroing_student_data(self):
        print(str(Student.student[-1]))
        with open("Student.txt",'a') as student_file:
            student_file.seek(0,2)
            student_file.write(str(Student.student[-1]) + "\n")
