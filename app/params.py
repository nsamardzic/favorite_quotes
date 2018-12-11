

class db_params:
    def __init__(self, dbhost, dbuser, dbpasswd, activeDatabase, newDatabase):
        self.dbhost = dbhost
        self.dbuser = dbuser
        self.dbpasswd = dbpasswd
        self.activeDatabase = activeDatabase
        self.newDatabase = newDatabase
        


class accountUsers:
    def __init__(self, accountFirstName, accountLastName, accountEmail, accountAddress, accountCity, accountCountry):
        self.accountFirstName = accountFirstName
        self.accountLastName = accountLastName
        self.accountEmail = accountEmail
        self.accountAddress = accountAddress
        self.accountCity = accountCity
        self.accountCountry = accountCountry


# Database login parameters
databaseLogin = db_params(
    'localhost',    # mysql host adderss
    'ime',          # mysql username
    'root',         # mysql password
    'test_db',      # mysql database name - Active database
    'test_db4'       # mysql database name - New Database name that you want to create
    )
  

# Create new user parameters
newUser = accountUsers(
    'Petar',                       # user Firs name
    'Petrovic',                   # user Last name
    'ppetrovic@gmail.com',     # user Email
    'street 22',          # user address
    'Surcin',                  # user city
    'Serbia'                     # user country
    )


removeAccount = deleteUser(
    '9',                        # User ID
    'someaddress4@gmail.com',    # User Email
    "Ime1"                       # User First name
    ) 






