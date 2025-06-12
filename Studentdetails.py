class Student:
    def __init__(self,name,age,rollno,clgname,dept):
        self.name=name
        self.age=age
        self.rollno=rollno
        self.clgname=clgname
        self.dept=dept
    def name(self):
        return self.name
    def age(self):
        return self.age
    def rollno(self):
        return self.rollno
    def clgname(self):
        return self.clgname
    def dept(self):
        return self.dept
    
class StudentDetails(Student):
    def __init__(self,native,fname,focc,mname,mocc):
        self.native=native
        self.fname=fname
        self.focc=focc
        self.mname=mname
        self.mocc=mocc
    def native(self):
        return self.native
    def fname(self):
        return self.fname
    def focc(self):
        return self.focc
    def mname(self):
        return self.mname
    def mocc(self):
        return self.mocc
    

name=input("Enter the Name: ")
age=int(input("Enter the Age: "))
rollno=int(input("Enter the Roll_no: "))
clgname=input("Enter the college_name: ")
dept=input("Ente the Department_Name: ")
native=input("Enter the native place: ")
fname=input("Enter your father's name: ")
focc=input("Enter your father's occupation: ")
mname=input("Enter your mother's name: ")
mocc=input("Enter your mother's occupatioin: ")
stu=Student(name,age,rollno,clgname,dept)
stu1=StudentDetails(native,fname,focc,mname,mocc)
print("Thank you for your details.....")
print("Check wether the given details are correct...")


print("Name: ",stu.name)
print("Age: ",stu.age)
print("Roll_No: ",stu.rollno)
print("College_name: ",stu.clgname)
print("Department: ",stu.dept)
print("Native place: ",stu1.native)
print("Father's_name: ",stu1.fname)
print("Father's_occupation: ",stu1.focc)
print("Mother's_name: ",stu1.mname)
print("Mother's_occupation: ",stu1.mocc)
