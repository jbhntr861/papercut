import sqlite3

class Database:
    def __init__(self, filename):
        self.conn = sqlite3.connect(filename)
        self.create_table()

    def create_table(self):
        """
        Creates the 'exploit_results' table if it doesn't exist.
        """
        query = '''
            CREATE TABLE IF NOT EXISTS exploit_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT,
                command TEXT,
                result TEXT
            )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def save_result(self, url, command, result):
        """
        Saves the exploit result to the database.
        """
        query = '''
            INSERT INTO exploit_results (url, command, result)
            VALUES (?, ?, ?)
        '''
        self.conn.execute(query, (url, command, result))
        self.conn.commit()

    def close(self):
        """
        Closes the database connection.
        """
        self.conn.close()
