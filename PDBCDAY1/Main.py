from curdoperations import add_Employee,view_Employee,del_Employee
print("1.add employee")
print("2.view employee")
print("3.update employee")
print("4.delete employee")
print("5.exit employee")

chooseOption=int(input("choose one above option:-"))
if chooseOption==1:
    emp_name=input("enter emp_name:--").strip()
    emp_sal=int(input("enter emp_sal:--"))
    emp_dept=input("enter emp_dept:--").strip()
    emp_loc=input("enter emp_loc:--").strip()
    add_Employee(emp_name,emp_sal,emp_dept,emp_loc)
elif chooseOption==2:
    view_Employee()
elif chooseOption==3:
    emp_id=int(input("enter emp_id here:----"))
    del_Employee()




