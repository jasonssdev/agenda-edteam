import sqlite3

def connect():
    try:
        connection = sqlite3.connect('contacts.db')
        print('database has been connected')
        return connection
    except sqlite3.Error as err:
        print('Something was wrong', err)


def create_table(connection):
    cursor = connection.cursor()
    sql_query = '''CREATE TABLE IF NOT EXISTS contacts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        business_name TEXT NOT NULL, 
        phone TEXT NOT NULL,
        email TEXT NOT NULL,
        address TEXT NOT NULL
    )'''
    cursor.execute(sql_query)
    connection.commit()