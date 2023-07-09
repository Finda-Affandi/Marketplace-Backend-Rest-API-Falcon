import psycopg2

instance_name = 'sat-kapita-selekta-b:asia-southeast2:training-kapita-selekta'
port = 5432
db = 'postgres'
user = 'postgres'
password = 'FwF6qfEA5AzlztzG'

param = f"host = '/cloudsql/{instance_name}' port = {port} dbname='{db}' user = '{user}' password = '{password}'"
# param = f"host = 'localhost' port = {port} dbname='{db}' user = '{user}' password = '{password}'"

def select(query = ""):
    try:
        conn = psycopg2.connect(param)
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        conn.commit()
        cursor.close()
        del(conn)
        return data
    except Exception as e:
        print(e)
        return False, print(e)

def insert(query = ""):
    try:
        conn = psycopg2.connect(param)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()
        del(conn)
        return True
    except psycopg2.Error as e:
        print(e)
        return False

def update(query = ""):
    try:
        conn = psycopg2.connect(param)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()
        del(conn)
        return True
    except psycopg2.Error as e:
        print(e)
        return False

def delete(query = ""):
    try:
        conn = psycopg2.connect(param)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()
        del(conn)
        return True
    except psycopg2.Error as e:
        print(e)
        return False