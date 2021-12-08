import urllib
import pyrebase
from pyrebase.pyrebase import Storage

firebaseConfig = {
    'apiKey': "AIzaSyDJ5OXTr2WM2ohx-nlmLrLC_U3qMpPHgiQ",
    'authDomain': "firsta-7968e.firebaseapp.com",
    'projectId': "firsta-7968e",
    'storageBucket': "firsta-7968e.appspot.com",
    'messagingSenderId': "912628195441",
    'appId': "1:912628195441:web:a713b246ca15e874a77bd0",
    'measurementId': "${config.measurementId}",
    'databaseURL': "https://firsta-7968e.firebaseio.com"
  }

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()
# Authentication
email = input("Enter Your Email: ")
password = input("Enter Your Password: ")
try:
  auth.sign_in_with_email_and_password(email, password)
  print("Success!")
except:
  print("Invalid Credentials")
# SignUP
email = input("Enter Your Email: ")
password = input("Enter Your Password: ")
cpass = input("Confirm Your Password: ")
if password == cpass:
  try:
    auth.create_user_with_email_and_password(email,password)
    print("Account Created Successfully!")
  except:
    print("Email Aready Exist!")
else:
  print("Password did not matched")
# Storage
filename= input("Enter the name of file you want to Upload: ")
cloudFile = input("Enter the name of the cloud where you want to store: ")
storage.child(cloudFile).put(filename)
print(storage.child(cloudFile).get_url(None))
# Download
filename = input("Enter the name of file to be downloaded: ")
storage.child(filename).download("", "downloaded.txt")

# reading file
filename = input("Enter the name of file to be read: ")
url = storage.child(filename).get_url(None)
file = urllib.request.urlopen(url).read()
print(file)
# Database

context = {
  'name': "Aftab",
  'age': 21,
  'resident': "Mumbai"
}
db.push(context)

