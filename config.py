# 
# Файл с константами и базовыми параметрами приложения
# 


class Server:
    '''
    Конфигурации сервера, для запуска из основного файла.
    '''
    
    def __init__(self) -> None:
        '''
        Конфигурации сервера, для запуска из основного файла.
        '''
        self.ip: str = ""
        self.port: int = 0


class DataBase:
    '''
    Конфигурации работы с базой данных.
    '''
    
    def __init__(self) -> None:
        '''
        Конфигурации работы с базой данных.
        '''
        
        self._fileName: str = "data.db"
        self.filePath: str = f"../{self._fileName}"