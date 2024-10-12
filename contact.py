from connection import *
#new comment

def register(name, last_name, business_name, phone, email, address):
    try:
        conn = connect()
        cursor =  conn.cursor()
        sql_query = ''' INSERT INTO contacts(
            name, last_name, business_name, phone, email, address) 
            VALUES (?, ?, ?, ?, ?, ?)'''
        data = (name, last_name, business_name, phone, email, address)
        cursor.execute(sql_query, data)
        conn.commit()
        conn.close()
        return 'registration has been completed'
    except sqlite3.Error as err:
        print('Something was wrong', err)

def show():
    data =  []
    try:
        conn = connect()
        cursor =  conn.cursor()
        sql_query = ''' SELECT * FROM contacts'''
        cursor.execute(sql_query)
        data = cursor.fetchall()
        conn.close()
    except sqlite3.Error as err:
        print('Something was wrong', err)
    return data

def search(id):
    data = []
    try:
        conn = connect()
        cursor =  conn.cursor()
        sql_query = ''' SELECT * FROM contacts WHERE id=?'''
        cursor.execute(sql_query, (id,))
        data = cursor.fetchall()
        conn.close()
    except sqlite3.Error as err:
        print('Something was wrong', err)
    return data

def edit(id, name, last_name, business_name, phone, email, address):
    try:
        conn = connect()
        cursor =  conn.cursor()
        sql_query = ''' UPDATE contacts SET name=?, last_name=?, business_name=?, phone=?, email=?, address=? WHERE id=?'''
        data = (name, last_name, business_name, phone, email, address, id)
        cursor.execute(sql_query, data)
        conn.commit()
        conn.close()
        return 'contact has been edited'
    except sqlite3.Error as err:
        print('Something was wrong', err)

def delete(id):
    try:
        conn = connect()
        cursor =  conn.cursor()
        sql_query = ''' DELETE FROM contacts WHERE id=?'''
        cursor.execute(sql_query, (id,))
        conn.commit()
        conn.close()
        return 'contact has been deleted'
    except sqlite3.Error as err:
        print('Something was wrong', err)
