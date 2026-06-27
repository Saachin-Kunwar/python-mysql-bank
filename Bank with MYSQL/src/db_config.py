import mysql.connector as myconn

def connect():
    return myconn.connect(
        host="localhost",
        user="root",
        password="yourmysql password",
        database="your data base name"
    )