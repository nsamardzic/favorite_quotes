
import mysql.connector
from resources.params import databaseLogin


mydb = mysql.connector.connect(
    host = databaseLogin.dbhost,
    user = databaseLogin.dbuser,
    passwd = databaseLogin.dbpasswd
)

mycursor = mydb.cursor()

# Create database
mycursor.execute("CREATE DATABASE {} character set UTF8 collate utf8_bin".format(databaseLogin.newDatabase))

# Show databases
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print('Databases:', db)


# Use "db_name" database
mycursor.execute("USE {}".format(databaseLogin.newDatabase))

# Create "quotes" table in database
mycursor.execute("CREATE TABLE quotes (id INT AUTO_INCREMENT PRIMARY KEY, external_id INT (10), author CHAR(50), content VARCHAR(355))")

# Create "users" table in database
mycursor.execute("CREATE TABLE users (user_id INT AUTO_INCREMENT PRIMARY KEY, first_name CHAR (20), last_name CHAR (25), email VARCHAR (30), address VARCHAR (125), city CHAR (25), country CHAR (25) )")

# Show table in database
mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print('\nTables:', tb)


mydb.close()
mycursor.close()




