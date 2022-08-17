import sqlite3
import pandas as pd
from prettify_txt import clear_text

# list_chat = ['whatsapp', 'telegram', 'vk']

conn = sqlite3.connect('main.db')
cur = conn.cursor()
print("Подключен к main.db/whatsapp")

cur.execute("""CREATE table IF NOT EXISTS 'whatsapp' ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT,
        time TEXT,
        sms TEXT,
        check_point TEXT);""")
conn.commit()

def insert_in_db():
    data_tuple = clear_text()
    for i, row in enumerate(data_tuple):

        sqlite_insert_with_param = """INSERT INTO 'whatsapp'
                                  (data, time, sms)
                                  VALUES (?, ?, ?);"""

        cur.execute(sqlite_insert_with_param, row)
        conn.commit()
        print(f'add {i + 1} row')

# except sqlite3.Error as error:
#     print("Ошибка при работе с SQLite", error)
# finally:
#     if sqlite_connection:
#         sqlite_connection.close()
#         print("Соединение с main.db закрыто")

df = pd.read_sql('select * from whatsapp limit 10', conn, index_col="id")
print(df)

# cur.execute('select * from whatsapp')
# first_str = cur.fetchall()
# print(first_str)


