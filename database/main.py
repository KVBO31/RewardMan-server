# 
# Файл обработки и создания локальной базы данных на основе СУБД SQLite
# 
# 

import sqlite3 as sql
import json

from functions import *
from config import DataBase


def initUsers() -> None:
    '''
    Инициализация базы данных.
    
    Создается база данных - таблица, если такой не существовало, иначе просто подключиться в ней.
    '''
    
    db = sql.connect(DataBase.filePath)
    cursor = db.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT,
    )
    """)

    # сохранить
    db.commit()
    
    return 

if __name__ == '__main__':
    # запускаем для начала инициализацию базы данных
    initUsers()