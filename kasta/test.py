

from DataBase.Connection import ConnectDatabase
user_choose = 'title'
idUsers = 70
connection = ConnectDatabase()
entire_note = connection.returnNote(user_choose, idUsers)
print(entire_note[0][0])