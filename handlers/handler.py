import sqlite3


class DataBase:
    def __init__(self, name_db):
        self.con = sqlite3.connect(name_db)
        self.cur = self.con.cursor()
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users_questions(
                tg_id_user INTEGER,
                question_text_id TEXT,
                photo_id TEXT,
                document_id TEXT
            )
            """
        )
        self.con.close()
