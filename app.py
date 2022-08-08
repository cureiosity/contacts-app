from models import *

contacts = []

class Contact:
  def __init__(self, first_name, last_name, phone_num, email):
    self.first_name = first_name
    self.last_name = last_name
    self.phone_num = phone_num
    self.email = email

def new_contact():
  first_name = input('First Name: ')
  last_name = input('Last Name: ')
  phone_num = input('Phone Number: ')
  email = input('Email Address: ')
  contact = Contact(first_name, last_name, phone_num, email)
  contacts.append(contact)
  print('')
  print('Contact added!')
  print('')
  print(f'{first_name} {last_name}')
  print(email)
  print(phone_num)
  print('')
  user_options()

def welcome():
  print('Welcome to Contacts')
  print('')
  print('Add your first contact! Type the value for each field, then press Enter/Return.')
  print('')
  new_contact()

def user_options():
  print('To view your contacts, use the View command.')
  print('To add another contact, use the Add command.')
  print('To exit the program, use the Exit command.')
  print('')
  user_selection()

def user_selection():
  selection = input('')
  selection = selection.lower()
  if selection == 'view':
    view_contacts()
  elif selection == 'add':
    new_contact()
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
  for contact in contacts:
    print(f'{contact.first_name} {contact.last_name}')
    print(contact.email)
    print(contact.phone_num)
    print('')
  user_options()

welcome()
