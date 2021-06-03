#!"C:\Users\Caio Batinga\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\python.exe"
print("Content-type:  text/html\n\n")
print()
import cgi
import mysql.connector
from tabulate import tabulate

con = mysql.connector.connect(user='caio', password='root', host='localhost', database='directory')
cur = con.cursor()
form = cgi.FieldStorage()

username = form.getvalue("id")
fullname = form.getvalue("fullname")
jobtitle = form.getvalue("jobtitle")
emergency = form.getvalue("emergency")
address = form.getvalue("address")


sql= (id, fullname, jobtitle, emergency, address, id)

cur.execute("update employees set values (%s,%s,%s,%s,%s) where id = %s", sql)
con.commit()

cur.close()
con.close()
