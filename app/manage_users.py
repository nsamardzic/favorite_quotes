import mysql.connector
from params import databaseLogin, newUser, removeAccount

mydb = mysql.connector.connect(
    host=databaseLogin.dbhost,
    user=databaseLogin.dbuser,
    passwd=databaseLogin.dbpasswd,
    database=databaseLogin.activeDatabase
)

mycursor = mydb.cursor()

# Use "db_name" database
mycursor.execute("USE {}".format(databaseLogin.activeDatabase))


# Create new user in database
def createNewUser():
    newUser_SQL = "INSERT INTO users (first_name, last_name, email, address, city, country) VALUES (%s, %s, %s, %s, %s, %s)"
    newUserInfo = (
        newUser.accountFirstName,
        newUser.accountLastName,
        newUser.accountEmail,
        newUser.accountAddress,
        newUser.accountCity,
        newUser.accountCountry
    )

    mycursor.execute(newUser_SQL, newUserInfo)

    print(
        'User created with following credentials:\nFirstName: {},\nLastName: {},\nEmail: {},\nAddress: {},\nCity: {},\nCountry: {}'.format(
            newUser.accountFirstName,
            newUser.accountLastName,
            newUser.accountEmail,
            newUser.accountAddress,
            newUser.accountCity,
            newUser.accountCountry
        ))

    mydb.commit()  # Actually writing to database
    mydb.close()  # Closing DB connection
    mycursor.close()  # Closing DB connection


# Delete user by ID
def deleteUserByID(userRemoveID):
    # accountDeleteById_SQL = "DELETE FROM users WHERE user_id = {}".format(removeAccount.user_id)
    accountDeleteById_SQL = "DELETE FROM users WHERE user_id = {}".format(userRemoveID)
    mycursor.execute(accountDeleteById_SQL)

    print("\nUser with USER_ID: {} is successfully deleted".format(userRemoveID))

    mydb.commit()  # Actually writing to database
    mydb.close()  # Closing DB connection
    mycursor.close()  # Closing DB connection


# Delete user by EMAIL
def deleteUserByEmail(userRemoveEmail):
    # accountDeleteByEmail_SQL = "DELETE FROM users WHERE email = '{}'".format(removeAccount.user_email)
    accountDeleteByEmail_SQL = "DELETE FROM users WHERE email = '{}'".format(userRemoveEmail)
    mycursor.execute(accountDeleteByEmail_SQL)

    print("\nUser with EMAIL: {}\nis successfully deleted".format(userRemoveEmail))

    mydb.commit()  # Actually writing to database
    mydb.close()  # Closing DB connection
    mycursor.close()  # Closing DB connection


# Delete user by First_Name
def deleteUserByFirstName(userRemoveFirstName):
    # accountDeleteByFirstName_SQL = "DELETE FROM users WHERE first_name = '{}'".format(removeAccount.user_first_name)
    accountDeleteByFirstName_SQL = "DELETE FROM users WHERE first_name = '{}'".format(userRemoveFirstName)
    mycursor.execute(accountDeleteByFirstName_SQL)

    print("\nUser with FIRST_NAME: {}\nis successfully deleted".format(removeAccount.user_first_name))

    mydb.commit()  # Actually writing to database
    mydb.close()  # Closing DB connection
    mycursor.close()  # Closing DB connection

# createNewUser()

# deleteUserByID('33')
# deleteUserByEmail('someaddress21@gmail.com')
# deleteUserByFirstName('Ime1')
