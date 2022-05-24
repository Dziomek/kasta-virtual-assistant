from DataBase.Connection import ConnectDatabase


def type_note(note, idUsers, key_word):
    title = ''
    note = note.split(key_word, 2)[1].strip()

    print(idUsers)
    print(title)
    print(note)
    print(key_word)

    connection = ConnectDatabase()
    connection.insertNote(title, note, idUsers)
