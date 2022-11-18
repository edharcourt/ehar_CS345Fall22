# https://firebase.google.com/docs/firestore/quickstart

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("cs345fall22-firebase-adminsdk-3ivaa-67f327fcdb.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

students = db.collection(u'students')

# READ: Read some students
"""
docs = students.stream()
for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
"""

# CREATE: insert data about Ron
"""
doc = students.document(u'student3')
doc.set(
    {
        "courses" : [{"coursenum" : "H101",
                      "title" : "Herbology",
                      "semester" : "Spring",
                      "year" : 2009},

                     {"coursenum" : "C101",
                      "title" : "Charms",
                      "semester" : "Spring",
                      "year" : 2008}],
        "name" : {"first" : "Ron", "last" : "Weasley"}
    }
)
"""

# Update a document
"""
doc = students.document(u'student3')
doc.update({u'name.first' : u'Ronald'})
"""

# DELETE
students.document(u'student3').delete()

print("Done")