import pyrebase

#Configure and Connext to Firebase

firebaseConfig = {
    'apiKey': "AIzaSyCNml3HZFFlmDjLWWemALI5iq32xwFrKNs",
    'authDomain': "tshs-app.firebaseapp.com",
    'projectId': "tshs-app",
    'databaseURL': "https://tshs-app-default-rtdb.firebaseio.com/",
    'storageBucket': "tshs-app.appspot.com",
    'messagingSenderId': "315720159645",
    'appId': "1:315720159645:web:fd27aa9bc7a163e5c65f74"}

firebase=pyrebase.initialize_app(firebaseConfig)
database = firebase.database();

data = {'age': 52, 'name': 'heback', 'isMan': True}

database.push(data)

