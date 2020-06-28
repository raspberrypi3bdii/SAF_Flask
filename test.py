from database import  MyDatabase

sqlite = MyDatabase("sqlite","admin","admin","saf_flask_db.db")

print(sqlite)

sqlite.create_db_tables()