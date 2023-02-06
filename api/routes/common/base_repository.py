import os
import dotenv
import pymysql
from pathlib import Path

class BaseRepository:
    def __init__(self):
        dotenv_path = Path.joinpath(Path(__file__).parent, '../../../.env')
        dotenv.load_dotenv(dotenv_path=dotenv_path)

    def get_host(self):
        return os.getenv('MYSQL_HOST')

    def get_port(self):
        return int(os.getenv('MYSQL_PORT'))

    def get_database(self):
        return os.getenv('MYSQL_DATABASE')

    def get_username(self):
        return os.getenv('MYSQL_USERNAME')

    def get_password(self):
        return os.getenv('MYSQL_PASSWORD')

    def get_connection(self) -> pymysql.Connection:
        return pymysql.connect(
            host=self.get_host(), 
            port=self.get_port(), 
            user=self.get_username(), 
            password=self.get_password(), 
            database=self.get_database())

    def execute(self, sql:str):
        connection = self.get_connection() 
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        connection.close()
