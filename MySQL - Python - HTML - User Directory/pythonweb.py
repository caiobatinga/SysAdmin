#!"C:\Users\Caio Batinga\AppData\Local\Programs\Python\Python38\python.exe"
print("Content-type:  text/html\n\n")
print()
import cgi

print("<h1> Employee Directory</h1>")
print("<hr/>")
print("<h1> Data</h1>")
print("<body bgcolor='red'>")

form = cgi.FieldStorage()

id = form.getvalue("id")
fullname = form.getvalue("fullname")
jobtitle = form.getvalue("jobtitle")
emergency = form.getvalue("emergency")
address = form.getvalue("address")

import mysql.connector

con = mysql.connector.connect(user='caio', password='root', host='localhost', database='directory')
cur = con.cursor()

cur.execute("insert into employees values(%s,%s,%s,%s,%s)", (id, fullname, jobtitle, emergency, address))
con.commit()

cur.close()
con.close()

print("<a href='http://localhost/project/index.html' Click here to go back")
print("<h3>Employee record created</h3>")

