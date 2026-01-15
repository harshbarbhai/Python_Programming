
def EmployeeInfo(Name,Age,Salary,City="Pune"):
    print("Name: ",Name)
    print("Age: ",Age)
    print("Salary: " ,Salary)
    print("City: ",City)

def main():
    #keyword arguments
    EmployeeInfo(Age=26,Name="Rahul",City="Pune",Salary=2000.50) #correct

if __name__=="__main__":
    main()