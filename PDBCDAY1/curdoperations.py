from dbconnection import db_connection
def add_Employee(n,s,d,l):
    db_connect=db_connection()
    cur=db_connect.cursor()
    cur.execute("insert into employees(emp_name, emp_sal, emp_dept, emp_loc) values(%s,%s,%s,%s)",(n,s,d,l))
    db_connect.commit()
    db_connect.close()
    print(f"{n} employees is added succesfully")
def view_Employee():
    db_connect=db_connection()
    cur=db_connect.cursor()
    cur.execute("select*from employees")
    data=cur.fetchall()
    print(data)
    db_connect.close()
    print("sucesfully data fetched")

def del_Employee():
    db_connect=db_connection()
    cur=db_connect.cursor()
    cur.execute("delete from employees where emp_id= %s",(id,))
    db_connect.commit()
    print(f"Employee with id no:---{id} is deleted successfully")



