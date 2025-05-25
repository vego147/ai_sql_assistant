import psycopg2
import os 
from dotenv import load_dotenv

def connection():
  return psycopg2.connect(
         host = os.getenv('DB_HOST'),
         port =os.getenv('DB_PORT'),
         user =os.getenv('DB_USER'),
         database = os.getenv('DB_NAME'),
         password = os.getenv('DB_PASSWORD')
         )


def column_name(cur,table_name):
   cur.execute(f'SELECT * FROM {table_name} LIMIT 0')
   return[desc[0] for desc in cur.description]


def check_table(cur, table_name):
   cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
   tables = [row[0] for row in cur.fetchall()]
   return table_name in tables


def commit(connection):
   connection.commit()
   print('Databse Updated')