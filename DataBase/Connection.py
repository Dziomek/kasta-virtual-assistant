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


    def insertRegisterData(self, firstName, lastName, email, password, phone, token, validAccount):
        if self.connection.is_connected():
            sql_select_Query = "INSERT INTO Users(firstName, lastName, email, password, phone, token, validAccount) " \
                               " VALUES('"+firstName+"','" + lastName + "','" + email + "','" + password + "','" + phone+ "','" + token + "','" + validAccount + "') "
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

    def get_notes(self, idUsers):
        if self.connection.is_connected():
            sql_select_Query = "SELECT text from Notes WHERE idUsers = '" + str(idUsers) + "'"
            #print(sql_select_Query)
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            return cursor.fetchall()

    def get_id_note(self, note_text):
        if self.connection.is_connected():
            sql_select_Query = "SELECT idNotes from Notes WHERE text = '" + note_text + "'"
            #print(sql_select_Query)
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            return cursor.fetchall()

    def delete_note_with_id(self, note_id):
        if self.connection.is_connected():
            sql_select_Query = "DELETE from Notes WHERE idNotes = '" + str(note_id) + "'"
            #print(sql_select_Query)
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            self.connection.commit()
            #print('note ' + str(note_id) + ' deleted')

    def get_valid_account(self, user_email):
        if self.connection.is_connected():
            sql_select_Query = "SELECT validAccount from Users WHERE email = '" + user_email + "'"
            # print(sql_select_Query)
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            #print(cursor.fetchall()[0][0])
            return cursor.fetchall()

    def get_commands(self, idUsers):
        if self.connection.is_connected():
            sql_select_Query = "SELECT keyWord, url from Commands2 WHERE idUsers = '" + str(idUsers) + "'"
            #print(sql_select_Query)
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            return cursor.fetchall()

    def get_id_command(self, key_word):
        if self.connection.is_connected():
            sql_select_Query = "SELECT idCommands from Commands2 WHERE keyWord = '" + key_word + "'"
            # print(sql_select_Query)
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            return cursor.fetchall()

    def delete_command_with_id(self, command_id):
        if self.connection.is_connected():
            sql_select_Query = "DELETE from Commands2 WHERE idCommands = '" + str(command_id) + "'"
            #print(sql_select_Query)
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            self.connection.commit()
            #print('command ' + str(command_id) + ' deleted')

    def insert_app(self, key_word, url, user_id):
        if self.connection.is_connected():
            sql_select_Query = "INSERT INTO Commands2(keyWord, url ,idUsers) VALUES ('" + key_word + "','" + url + "','" + str(user_id) + "')"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            self.connection.commit()
        else:
            print('Error while inserting note to DB')