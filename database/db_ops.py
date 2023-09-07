```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:')       
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def close_connection(conn):
    conn.close()

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_data(conn, table, data):
    try:
        c = conn.cursor()
        c.execute(f"INSERT INTO {table} VALUES({data})")
        conn.commit()
    except Error as e:
        print(e)

def select_data(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
        rows = c.fetchall()
        return rows
    except Error as e:
        print(e)

def update_data(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
        conn.commit()
    except Error as e:
        print(e)

def delete_data(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
        conn.commit()
    except Error as e:
        print(e)
```