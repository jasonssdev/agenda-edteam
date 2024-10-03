import os
from  tabulate import tabulate
from connection import *
from contact import *

conn = connect()
create_table(conn)

def start():
    os.system('cls')
    while True:
        print('Select an option')
        print('\t1. Add a new contact')
        print('\t2. Show contacts')
        print('\t3. Search a contact')
        print('\t4. Edit a contact')
        print('\t5. Delete a contact')
        print('\t6. Logout')
        option = input('Chose an option: ')
        if option == '1':
            register_contact()
        elif option == '2':
            show_contacts()
        elif option == '3':
            search_contact()
        elif option == '4':
            edit_contact()
        elif option == '5':
            delete_contact()
        elif option == '6':
            break
    
def register_contact():
    name = input('Enter name: ')
    last_name = input('Enter last name: ')
    business_name = input('Enter business name: ')
    phone = input('Enter phone: ')
    email = input('Enter email: ')
    address = input('Enter address: ')
    response = register(name, last_name, business_name, phone, email, address)
    print(response)

def show_contacts():
    data = show()
    headers = ['ID', 'NAME', 'LAST_NAME', 'BUSINESS_NAME', 'PHONE', 'EMAIL', 'ADDRESS']
    table = tabulate(data, headers, tablefmt='fancy_grid')
    print(table)

def search_contact():
    id = input('enter contact id: ')
    data = search(id)
    headers = ['ID', 'NAME', 'LAST_NAME', 'BUSINESS_NAME', 'PHONE', 'EMAIL', 'ADDRESS']
    table = tabulate(data, headers, tablefmt='fancy_grid')
    print(table)

def edit_contact():
    id = input('enter contact id: ')
    name = input('Enter name: ')
    last_name = input('Enter last name: ')
    business_name = input('Enter business name: ')
    phone = input('Enter phone: ')
    email = input('Enter email: ')
    address = input('Enter address: ')
    response = edit(id, name, last_name, business_name, phone, email, address)
    print(response)

def delete_contact():
    id = input('enter contact id: ')
    response = delete(id)
    print(response)

start()





