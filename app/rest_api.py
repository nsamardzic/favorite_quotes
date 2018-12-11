

import requests
import json

api_base = 'https://favqs.com/api' # Base link

class apiEndpoints:
    def __init__(self, url_sessionCreate, url_userCreate, url_userLogin, url_qotd, url_userQuotes, url_createQuote):
        self.url_sessionCreate = url_sessionCreate
        self.url_userCreate = url_userCreate
        self.url_userLogin = url_userLogin
        self.url_qotd = url_qotd
        self.url_userQuotes = url_userQuotes
        self.url_createQuote = url_createQuote



class headerData:
    def __init__(self, userToken, apiToken, etagValue, contentType, acceptData):
        self.userToken = userToken
        self.apiToken = apiToken
        self.etagValue = etagValue
        self.contentType = contentType
        self.acceptData = acceptData


class userData:
    def __init__(self, userLogin, userPassword, userEmail):
        self.userLogin = userLogin
        self.userPassword = userPassword
        self.userEmail = userEmail


userParams = userData(
    'execom_test11',               # userLogin
    'password123',                 # userPassword
    'execom.testing@gmail.com'     # userEmail
)


headerParams = headerData(
    'IWO9CwTvhmrNFFkXbdPllTkc4RUJIlHsH6REyK6GiI6mVKkqeyzbXS4zG+xSqqBak7KoOCZGCstOoMAm/LRt0w==',  # userToken
    'Token token=2fac29a69309e3d566df7ece3ce79dc5',                                              # apiToken
    '558f0b9bea2e6910b1f93de7f4c0d47c',                                                          # etagValue
    'application/json',                                                                          # contentType
    'application/vnd.favqs.v2+json'                                                              # acceptData
    )


# API Endpoints
apiLinks = apiEndpoints(
    '{}/session'.format(api_base),         # 01_POST_session_create
    '{}/users'.format(api_base),           # 02_POST_create_user
    '{}/users/:login'.format(api_base),    # 03_GET_users_login
    '{}/qotd'.format(api_base),            # 04_GET_qotd
    '{}/quotes'.format(api_base),          # 05_GET_user quotes
    '{}/quotes'.format(api_base)           # 07_POST_create quote

) 




