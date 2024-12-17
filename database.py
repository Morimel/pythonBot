import sqlite3

class Database:
    def __init__(self, path: str):
        self.path = path    
        
    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS database_table (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    number TEXT,
                    cleaning TEXT,
                    complaints TEXT
                )
            """)
            
            conn.execute("""
                CREATE TABLE IF NOT EXISTS food (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    price TEXT,
                    weight TEXT
                )
            """)
            conn.commit()
    
    def save_table(self, user_data: dict):
        try:
            with sqlite3.connect(self.path) as conn:
                conn.execute(
                    """
                    INSERT INTO database_table (name, number, cleaning, complaints)
                    VALUES (?, ?, ?, ?)
                    """,
                    (user_data["name"], user_data["number"], user_data["cleaning"], user_data["complaints"])
                )
                conn.commit()
                print("Данные успешно сохранены в базу данных.")
        except Exception as e:
            print(f"Ошибка при сохранении данных: {e}")

    def save_food(self, user: dict):
        try:
            with sqlite3.connect(self.path) as conn:
                conn.execute(
                    """
                    INSERT INTO food (name, price, weight)
                    VALUES (?, ?, ?)
                    """,
                    (user["name"], user["price"], user["weight"])
                )
                conn.commit()
                print("Данные успешно сохранены в базу данных.")
        except Exception as e:
            print(f"Ошибка при сохранении данных: {e}")