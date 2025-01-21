# 
# Файл обработки и создания локальной базы данных на основе СУБД SQLite
# 
# 

import sys
import os

# Добавляем путь к директории, где находится ваш модуль
sys.path.append(os.path.abspath('../'))

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
        email TEXT
    )
    """)

    # сохранить
    db.commit()
    db.close()
    return 

# Проверка уникальности логина
def _checkUniqueLogin(login) -> bool:
    '''
    Проверка уникальности логина
    '''
    
    db = sql.connect(DataBase.filePath)
    cursor = db.cursor()
    
    try:
        cursor.execute(f"""
                SELECT * FROM users WHERE login = {login}
            """)
        
        return len(cursor.fetchall()) == 0
    
    except:
        return True

# Функция создания нового пользователя
def createUser(login:str, password: str) -> None:
    '''
    Функция, создает нового пользователя, используя уникальный логин и пароль
    '''
    
    db = sql.connect(DataBase.filePath)
    cursor = db.cursor()
    
    # форматируем пароль, чтобы обеспечить сохранность
    password = hashPassword(password)
    
    # проверяем логин на уникальность
    if (_checkUniqueLogin(login)):
        cursor.execute("""
            INSERT INTO users(login, password) VALUES (?, ?)
        """, (login, password))
        db.commit()
        
        return "Успешно"
    
    return "Логин занят"

# Функция проверки соответствия пароля и логина пользователя
def checkPassword(login, password) -> bool:
    '''
    Функция проверки соответствия пароля и логина пользователя
    '''
    
    db = sql.connect(DataBase.filePath)
    cursor = db.cursor()
    
    cursor.execute(f"""
            SELECT password FROM users WHERE login = {login}
        """)
    
    return checkPassword(password, cursor.fetchone()[0])

if __name__ == '__main__':
    # запускаем для начала инициализацию базы данных
    initUsers()
    
    createUser("test", "test")
    
    print(checkPassword("test", "test"))