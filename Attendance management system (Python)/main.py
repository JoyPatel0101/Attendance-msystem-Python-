import Faculty,Student,Batch,Subject,Attendance
import re,time
import pywhatkit as kit
import pyautogui
from datetime import datetime,date
from tabulate import tabulate 

flag = True
while(flag):
    print("\n\n------------------------------------")
    print("--Welcome to Attendance Management--")
    print("------------------------------------")
    print("1 : Manage Attendance.")
    print("2 : Add new Faculty.")
    print("3 : Add new Student.")
    print("4 : Add new Batch.")
    print("5 : Show Attendance.")
    
    print("0 : EXIT")
    choice = 0
    try:
        choice = int(input("Enter your choice : "))
    except ValueError:
        print("Enter only 1 to 5 integer numbers only.")
        
    if(choice>=0 and choice<=5):
        if(choice == 0):
            print("Exiting",end="")
            for i in range(3):
                print(".",end="")
                time.sleep(0.7)

        elif(choice==1):
            isValidUser = False
            faculty = []   # details of login facutly
            faculties = []
            
            try:
                with open("Faculty.txt",'r') as faculty_file:
                    data = faculty_file.readlines()
                    
                    for fac in data:
                        faculties.append(fac.split())
                        
            except FileNotFoundError:
                print("Faculty data not found.")
                
            count = 0 
            un = False
            pw = False
            username = ""
            password = ""
            while((not isValidUser) and (count!=3)):   # (True)and(True)
                count += 1
                if(un==False):
                    username = input("Enter Username : ")
                    password = input("Enter Password : ")
                elif(un==True):
                    password = input("Enter Password : ")
                    
                # Verification of username and password are right or not?
                for fac in faculties:
                    if(fac[4] == username):
                        un = True
                        if(fac[5] == password):
                            pw = True
                            isValidUser = True
                            faculty = fac
                            break
                        break
                
                # What is the wrong that's checking.
                if(not isValidUser):
                    if(count != 3):
                        if(not un):
                            print("Invalid Username.")
                            print("Re-enter Username & Password...")
                        elif(not pw):
                            print("Invalid Password")
                            print("Re-enter Password...")
                    else:
                        print("You are lose maximum chances of login.")
                        
            # User is login or not?
            if(isValidUser):
                print(f"\n-- {username} successfully logined --")
                isLogin = ""
                while(isLogin != "EXIT"):
                    
                    # Manage Attendance
                    print("\nEnter date for attendance(today or yyyy-mm-dd).")
                   
                    # Get Date.
                    isValidDate = False
                    dt = None
                    while(not isValidDate):
                        choice = input("Enter Date : ").lower()
                        if(choice == "today"):
                            dt = date.today()
                            isValidDate = True
                        else:
                            date_format = "%Y-%m-%d"
                            try:
                                choice = datetime.strptime(choice,date_format).date()
                                if choice <= date.today():
                                    dt = choice
                                    isValidDate = True
                                else:
                                    print("Invalid Date")
                                    print("Re-enter...")
                            except ValueError:
                                print("Invalid Date")
                                print("Re-enter...")

                    # Get Batch... 
                    isValidBatch = False
                    batch = ""
                    while(not isValidBatch):                
                        batch = input("In which batch you take lecture : ").upper()
                        with open("Batch.txt") as batch_file:
                            data = batch_file.readlines()
                            batches = []
                            for bat in data:
                                batches.extend(bat.split())

                            if(batch in batches):
                                isValidBatch = True
                            else:
                                print(f"Invalid Batch {batch}.")
                                print("Re-enter...")                

                    # Get Subject...
                    isValidSubject = False
                    subject = ""
                    while(not isValidSubject):
                        subject = input(f"Which subject taken in {batch} : ").upper()
                        subjects = faculty[-1].split(",")
                        if(subject in subjects):
                            isValidSubject = True
                        else:
                            print(f"{subject} is not taken by {username}")
                            print("Re-enter...")
                            
                    
                    total_students = {}
                    present_students = {}
                    absent_students = {}
                    present_numbers = []
                    with open("Student.txt") as student_file:
                        data= student_file.readlines()
                        students = []
                        for std in data:
                            students.append(std.split())
                            
                    for student in students:
                        if(student[-2] == batch):
                            total_students[int(student[-1])] = student[1]+" "+student[3]
                    print(f"Total Students :- \n{total_students}")
                    
                    try:
                        print(f"\nEnter below only present Roll numbers in {batch}.\n(Enter excpet roll number after entered all presents.)")
                        for i in range(len(total_students)+1):
                            present = int(input(f"Roll number - {i+1} : "))
                            present_numbers.append(present)
                    except(ValueError):
                        pass
                    
                    present_numbers = list(set(present_numbers))   # for remove duplicates from present numbers
                    absent_students = total_students   
                    
                    # for fetch all Present & Absent students.
                    isNotValidAttendance = False
                    try:
                        for pre in present_numbers:
                            present_students[pre] = total_students[pre]  # add present students in present_students 
                            del(absent_students[pre])   # remove absent students from total students
                    except KeyError as e:
                        isNotValidAttendance = True
                        print(f"Invalid Roll number {e} (Doesn't exists in {batch}).")
                        print("That attendance session are Rejected.")
                        
                    if(not isNotValidAttendance):
                        print(f"{len(present_students)} Present Students : {present_students}")
                        print(f"{len(absent_students)} Abesent Student : {absent_students}")
                        absent_numbers = absent_students.keys()
                         
                        for roll_num in present_numbers:
                            Attendance.Attendance(dt,(faculty[1][0] + faculty[2][0] + faculty[3][0]).upper(), batch, subject, roll_num, present_students[roll_num],"Present")

                        for roll_num in absent_numbers:
                            Attendance.Attendance(dt,(faculty[1][0] + faculty[2][0] + faculty[3][0]).upper(), batch, subject, roll_num, absent_students[roll_num],"Absent")
                                        
                                        
                        
                    print("\nIf, you not want to logout then press except 'EXIT'.")
                    isLogin = input("for Logout press 'EXIT' : ").upper()
                    if(isLogin == "EXIT"):
                        print("Successfully logged out" ,end="")
                        for i in range(3):
                            print(".",end="")
                            time.sleep(0.7)
                
            else:
                print("Login failed.")
            
            
            
            
            
        elif(choice==2):
            print("--Please give me information about Faculty--")
            fname = input("First name : ").strip()
            mname = input("Middle name : ").strip()
            lname = input("Last name : ").strip()
            favourite_number = int(input("Enter your favourite number in 4 digit : "))
            password = ""
            isValidPassword = False
            while(not isValidPassword):         
                password = input("Enter Password : ").strip()
                password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()\-_+=]).{8,}$"
                
                if(re.match(password_pattern , password)):
                    isValidPassword = True
                else:
                    print("Password is must be 8 characters")
                    print("Password is also conatin atleast one Upper,lower,digit & special character.")
                    print("Re-enter...")
                    
            sub_num = int(input(f"How many subjects will teach faculty : "))
            subjects=[input(f"Subject-{i+1} : ").upper().strip() for i in range(sub_num)]
            
            for subject in subjects:
                try:
                    with open("Subject.txt",'r') as subject_file:
                        data = subject_file.readlines()
                        past_subjects = []
                        
                        for sub in data:
                            past_subjects.extend(sub.split())
                        
                        if(subject not in past_subjects):
                            Subject.Subject(subject)
                        
                except:
                    Subject.Subject(subject)

            Faculty.Faculty(fname,mname,lname,favourite_number,password,subjects)

        elif(choice==3):
            print("--Please give me information about Student--")
            fname = input("First name : ").strip()
            mname = input("Middle name : ").strip()
            lname = input("Last name : ").strip()
            cn = input("Course name : ").strip()
            
            isValidBatch = False
            bn=""
            while(not isValidBatch):
                bn = input("Batch name : ").upper().strip()
                with open("Batch.txt") as batch_file:
                    data = batch_file.readlines()
                    batches=[]
                    for batch in data:
                        batches.extend(batch.split())
                    
                    if(bn in batches):
                        isValidBatch = True
                        pass
                    else:
                        print(f"{bn} batch is not exists.")
                        print("Re-enter...")
                        
            isValidRollNumber = True
            rn = int(input("Roll number : "))
            with open("Student.txt") as student_file:
                data = student_file.readlines()
                students = []
                
                for student in data:
                    students.append(student.split())
                
                for student in students:
                    if(bn == student[-2]):
                        if(rn == int(student[-1])):
                            print(f"In {bn} {rn} roll number is alredy exists!")
                            isValidRollNumber = False
                            break
                
            if(isValidRollNumber):
                Student.Student(fname,mname,lname,cn,bn,rn)

        elif(choice==4):
            print("--Please give me information about Batch--")
            batch = ""
            isValidBatch = False
            while(not isValidBatch):            
                batch_pattern = r"^[A-Za-z][0-9]$"
                batch = input("Enter Batch name(eg.A1,B2) : ").upper()
                
                if(re.match(batch_pattern , batch)):
                    isValidBatch = True
                    try: 
                        with open("Batch.txt",'r') as batch_file:
                            data = batch_file.readlines()
                            batches=[]
                            # fetch all batches from file.
                            for bat in data:
                                batches.extend(bat.split())
                            
                            # batch will add only when same batch is not in file. 
                            if(batch in batches):
                                print(f"{batch} is already exists in Data.")
                            else:
                                Batch.Batch(batch)
                            
                    except(FileNotFoundError):
                        pass
                else:
                    print("Batch is like only A1,a1,B1,b2...")
                    print("Re-enter Batch...")
                
        elif(choice==5):
            print("\n1 : Batch-wise")
            print("2 : Student-wise")
            print("3 : Subject-wise")
            
            sub_choice=0
            try:            
                sub_choice = int(input("Enter your choice : "))
            except ValueError:
                print("Enter only 1 to 3 integer numbers only.")
                
                
            with open("Attendance.txt") as attendance_file:
                
                data = attendance_file.readlines()
                attendances = []
                for attendance in data:
                    split = re.split(r'[|\n]',attendance)
                    split = [item for item in split if item.strip()]
                    attendances.append(split)
                
                if(sub_choice == 1):
                    batch_attend = []
                    # Select batch
                    isValidBatch = False
                    batch =""
                    while(not isValidBatch):
                        batch = input("Batch name : ").upper().strip()
                        with open("Batch.txt") as batch_file:
                            data = batch_file.readlines()
                            batches=[]
                            for bn in data:
                                batches.extend(bn.split())

                            if(batch in batches):
                                isValidBatch = True
                                pass
                            else:
                                print(f"{batch} batch is not exists.")
                                print("Re-enter...")
                
                    
                    total_sessions = 0
                    attend_sessions = 0

                    for attendance in attendances:
                        if(attendance[2] == batch):
                            batch_attend.append([attendance[0],attendance[4],attendance[5],attendance[3],attendance[1],attendance[6]])   # date,roll number,name,subject,faculty,status
                            total_sessions += 1
                            if attendance[-1] == 'Present':
                                attend_sessions += 1

                    head = ["Date" , "Roll number" , "Name" , "Subject" , "Faculty" , "Status"]
                    print(f"All-over {batch} attendance is {(attend_sessions/total_sessions)*100} %...")
                    print(tabulate(batch_attend,head,tablefmt="grid"))
                    final_attendance = tabulate(batch_attend,head,tablefmt="grid")
                    
                    need = input("\nYou want to text file? (yes/no) : ").strip().lower()
                    if(need == "yes"):
                        with open("Show_Attendance.txt",'w') as show_attendance_file:
                            show_attendance_file.write(f"Attendace of {batch} {(attend_sessions/total_sessions)*100} %...\n\n")
                            show_attendance_file.writelines(final_attendance)
                        path = "D:\\LJU\\Sem-III\\Python\\Attendance Management\\Show_Attendance.txt"
                        phone_number = "+91" + input("Enter Phone number : ")
                        kit.sendwhatmsg_instantly(phone_number , "Your file is here...")
                        time.sleep()
                        pyautogui.click(715,950)   # click to atach option                          
                        time.sleep(1.5)
                        pyautogui.click(715,600)
                        time.sleep(1.5)
                        pyautogui.typewrite(path)   # write path
                        time.sleep(1.5)
                        pyautogui.press("enter") 
                        time.sleep(1.5) 
                        pyautogui.press("enter")
                
                if(sub_choice == 2):
                    # Select batch
                    std_attend=[]
                    isValidBatch = False
                    batch =""
                    while(not isValidBatch):
                        batch = input("Batch name : ").upper().strip()
                        with open("Batch.txt") as batch_file:
                            data = batch_file.readlines()
                            batches=[]
                            for bn in data:
                                batches.extend(bn.split())

                            if(batch in batches):
                                isValidBatch = True
                                pass
                            else:
                                print(f"{batch} batch is not exists.")
                                print("Re-enter...")
                    
                    isValidRollNumber = False
                    rn = 0
                    name = ""
                    while(not isValidRollNumber):
                        rn = int(input("Roll number : "))
                        with open("Student.txt") as student_file:
                            data = student_file.readlines()
                            students = []
                            
                            for student in data:
                                students.append(student.split())
                            
                            for student in students:
                                if(batch == student[-2]):
                                    if(rn == int(student[-1])):
                                        name = student[1]+ " "+student[3]
                                        isValidRollNumber = True
                                        break

                            if(not isValidRollNumber):
                                print("Invalid roll number")                                                   
                                print("Re-enter...")
                    
                    total_sessions = 0
                    attend_sessions = 0
                    for attendance in attendances:
                        if((attendance[2] == batch) and (int(attendance[4]) == rn)):
                            std_attend.append([attendance[0],attendance[3],attendance[1],attendance[6]])   # date,subject,fac_name,status
                            total_sessions += 1
                            if(attendance[-1] == "Present"):
                                attend_sessions += 1

                    head = ["Date" , "Subject" , "Faculty" , "Status"]
                    print(F"Attendance of {name} {(attend_sessions/total_sessions)*100} %...")
                    print(tabulate(std_attend,head,tablefmt="grid"))
                    final_attendance = tabulate(std_attend,head,tablefmt="grid")
                    
                    print("\nHow many remaining days should be present to maintain minimum attendance?")
                    wantKnow = input("If you want to know : ").strip().lower()
                    if(wantKnow == "yes"):
                        try:
                            total_lectures = int(input("How many total lectures of sem : "))
                            want_minimum = int(input("How many minimum percentage for maintain attendance(in percentage) : "))
                            print(f"You attend remain '{int(((want_minimum/100)*total_lectures)-attend_sessions)}' lectures from '{(total_lectures-total_sessions)}' to maintain attendance {want_minimum}%.")
                        except ValueError:
                            print("Only integer number could be enter.")

                    need = input("\nYou want to text file? (yes/no) : ").strip().lower()
                    if(need == "yes"):
                        with open("Show_Attendance.txt",'w') as show_attendance_file:
                            show_attendance_file.write(f"Attendance of {name} {(attend_sessions/total_sessions)*100} %...\n\n")
                            show_attendance_file.writelines(final_attendance)
                        path = "D:\\LJU\\Sem-III\\Python\\Attendance Management\\Show_Attendance.txt"
                        phone_number = "+91" + input("Enter Phone number : ")
                        kit.sendwhatmsg_instantly(phone_number , "Your file is here...")
                        time.sleep(7)
                        pyautogui.click(715,950)   # click to atach option                          
                        time.sleep(1.5)
                        pyautogui.click(715,600)
                        time.sleep(1.5)
                        pyautogui.typewrite(path)   # write path
                        time.sleep(1.5)
                        pyautogui.press("enter") 
                        time.sleep(1.5) 
                        pyautogui.press("enter")

                if(sub_choice == 3):
                    sub_attend = []
                    # Get Subject...
                    isValidSubject = False
                    subject = ""
                    while(not isValidSubject):
                        with open("Subject.txt") as subject_file:
                            subject = input(f"Which subject : ").strip().upper()
                            subjects = []
                            data = subject_file.readlines()
                            for sub in data:
                                print(sub)
                                subjects.append(sub.split()[1])

                            print(subjects)
                            if(subject in subjects):
                                isValidSubject = True
                            else:
                                print(f"Invalid Subject")
                                print("Re-enter...")

                    total_sessions = 0
                    attend_sessions = 0
                    for attendance in attendances:
                        if((attendance[3] == subject)):
                            sub_attend.append([attendance[0],attendance[2],attendance[4],attendance[5],attendance[6]])   # date,batch,roll_number,name,status
                            total_sessions += 1
                            if(attendance[-1] == "Present"):
                                attend_sessions += 1
                    
                    head = ["Date" , "Batch" , "Roll Number" , "Name" , "Status"]
                    print(F"All over {subject.capitalize()} attendance is {(attend_sessions/total_sessions)*100} %...")

                    print(tabulate(sub_attend,head,tablefmt="grid"))

                    final_attendance = tabulate(sub_attend,head,tablefmt="grid")
                    
                    need = input("\nYou want to text file? (yes/no) : ").strip().lower()
                    if(need == "yes"):
                        with open("Show_Attendance.txt",'w') as show_attendance_file:
                            show_attendance_file.write(f"All over {subject} attendance is {(attend_sessions/total_sessions)*100} %...\n\n")
                            show_attendance_file.writelines(final_attendance)
                        path = "D:\\LJU\\Sem-III\\Python\\Attendance Management\\Show_Attendance.txt"
                        phone_number = "+91" + input("Enter Phone number : ")
                        kit.sendwhatmsg_instantly(phone_number , "Your file is here...")
                        time.sleep(7)
                        pyautogui.click(715,950)   # click to atach option                          
                        time.sleep(1.5)
                        pyautogui.click(715,600)
                        time.sleep(1.5)
                        pyautogui.typewrite(path)   # write path
                        time.sleep(1.5)
                        pyautogui.press("enter") 
                        time.sleep(1.5) 
                        pyautogui.press("enter")
                
            
        else:
            flag = False
    else:
        print("Enter only number in between 0 to 5.")