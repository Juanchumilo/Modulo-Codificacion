import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="2207Chumilo,",
        database="actividad_flask",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
