import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="myuser",
    password="mypass",
    database="my_test_db"
    )
# using the cursor() method 
# cursor method is use to  execute the SQL queries
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")