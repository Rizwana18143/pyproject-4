print("---Employee Management System---")
print("1.Developer")
print("2.Manager")
print("3.Tester")
choice=int(input("enter your Choice:"))
class Employee:
    def __init__(self):
        self.EmployeeId=int(input("enter Employee Id:"))
        self.EmployeeName=input("enter employee Name:")
        self.BasicSalary=int(input("enter Basic Salary:"))
    def display_details(self):
        print("EmployeeId :",self.EmployeeId)
        print("employee Name:",self.EmployeeName)
    def calculate_salary(self):
        return self.BasicSalary 
    

class Developer(Employee):
    def __init__(self):
            super().__init__()
            self.programmingLanguage=input("enter Programming Language:")
            self.ProjectName=input("enter Project Name:")
            self.Experience=int(input("enter Experience:"))
    def calculate_salary(self):
            self.FinalSalary=self.BasicSalary+(self.BasicSalary*20/100)
            print("final salary:",self.FinalSalary)
    def display_details(self):
            print("Programming Language:",self.programmingLanguage)
            print("Project Name:",self.ProjectName)
            print("experience:",self.Experience)

class Manager(Employee):
    def __init__(self):
            super().__init__()
            self.Department=input("enter department:")
            self.TeamSize=input("enter team size:")
            self.Experience=int(input("enter Experience:"))
    def calculate_salary(self):
            self.FinalSalary=self.BasicSalary+(self.BasicSalary*30/100)
            print("final salary:",self.FinalSalary)
    def display_details(self):
            print("Department:",self.Department)
            print("Team size:",self.TeamSize)
            print("Experience:",self.Experience)
            
class Tester(Employee):
    def __init__(self):
            super().__init__()
            self.TestingTool=input("enter testing tool:")
            self.TestingType=input("enter TestingType:")
            self.Experience=int(input("enter Experience:"))
    def calculate_salary(self):
            self.FinalSalary=self.BasicSalary+(self.BasicSalary*15/100)
            print("final salary:",self.FinalSalary)
    def display_details(self):
            print("Testing tool:",self.TestingTool)
            print("Testing type:",self.TestingType)
            print("Experience:",self.Experience)
if choice==1:
    d=Developer()
    d.calculate_salary()
    d.display_details()
elif choice==2:
    m=Manager()
    m.calculate_salary()
    m.display_details()
elif choice==3:
    t=Tester()
    t.calculate_salary()
    t.display_details()
else:
    print("invalid choice")