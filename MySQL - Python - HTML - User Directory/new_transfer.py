#!"C:\Users\Caio Batinga\AppData\Local\Programs\Python\Python38\python.exe"
print("Content-type:  text/html\n\n")
print()
import cgi
print("""<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}

.topnav {
  overflow: hidden;
  background-color: #333;
}

.topnav a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.topnav a:hover {
  background-color: #ddd;
  color: black;
}

.topnav a.active {
  background-color: #4CAF50;
  color: white;
}
</style>
	<style>
body {
  background: #FFFFFF;
}

.content {
  max-width: 500px;
  margin: auto;
  background: white;
  padding: 10px;
}
</style>
<h1> Employee Directory</h1>
	<div class="topnav">
  <a href="page1.html">Home</a>
	<a href="new.html">New Record</a>
  <a href="display.py">View Employees</a>
  <a href="delete.html">Delete Record</a>
  <a href="change.html">Change Record </a>
<a class="active" href="transfer.py">Transfers</a>
<a href="vacation.py">Vacation Request</a>
<a href="new_hire.py">New Hires</a>
</div>
<div class=content>""")

form = cgi.FieldStorage()

name = form.getvalue("name")
office = form.getvalue("office")
destination = form.getvalue("destination")

import mysql.connector

con = mysql.connector.connect(user='caio', password='root', host='localhost', database='directory')
cur = con.cursor()

cur.execute("insert into transfer values(%s,%s,%s)", (name, office, destination))
con.commit()

cur.close()
con.close()

print("<a href='transfer.py' Click here to go back")
print("<h3>Transfer Request Created</h3>")
