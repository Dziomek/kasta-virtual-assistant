import mysql.connector
from mysql.connector import Error
from databaseConfig import USER
from databaseConfig import PASSWORD
from databaseConfig import HOST
from databaseConfig import DATABASE


try:
    connection = mysql.connector.connect(user=USER,
                                         password=PASSWORD,
                                         host=HOST,
                                         database=DATABASE)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

        sql_select_Query = "select * from Users"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)
        print(records)
        passwordUser = ''
        for row in records:
            passwordUser = row[4]

        print('Wyciagniete haslo:',passwordUser)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

