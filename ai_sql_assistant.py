import requests 
from database import connection, check_table, column_name, commit
from agent import sql_agent


def main():

  connect = connection()
  cursor = connect.cursor()

  convo_history = []

  while True:
    table_name = input('Please Enter name You want to access: ').strip()
    if table_name == 'quit' or table_name == 'q':
      break
    if not check_table(cursor, table_name):
      print('Table doesnt exist')
      continue
    column_names = column_name(cursor, table_name)
    
    while True:
      user_input = input(f'Please Enter What you want to do with {table_name}: ')
      if user_input == 'quit':
        break
      elif user_input == 'commit':
        commit(connect)

      convo_history.append(user_input)
      try:
        sql = sql_agent(table_name, column_names, convo_history, user_input)
        cursor.execute(sql)
        if cursor.description:
          for i in cursor.fetchall():
            print(i)
        else:
          print('Success')
      except Exception as e:
        print(e)

  cursor.close()
  connect.close()


if __name__ == "__main__":
  main()