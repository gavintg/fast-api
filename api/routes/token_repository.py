from .common.base_repository import BaseRepository

class TokenRepository(BaseRepository):
    
    def __init__(self):
        super().__init__()
        super().execute('''
            CREATE TABLE IF NOT EXISTS tokens (
                id VARCHAR(36) NOT NULL,
                expiry DATETIME NOT NULL,
                PRIMARY KEY (id)
            );''')

    def insert_token(self) -> str:
        connection = super().get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT replace(uuid(),'-','')")
            id_result = cursor.fetchone()
            sql = "INSERT INTO `tokens` (`id`, `expiry`) VALUES (%s, NOW() + INTERVAL 1 HOUR);"
            cursor = connection.cursor()
            cursor.execute(sql, id_result[0])
            connection.commit()
            return id_result[0]
        except:
            return None
        finally:
            connection.close()

    def validate_token(self, token:str) -> bool:
        connection = super().get_connection()
        try:
            sql = "SELECT `id`, `expiry` FROM `tokens` WHERE `id`=%s AND `expiry` > NOW()"
            cursor = connection.cursor()
            cursor.execute(sql, token)
            result = cursor.fetchone()
            return result[0] == token
        except:
            return None
        finally:
            connection.close()
