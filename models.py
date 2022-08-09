from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

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
