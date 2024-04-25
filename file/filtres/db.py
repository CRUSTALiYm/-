import sqlite3
import datetime

class Database:
    def __init__(self, db_file_name):
        self.connection = sqlite3.connect(db_file_name)
        self.cursor = self.connection.cursor()
    
    #Регистрация пользователя
    def user_login(self, id:int, first_name:str, last_name:str):
        with self.connection:
            
            data_reg = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            self.cursor.execute(f"SELECT id FROM users WHERE first_name = ? AND last_name = ?", [first_name, last_name])
            if self.cursor.fetchone() is None:
                #Создание
                self.cursor.execute("INSERT INTO users(id, data_reg, last_name, first_name) VALUES (?, ?, ?, ?)", [id, data_reg, last_name, first_name])
    
    
    # Информация из БД
    def info_user(self, user_id):
        with self.connection:
            try:
                return self.cursor.execute(f"SELECT * FROM users WHERE id = ?", [user_id]).fetchone()
            except:
                return None
    
    #Все id
    def all_user_id(self):
        with self.connection:
            return self.cursor.execute(f"SELECT id FROM users").fetchall()





#Создание базы данных
def creat_databese(db_file_name: str):
    with sqlite3.connect(db_file_name) as db:
        cur = db.cursor()
        
        query = """
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY NOT NULL,
            data_reg VARCHAR,
            last_name VARCHAR NOT NULL,
            first_name VARCHAR NOT NULL,
            admin INTEGER NOT NULL DEFAULT 0
        );
            CREATE TABLE IF NOT EXISTS `in/out`(
            id INTEGER NOT NULL,
            last_name VARCHAR NOT NULL,
            first_name VARCHAR NOT NULL,
            data VARCHAR,
            rez VARCHAR
        )
        """
        cur.executescript(query)
