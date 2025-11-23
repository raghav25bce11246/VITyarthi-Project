import datetime as dt
class Office:
    def __init__(self,name,role):
        print("-------------------------------------------------------")

        print("Mr.",name,"punched in")
        

        self.name = name
        self.role = role
    def targets(self,sales):
        self.sales = sales
        print("Mr.",self.name,"Your current sales are",sales)
        print("Your target for this month is",sales+20)
        
    def techteam(self,team):
        self.team = team
        if team == "cloud":
            print("Mr.",self.name,"Your current project is in collaboration with mahindra")
            if self.role != "Cloud Head":
                print("Get details from Mr.Ram")
                


        elif team == "backend":
            j = int(input("no. of databases managed: "))
            if j<3:
                print("get new databases from server department")
            elif j>=3:
                print("ensure stability and maintain new additions")
            print("Company monthly report required by you for this month")
            print("Mr.",self.name,"kindly submit your maintainence goals")

        elif team == "cyber":
            a = int(input("enter bugs fixes completed this month: "))
            print("your incentive is ", a*500)
    def deadline(self):
            x = dt.date.today()
            y = x + dt.timedelta(10)

            print("Mr.",self.name,"your project deadline is ",y)


print("---ROLE--CODES---")
print("111 for sales")
print("222 for cyber")
print("333 for backend")
print("444 for cloud")
print("555 to get your project deadline")


x = input("enter name: ")
y = input("enter role: ")
z = int(input("enter role code: "))
def officestatus(x,y,z):
    employee = Office(x,y)

    if z == 111:
        sale = int(input("enter current sales: "))
        employee.targets(sale)
    
    elif z == 222:
        employee.techteam(y)
    
    elif z == 333:
        employee.techteam(y)
    
    elif z == 444:
        employee.techteam(y)
    
    elif z == 555:
        employee.deadline()

    
        
    
    
officestatus(x,y,z)


        




