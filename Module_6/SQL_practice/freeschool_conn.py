import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   """ create a database connection to a SQLite database """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       print(f"Connected to {db_file}, sqlite version: {sqlite3.version}")
   except Error as e:
       print(e)
   finally:
       if conn:
           conn.close()

def create_connection_in_memory():
   """ create a database connection to a SQLite database """
   conn = None
   try:
       conn = sqlite3.connect(":memory:")
       print(f"Connected, sqlite version: {sqlite3.version}")
   except Error as e:
       print(e)
   finally:
       if conn:
           conn.close()

if __name__ == '__main__':
   create_connection(r"freeschool.db")
   create_connection_in_memory()

create_instructor_sql = """
-- instructor table
CREATE TABLE IF NOT EXISTS instructor (
  id integer PRIMARY KEY,
  first_name text NOT NULL,
  last_name text,
  description text
);
"""

create_course_sql = """
-- course table
CREATE TABLE IF NOT EXISTS course (
  id integer PRIMARY KEY,
  instructor_id integer NOT_NULL,
  title text NOT NULL,
  description VARCHAR(250) NOT NULL,
  category TEXT,
  language TEXT NOT NULL,
  rating text NOT NULL,
  FOREIGN KEY (instructor_id) REFERENCES instructor (id)
);
"""

def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except Error as e:
       print(e)

   return conn

def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

if __name__ == "__main__":

   create_instructor_sql = """
   -- instrucctor table
   CREATE TABLE IF NOT EXISTS instructor (
    id integer PRIMARY KEY,
    first_name text NOT NULL,
    last_name text,
    description text
   );
   """

   create_course_sql = """
   -- course table
   CREATE TABLE IF NOT EXISTS course (
      id integer PRIMARY KEY,
      instructor_id integer NOT NULL,
      title text NOT NULL,
      description VARCHAR(250) NOT NULL,
      category TEXT,
      language TEXT NOT NULL,
      rating text NOT NULL,
      FOREIGN KEY (instructor_id) REFERENCES instructor (id)
   );
   """

   db_file = "freeschool.db"

   conn = create_connection(db_file)
   if conn is not None:
       execute_sql(conn, create_instructor_sql)
       execute_sql(conn, create_course_sql)
       conn.close()