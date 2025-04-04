# subject_index subject
class Subject:
    subject=[]
    def __init__(self,subject):
        self.subject_id = self.generateId()
        self.subject = subject
        Subject.subject.append(self)
        self.storing_subject_data()
        
    def generateId(self):
        try: 
            with open("Subject.txt",'r') as subject_file:
                data = subject_file.readlines()
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
        return f"{self.subject_id} {self.subject}"
    
        
    def storing_subject_data(self):
        with open("Subject.txt",'a') as subject_file:
            subject_file.seek(0,2)
            subject_file.write(str(Subject.subject[-1]) + "\n")