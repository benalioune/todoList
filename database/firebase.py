import firebase_admin
from firebase_admin import credentials
import pyrebase
import os


from dotenv import load_dotenv

load_dotenv()

configs= {
    "FIREBASE_SERVICE_ACCOUNT_KEY" :     os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY"),
    "FIREBASE_CONFIG" : os.getenv('FIREBASE_CONFIG')
              
}







# import des crédentiels
#initialise our app import credentials if not done
if not firebase_admin._apps: 
    cred = credentials.Certificate(configs["FIREBASE_SERVICE_ACCOUNT_KEY"])
    firebase_admin.initialize_app(cred)



# getting access to firebase  by using rebase / create a new firebase instance  
firebase = pyrebase.initialize_app(configs["FIREBASE_CONFIG"])
# access to our database instance by pyrebase 
db = firebase.database()
authTodo = firebase.auth()

