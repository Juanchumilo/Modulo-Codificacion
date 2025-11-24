import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="TU_PASSWORD",
        database="actividad_flask",
        cursorclass=pymysql.cursors.DictCursor
    )
