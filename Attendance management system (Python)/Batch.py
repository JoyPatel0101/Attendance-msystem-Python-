# batch_name
class Batch:
    batch=[]
    def __init__(self,name):
        self.batch_name = name
        Batch.batch.append(self)
        self.storing_batch_data()
    
    def __str__(self):
        return f"{self.batch_name}"
    
    def storing_batch_data(self):
        with open("Batch.txt",'a') as batch_file:
            batch_file.seek(0,2)
            batch_file.write(str(Batch.batch[-1]) + "\n")