"""-----------------------------------------------------------
Name             : Favorite Quotes - Get specific Quote (based on Quote ID)
Description      :
Created By       : Nenad Samardzic
License          : GNU GENERAL PUBLIC LICENSE Version 3,
Date:            : September 2018
Powered          : Python-3.7

-----------------------------------------------------------"""

from rest_api import apiLinks, userParams, headerParams
from params import databaseLogin
import requests
import mysql.connector
import time

# Database connector parameters
mydb = mysql.connector.connect(
    host = databaseLogin.dbhost,
    user = databaseLogin.dbuser,
    passwd = databaseLogin.dbpasswd,
    database = databaseLogin.activeDatabase
)


# Header content for REQUEST
header_data = {
    'Content-Type': header_content_type,
    'Authorization': api_token
    }

# set start & end value for the request ID to be targeted
start_value = 20001
end_value = 22000

# Defining the range (set by start/end value) for the request ID to be targeted
while start_value <= end_value:
    mycursor = mydb.cursor()
    api_url = '{}/{}'.format(url_user_quotes, start_value) # quote ID
    start_value += 1

    # Storing the JSON response from request
    api_response = requests.get(api_url, headers = header_data )
    response_data = json.loads(api_response.text)

    if api_response.status_code == 200:
        # Handling of multipart response containing several same fields
        if 'lines' in response_data:
            print('Unable to parse this response - Skiping...')
            continue
        # Handling of data content that is bigger than db row for storing data - VARCHAR(355)
        elif (len(response_data['body'])) > 350:
            print('Data content too long - Skiping...')
            continue
        else:
            # Message for the user Succesfull server response 200
            print(api_response.url + ' - Success: server returned {}'.format(api_response.status_code))

            # Script part for inserting retrieved data to database
            sqlFormula = "INSERT INTO quotes (external_id, author, content) VALUES (%s, %s, %s)"
            dataSet = (response_data['id'], response_data['author'], response_data['body'])
            mycursor.execute(sqlFormula, dataSet)

            # Inserted wait/sleep timeout
            time.sleep(1) # Waits 1 seconds.

    # Handling of server 404 error code - not found
    elif api_response.status_code == 404:
        print(api_response.url + ' - Content not available: server returned {}'.format(api_response.status_code))

        # Inserted wait/sleep timeout
        time.sleep(1) # Waits 1 seconds.
    else:
        continue

    # Actually writing to database
    mydb.commit()
