import sqlite3

def setup_database(db_path):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def create_table(conn, table_name, columns):
    cursor = conn.cursor()
    column_str = ', '.join([f'{col} {ctype}' for col, ctype in columns.items()])
    query = f'CREATE TABLE IF NOT EXISTS {table_name} ({column_str})'
    cursor.execute(query)
    conn.commit()

def insert_data(conn, table_name, columns, data):
    cursor = conn.cursor()
    placeholders = ', '.join(['?'] * len(columns))
    query = f'INSERT INTO {table_name} ({", ".join(columns)}) VALUES ({placeholders})'
    cursor.execute(query, list(data.values()))
    conn.commit()

def select_data(conn, table_name, columns, condition=None):
    cursor = conn.cursor()
    query = f'SELECT {", ".join(columns)} FROM {table_name}'
    if condition:
        query += f' WHERE {condition}'
    cursor.execute(query)
    return cursor.fetchall()
