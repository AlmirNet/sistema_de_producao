import sqlite3

conn = sqlite3.connect('production_orders.db')
cursor = conn.cursor()

# Criação da tabela de ordens de produção
cursor.execute('''
    CREATE TABLE IF NOT EXISTS production_orders (
               order_id INTEGER PRIMARY KEY,
               product_name TEXT,
               quantity INTEGER,
               delivery_date TEXT,
               status TEXT
    )
''')

conn.commit()