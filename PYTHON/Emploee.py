class Employee:
    count=0
    def __init__(self, name, desig, salary): 
        self.name =name 
        self.desig=desig
        self.salary=salary
        Employee.count+=1 
    def displayCount (self): 
        print("\nThere are %d employees" % Employee.count) 
    def displayDetails (self): 
        print("\nName: ",self.name,", Designation:",self.desig, 
              ",Salary: ", self.salary)


el= Employee ("John","Manager",80000)

e2= Employee ("Mike", "Team Leader",50000)

e3 = Employee("Derek","Programmer",30000)

e4 =Employee ( "Raj", "Assistant",25000)

e4.displayCount() 
print("\nDetails of all employee: ")

el.displayDetails ( )

e2.displayDetails ( ) 

e3.displayDetails ( )

e4.displayDetails ( )