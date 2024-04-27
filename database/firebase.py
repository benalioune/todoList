import firebase_admin
from firebase_admin import credentials
import pyrebase
import json

from configs.firebase_config import firebaseConfig

from dotenv import dotenv_values






# import des crédentiels
#initialise our app import credentials if not done
if not firebase_admin._apps: 
    cred = credentials.Certificate("configs/todo-a0df3-firebase-adminsdk-ulejs-c36a75d8de.json")
    firebase_admin.initialize_app(cred)



# getting access to firebase  by using rebase / create a new firebase instance  
firebase = pyrebase.initialize_app(firebaseConfig)
# access to our database instance by pyrebase 
db = firebase.database()
authTodo = firebase.auth()

