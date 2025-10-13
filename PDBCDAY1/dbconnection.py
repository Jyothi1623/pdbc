import mysql.connector
print(mysql.connector)

def db_connection():
    mysql.connector.connect(
        host='localhost',
        user='root',
        password='Amma@16',
        database='empmanageSys'
    )
print('database connected succesfully')