#!"C:\Users\Caio Batinga\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\python.exe"
print("Content-type:  text/html\n\n")
print()
import cgi
import mysql.connector

form = cgi.FieldStorage()
con = mysql.connector.connect(user='caio', password='root', host='localhost', database='directory')
cur = con.cursor()

id = (form.getvalue("id"),)

sql="delete from employees where id = %s"

cur.execute(sql, id)
con.commit()

cur.close()
con.close()

print("<h2>Record deleted successfully</h2>")