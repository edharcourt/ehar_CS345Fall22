# https://firebase.google.com/docs/firestore/quickstart

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("cs345fall22-firebase-adminsdk-3ivaa-67f327fcdb.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

students = db.collection(u'students')
docs = students.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')

print("Done")