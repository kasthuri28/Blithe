import psycopg2

def db():
    conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    return cur
