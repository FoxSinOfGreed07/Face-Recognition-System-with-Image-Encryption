import sqlite3
conn = sqlite3.connect("myData.db")
c = conn.cursor()

c.execute("""CREATE TABLE Details (
        fname text,
        lname text,
      email text,
      question text,
         answer text,
          username text,
           password text)"""
           )
conn.commit()
conn.close()
