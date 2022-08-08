from models import *

db.drop_tables([Contact])
db.create_tables([Contact])

adam = Contact( \
  first_name = 'Adam', \
  last_name = 'Bachrach', \
  phone_num = '908-111-1111', \
  email = 'adam@gmail.com')
adam.save()

ayoni = Contact( \
  first_name = 'Ayoni', \
  last_name = 'Bachrach', \
  phone_num = '908-222-2222', \
  email = 'ayoni@gmail.com')
ayoni.save()

andy = Contact( \
  first_name = 'Andy', \
  last_name = 'Bachrach', \
  phone_num = '908-333-3333', \
  email = 'andy@gmail.com')
andy.save()

alex = Contact( \
  first_name = 'Alex', \
  last_name = 'Bachrach', \
  phone_num = '908-444-4444', \
  email = 'alex@gmail.com')
alex.save()

db.close()
