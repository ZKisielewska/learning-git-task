import sqlite3

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
   except sqlite3.Error as e:
       print(e)
   return conn

def add_instructor(conn, instructor):
   """
   Create a new instrudctor into the instructor table
   :param conn:
   :param instructor:
   :return: instructor id
   """
   sql = '''INSERT INTO instructor(first_name, last_name, description)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, instructor)
   conn.commit()
   return cur.lastrowid

def add_course(conn, course):
   """
   Create a new course into the course table
   :param conn:
   :param task:
   :return: course id
   """
   sql = '''INSERT INTO course(instructor_id, title, description, category, language, rating )
             VALUES(?,?,?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, course)
   conn.commit()
   return cur.lastrowid

if __name__ == "__main__":
    instructor1 = ("Michael", "Nigel", "Developer")
    instructor2 = ("Jason", "Nesbo", "DevOps")
    instructor3 = ("Mark", "Stone", "Data Scienist")

    conn = create_connection("freeschool.db")
    instructor_id = add_instructor(conn, instructor1)
    instructor_id = add_instructor(conn, instructor2)
    instructor_id = add_instructor(conn, instructor3)

    course1 = (
       instructor_id,
       "Python basic",
       "basic course",
       "basic",
       "python",
       "5"
   )

    course2 = (
       instructor_id,
       "Java advanced",
       "advanced course",
       "adanced",
       "java",
       "8"
   )
    
course3 = (
       instructor_id,
       "SQL exercises ",
       "practice course",
       "basic",
       "SQL",
       "6"
   )

course_id = add_course(conn, course1)
course_id = add_course(conn, course2)
course_id = add_course(conn, course3)

print(instructor_id, course_id)
conn.commit()