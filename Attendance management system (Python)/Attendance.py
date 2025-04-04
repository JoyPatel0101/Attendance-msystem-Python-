# date | faculty_name | batch | subject | roll_number | student_name | status

class Attendance:
    attendance = []

    def __init__(self,date,faculty_name,batch,subject,roll_number,student_name,status):
        self.date = date
        self.faculty_name = faculty_name
        self.batch = batch 
        self.subject = subject 
        self.roll_number = roll_number 
        self.student_name = student_name
        self.status = status
        Attendance.attendance.append(self)
        self.storing_attendance_data()
        
    def __str__(self):
        return f"{self.date}|{self.faculty_name}|{self.batch}|{self.subject}|{self.roll_number}|{self.student_name}|{self.status}"
        
    def storing_attendance_data(self):
        with open("Attendance.txt",'a') as attendance_file:
            attendance_file.seek(0,2)
            attendance_file.write(str(Attendance.attendance[-1]) + "\n")