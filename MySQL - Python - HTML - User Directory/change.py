#!"C:\Users\Caio Batinga\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\python.exe"
print("Content-type:  text/html\n\n")
print()
import cgi
import mysql.connector

con = mysql.connector.connect(user='caio', password='root', host='localhost', database='directory')
cur = con.cursor()
form = cgi.FieldStorage()

id = form.getvalue("id")
fullname = form.getvalue("fullname")
jobtitle = form.getvalue("jobtitle")
emergency = form.getvalue("emergency")
address = form.getvalue("address")


sql= "update employees set id = %s, fullname = %s,jobtitle = %s,emergency = %s, address= %s where id = %s"

cur.execute(sql,(id, fullname, jobtitle, emergency, address, id))
con.commit()

cur.close()
con.close()
print("Record updated")