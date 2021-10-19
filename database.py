import psycopg2

def import_to_db(ititle, iurl, istockname, irelease_date):

   #Establishing the connection
   conn = psycopg2.connect(
      database="tradingnews", user='', password='', host='', port= ''
   )
   #Setting auto commit false
   conn.autocommit = True

   #Creating a cursor object using the cursor() method
   cursor = conn.cursor()

   # Preparing SQL queries to INSERT a record into the database.
   cursor.execute('''INSERT INTO tradingnews(title, url, stockname, release_date) VALUES (ititle, iurl, istockname, irelease_date);''')

   # Commit your changes in the database
   conn.commit()
   print("Records inserted........")

   # Closing the connection
   conn.close()
import_to_db("test", 'sifmit.com', 'tests', '2011')