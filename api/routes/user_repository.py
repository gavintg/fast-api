from .user_model import UserModel
from .common.base_repository import BaseRepository

class UserRepository(BaseRepository):
    
    def __init__(self):
        super().__init__()
        super().execute('''
            CREATE TABLE IF NOT EXISTS users (
                id MEDIUMINT NOT NULL AUTO_INCREMENT,
                username VARCHAR(1024) NOT NULL,
                password VARCHAR(1024) NOT NULL,
                PRIMARY KEY (id)
            );''')

    def insert(self, user:UserModel) -> int:
        connection = super().get_connection()
        sql = "INSERT INTO `users` (`username`, `password`) VALUES (%s, %s)"
        cursor = connection.cursor()
        cursor.execute(sql, (user.username, user.password))
        connection.commit()
        connection.close()
        return cursor.lastrowid

    def select_by_username(self, username:str) -> UserModel:
        connection = super().get_connection()
        try:
            sql = "SELECT * FROM `users` WHERE `username`=%s"
            cursor = connection.cursor()
            cursor.execute(sql, username)
            id, username, password = cursor.fetchone()
            return UserModel(id=id, username=username, password=password)
        finally:
            connection.close()
