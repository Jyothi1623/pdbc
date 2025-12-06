import mysql.connector
db_connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Amma@16",
    database="SBIBankDatabase"

   
)
cursorobj=db_connection.cursor()
def signup():
    name=input("enter name:----").strip().lower()
    password=input("enter pwd:----").strip().lower()
    userRole=input("enter userrole(customer/admin):----").strip().lower()
    cursorobj.execute("insert into  users(user_name,user_pwd,user_role) values (%s,%s,%s)", (name,password,userRole,) )
    db_connection.commit()
    cursorobj.execute("select*from users where user_name=%s", (name,))
    data=cursorobj.fetchone()
    # print(data)
    user_id,un,up,urole=data
    print(user_id,"id")


    acc_type=input("enter ac/type (savings/current):----")
    cursorobj.execute("insert into accounts(user_id,acc_type,acc_bal) values(%s,%s,%s)",(user_id,acc_type,5000))

print("-----SBI BANK PROJECT------")
print("1. signup")
print("2. login")
print("3. exit")

choose=input("enter option:----")
if choose=="1":
    signup()




