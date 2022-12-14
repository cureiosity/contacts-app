from models import *
from playhouse.shortcuts import model_to_dict, dict_to_model

def welcome():
  print('Welcome to Contacts!')
  print('')
  user_options()

def user_options():
  print('To view all contacts, use the View command.')
  print('To find a specific contact, use the Find command.')
  print('To add another contact, use the Add command.')
  print('To exit the program, use the Exit command.')
  print('')
  user_selection()

def user_selection():
  selection = input('')
  selection = selection.lower()
  if selection == 'view':
    view_contacts()
  elif selection == 'find':
    find_contact()
  elif selection == 'add':
    create_new_contact()
  elif selection == 'exit':
    print('')
    print('Goodbye!')
  else:
    print('')
    print('Invalid Command!')
    print('')
    user_options()

def view_contacts():
  print('')
  contacts = []
  for contact in Contact.select():
    contacts.append(model_to_dict(contact))
  for contact in contacts:
    print(f'{contact["first_name"]} {contact["last_name"]}')
    print(f'{contact["phone_num"]}')
    print(f'{contact["email"]}')
    print('')
  user_options()

def find_contact():
  print('')
  search_term = input('Enter your search: ')
  contacts = []
  filtered_contacts = []
  for contact in Contact.select():
    contacts.append(model_to_dict(contact))
  for contact in contacts:
    if( \
    search_term.lower() == contact['first_name'].lower() \
    or search_term.lower() == contact['last_name'].lower() \
    or search_term.lower() == contact['phone_num'].lower() \
    or search_term.lower() == contact['email'].lower()):
        filtered_contacts.append(contact)
  print('')
  for contact in filtered_contacts:
    print(f'{contact["first_name"]} {contact["last_name"]}')
    print(f'{contact["phone_num"]}')
    print(f'{contact["email"]}')
    print('')
  user_options()

def create_new_contact():
  print('')
  new_contact = Contact( \
    first_name = input('First Name: '), \
    last_name = input('Last Name: '), \
    phone_num = input('Phone Number: '), \
    email = input('Email Address: ')
  )
  new_contact.save()
  print('')
  print('Contact added!')
  print('')
  print(f'{new_contact.first_name} {new_contact.last_name}')
  print(new_contact.phone_num)
  print(new_contact.email)
  print('')
  user_options()

welcome()
