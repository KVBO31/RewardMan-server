'''
Хранение дополнительных функций и фитч, которые являются рабочими, 
но в то же время не обязательными в сборке проекта. 

Личное желание.
''' 


import bcrypt

def hashPassword(password):
    '''
    Функция для хеширования пароля
    '''
    # Генерация соли
    salt = bcrypt.gensalt()
    # Хеширование пароля
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

# Функция для проверки пароля
def checkPassword(hashed, password) -> bool:
    '''
    Функция проверки соответсвия пароля и хеша этого пароля
    '''
    
    # Сравнение хешированного пароля с введенным
    return bcrypt.checkpw(password.encode('utf-8'), hashed)