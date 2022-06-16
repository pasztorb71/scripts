from datetime import datetime

import firebase_admin
from firebase_admin import credentials, firestore


def connect():
    cred = credentials.Certificate('./firestore_key.json')
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db

if __name__ == '__main__':
    db = connect()
    data = {"name": "Los Angeles", "state": "CA", "country": "USA"}
    #db.collection("cities").document("LA").set(data)
    #exit(0)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Start Time =", current_time)

    for i in range(1,11):
        db.collection("cities").document("city_"+str(i)).set(data)
        #db.collection("cities").document("city_"+str(i)).delete() #12:32:19 - 12:33:47
        #db.collection("cities").document("city1_"+str(i)).delete() #12:29:48 - 12:31:15
        #import függvény nélkül 12:50:48 - 12:51:34
        #import függvénnyel 12:59:50 - 1:01:51 Nem replikál

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("End Time =", current_time)