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

    def loginAuthentication(self, email,  hashedPassword):
        if self.connection.is_connected():
            sql_select_Query = "select * from Users where email='" + email + "' and password='" + hashedPassword + "'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)

            # get all records
            records = cursor.fetchall()
            return records

    def checkUserExists(self, email):
        if self.connection.is_connected():
            print('connected')
            sql_select_Query = "select * from Users where email='" + email + "'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            cursor.fetchall()

            #check the existence
            if cursor.rowcount == 0:
                return False
            else:
                return True


    def insertRegisterData(self, firstName, lastName, email, password, date, token, validAccount):
        if self.connection.is_connected():
            sql_select_Query = "INSERT INTO Users(firstName, lastName, email, password, birthday, token, validAccount) " \
                               " VALUES('"+firstName+"','" + lastName + "','" + email + "','" + password + "','" + date + "','" + token + "','" + validAccount + "') "
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            self.connection.commit()
        else:
            print('Error while inserting data to DB')

    def updateValidationAccount(self,email):
        if self.connection.is_connected():
            sql_select_Query = "UPDATE Users SET validAccount = 'True' WHERE email= '" + email + "'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            self.connection.commit()
        else:
            print('Error while updating data to DB')

    def newOtpCode(self, email, token):
        if self.connection.is_connected():
            sql_select_Query = "UPDATE Users SET token = '" + token +"' WHERE email= '" + email + "'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            self.connection.commit()
        else:
            print('Error while inserting new token')


    def returnIdUser(self, email):
        if self.connection.is_connected():
            sql_select_Query = "SELECT idUsers from Users WHERE email = '" + email + "'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            return cursor.fetchall()
        else:
            print('Error while returning idUser')


    def insertNote(self,title, note, idUsers):
        if self.connection.is_connected():
            sql_select_Query = "INSERT INTO Notes(title,text,idUsers) VALUES ('" +title + "','" + note + "','" + str(idUsers) + "')"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            self.connection.commit()
        else:
            print('Error while inserting note to DB')


    def returnNotesTopics(self,idUsers):
        if self.connection.is_connected():
            sql_select_Query = "SELECT title from Notes WHERE idUsers = '" + str(idUsers) + "'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            return cursor.fetchall()


    def returnNote(self,title,idUsers):
        if self.connection.is_connected():
            sql_select_Query = "SELECT text from Notes WHERE idUsers = '" + str(idUsers) + "' and title = '" + title + "'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            return cursor.fetchall()

    def get_user_name(self, email):
        if self.connection.is_connected():
            sql_select_Query = "SELECT firstName from Users WHERE email = '" + email + "'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)

            # get all records
            name = cursor.fetchall()
            return name

