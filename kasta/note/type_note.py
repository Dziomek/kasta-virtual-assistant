from DataBase.Connection import ConnectDatabase


def type_note(note, idUsers):
    title = ''
    note = note.split('notetype', 2)[1].strip()

    print(idUsers)
    print(title)
    print(note)

    connection = ConnectDatabase()
    connection.insertNote(title, note, idUsers)
