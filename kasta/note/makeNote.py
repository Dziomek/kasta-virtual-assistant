from DataBase.Connection import ConnectDatabase


def make_note(title, note, idUsers):
    title = ''.join(title)
    note = ''.join(note)

    print(idUsers)
    print(title)
    print(note)

    connection = ConnectDatabase()
    connection.insertNote(title, note, idUsers)
