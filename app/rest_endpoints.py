import requests
import json
from rest_api import userParams, headerParams, apiLinks


def userSessionCreate():
    header_data = {
        'Content-Type': headerParams.contentType,
        'Authorization': headerParams.apiToken
    }

    body_data = {
        "user": {
            "login": userParams.userLogin,
            "password": userParams.userPassword,
            "email": userParams.userEmail
        },
    }

    api_url = apiLinks.url_sessionCreate
    api_response = requests.post(api_url, headers=header_data, json=body_data)
    json_data = json.loads(api_response.text)

    tok_ing = json_data['User-Token']  # JSON Data - user token
    stat_code = api_response.status_code  # Status code
    response_text = api_response.text  # Response text
    token_key = (json_data['User-Token'])  # Response token

    print(api_response.url)  # API url
    print(stat_code)  # print status code


def createUser(newUserLogin, newUserEmail, newUserPassword):
    header_data = {
        'Content-Type': headerParams.contentType,
        'Authorization': headerParams.apiToken,
        'Etag': headerParams.etagValue,
        'Accept': headerParams.acceptData
    }

    body_data = {
        "user": {
            "login": newUserLogin,
            "email": newUserEmail,
            "password": newUserPassword
        },
    }

    api_url = apiLinks.url_userCreate
    api_response = requests.post(api_url, headers=header_data, json=body_data)

    print(api_response.url)
    print(api_response.status_code)
    print(api_response.text)


def createNewQuote(quoteAuthor, quoteContent):
    header_data = {
        'Content-Type': headerParams.contentType,
        'Authorization': headerParams.apiToken,
        'User-Token': headerParams.userToken
    }

    body_data = {
        "quote": {
            "author": quoteAuthor,
            "body": quoteContent
        },
    }

    api_url = apiLinks.url_createQuote

    api_response = requests.post(api_url, headers=header_data, json=body_data)

    print(api_response.url)
    print(api_response.status_code)
    print(api_response.text)


def userQuotes():
    header_data = {
        'Content-Type': headerParams.contentType,
        'Authorization': headerParams.apiToken
    }

    api_url = apiLinks.url_userQuotes

    api_response = requests.get(api_url, headers=header_data)

    print(api_response.url)
    print(api_response.status_code)
    print(api_response.text)


def quoteOfTheDay():
    header_data = {
        'Content-Type': headerParams.contentType,
        'Authorization': headerParams.apiToken,
        'User-Token': headerParams.userToken,
        'Etag': headerParams.etagValue,
        'Accept': headerParams.acceptData
    }

    api_url = apiLinks.url_qotd

    api_response = requests.get(api_url, headers=header_data)

    print(api_response.url)
    print(api_response.status_code)
    print(api_response.text)


def quoteSpecific(quoteID):
    header_data = {
        'Content-Type': headerParams.contentType,
        'Authorization': headerParams.apiToken
    }

    api_url = apiLinks.url_userQuotes + '/' + quoteID  # quote ID

    api_response = requests.get(api_url, headers=header_data)

    print(api_response.url)
    print(api_response.status_code)
    print(api_response.text)

# # Create new Quote
# createNewQuote(
#     'Dickenson Mike',                  # Author of the quote
#     'Morning is always the wiser.'     # Quote Content
#     )

# # Create New User
# createUser(
#     'Mickey2',                    # New user login
#     'mickey2@mail.com',           # New user email  
#     'test1234'                    # New user password
#     ) 


# # Create new user session
# userSessionCreate()


# # Get user quotes
# userQuotes()

# # Get Quote of The Day
# quoteOfTheDay()

# # Get Quote by quote ID
# quoteSpecific('1884')
