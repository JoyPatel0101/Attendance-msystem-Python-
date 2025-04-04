# faculty_id first_name middle_name last_name username password *subject
class Faculty:
    faculty = []
    def __init__(self,fname,mname,lname,favourite_number,password,*sub):
        self.faculty_id = self.generateId()
        self.first_name = fname
        self.middle_name = mname
        self.last_name = lname
        self.username = fname[0:5].lower() + str(favourite_number).zfill(4)
        self.password = password
        self.subject = sub
        Faculty.faculty.append(self)
        self.storing_faculty_data()
        
    def generateId(self):
        try:
            with open("Faculty.txt",'r') as faculty_file:
                data = faculty_file.readlines()
                id=-1
                if(data):
                    last_id = int(data[-1].split()[0])
                    # print(last_id)
                    id = last_id+1
                else:
                    id = 0
                    # print("File is empty")
                return id
        except(FileNotFoundError):
            return 0
        
    def __str__(self):
        for sub in self.subject:
            subjects = ",".join(sub)
        
        return f"{self.faculty_id} {self.first_name} {self.middle_name} {self.last_name} {self.username} {self.password} {subjects}"
    
    def storing_faculty_data(self):
        print(str(Faculty.faculty[-1])) 
        with open("Faculty.txt",'a') as faculty_file:
            faculty_file.seek(0,2)
            faculty_file.write(str(Faculty.faculty[-1]) + "\n")
        print(f"Your generated user-name is '{self.username}'.")
