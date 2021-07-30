import os
import shutil
import sys
import pymysql
try:
    connection = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='',
    database='bof',
    cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute("""CREATE TABLE sud 
            (
            id int AUTO_INCREMENT PRIMARY KEY,
            pl1 varchar(32),
            pl2 varchar(32),
            st varchar(32),
            more varchar(32),
            verd varchar(32),
            disid varchar(32)
            )
            """)
            connection.commit()

    finally:
        connection.close()

except Exception as ex:
    print('not work')
    print(ex)