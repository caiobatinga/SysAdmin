#!"C:\Users\Caio Batinga\AppData\Local\Programs\Python\Python38\python.exe"
print("Content-type:  text/html\n\n")
import cgi
import mysql.connector

con = mysql.connector.connect(user='caio', password='root', host='localhost', database='directory')
cur = con.cursor()

form = cgi.FieldStorage()

id = form.getvalue("id")
password= form.getvalue("password")
sql = "Select username, password from users where username = %s and password = %s"
cur.execute(sql, (id, password))
checkusername = cur.fetchall()
cur.close()
con.close()

if not checkusername:
    print("Invalid login")

else: print("""<meta http-equiv="refresh" content="0; url=http://127.0.0.1/project/page1.html" />""")