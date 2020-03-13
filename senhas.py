import sqlite3

MASTER_PASSWORD = "123456"

conn = sqlite3.connect('senhas.db')

cursor = conn.cursor()

cursor.executa('''
               CREATE TABLE IF NOT EXIST users (
                   service TEXT NOT NULL,
                   username TEXT NOT NULL,
                   password TEXT NOT NULL    
               );
               ''')