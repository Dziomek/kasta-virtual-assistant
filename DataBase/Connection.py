import mysql.connector
from mysql.connector import Error

from DataBase.databaseConfig import USER
from DataBase.databaseConfig import PASSWORD
from DataBase.databaseConfig import HOST
from DataBase.databaseConfig import DATABASE


class ConnectDatabase:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(user=USER,
                                                      password=PASSWORD,
                                                      host=HOST,
                                                      database=DATABASE)
            self.cursor = self.connection.cursor()
        except Error as e:
            print("Error while connecting to MySQL", e)

    def loginAuthentication(self, email, password):
        if self.connection.is_connected():
            sql_select_Query = "select * from Users where email='" + email + "' and password='" + password + "'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)

            # get all records
            records = cursor.fetchall()
            return records


"""def connectToDatabaseLogin():
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

            print('Wyciagniete haslo:', passwordUser)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")"""
