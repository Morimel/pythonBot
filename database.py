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
                    cleaning INTEGER,
                    date DATE,
                    complaints TEXT
                )
            """)
            
            conn.execute("""
                CREATE TABLE IF NOT EXISTS dishes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    price TEXT,
                    weight TEXT, 
                    description TEXT, 
                    photo TEXT,
                    category TEXT
                )
            """)
            conn.commit()
    
    def save_table(self, user_data: dict):
        try:
            with sqlite3.connect(self.path) as conn:
                conn.execute(
                    """
                    INSERT INTO database_table (name, number, cleaning, date, complaints)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (user_data["name"], user_data["number"], user_data["cleaning"], user_data["date"], user_data["complaints"])
                )
                conn.commit()
                print("Данные успешно сохранены в базу данных.")
        except Exception as e:
            print(f"Ошибка при сохранении данных: {e}")

    def save_dishes(self, user: dict):
        try:
            with sqlite3.connect(self.path) as conn:
                conn.execute(
                    """
                    INSERT INTO dishes (name, price, weight, description, photo, category)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (user["name"], user["price"], user["weight"], user["description"], user["photo"], user["category"])
                )
                conn.commit()
                print("Данные успешно сохранены в базу данных.")
        except Exception as e:
            print(f"Ошибка при сохранении данных: {e}")
        
    def get_all_dishes(self):
        with sqlite3.connect(self.path) as conn:
            result = conn.execute("SELECT * from dishes")
            result.row_factory = sqlite3.Row
            data = result.fetchall()
            return [dict(row) for row in data]