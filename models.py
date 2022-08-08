from peewee import *

db = PostgresqlDatabase( \
  'contacts',\
    user='adam', \
    password='', \
    host='localhost', \
    port=5432)
    
db.connect()

class BaseModel(Model):
  class Meta:
    database = db

class Contact(BaseModel):
  first_name = CharField()
  last_name = CharField()
  phone_num = CharField()
  email = CharField()
  