import sqlite3

#Обращение к БД
def OutSet(file: str):
    db = sqlite3.connect(file)
    sql = db.cursor()
    sql.execute("SELECT * FROM Phonebook")
    data = sql.fetchall()
    db.commit()
    return data