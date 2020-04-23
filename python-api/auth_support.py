""" Authentication Support using JWT Tockens """

import hashlib
import jwt
import db_support
import config
from OAuth_Google import quickstart

def md5(string):
    """ Returns Md5 hash of the given string """
    return str(hashlib.md5(string.encode()).digest())

def vaerify_password(username, password):
    """ checks if password is correct for given username """
    db_col = db_support.find_password_by_user_name(username)
    original_password = ""
    try:
        original_password = db_col[0]['password']
    except:
        return False
    given_password = md5(password)
    return original_password == given_password

def generate_jwt(username):
    """ Generats JWT Tocken with given username """
    jwt_token = jwt.encode(payload={"username" : username}, key=config.JWT_SCRET_KEY, algorithm=config.JWT_ALGORITHM).decode()
    print("JWT tocken generated for username - " + str(username) + " - " + str(jwt_token))
    return jwt_token

def get_user_name_from_jwt(jwt_token):
    """ Verify JWT Tocken and return username from it """
    decoded_payload = jwt.decode(jwt=jwt_token.encode(), key=config.JWT_SCRET_KEY, algorithms=[config.JWT_ALGORITHM])
    return decoded_payload['username']

def oAuth_log_in():
    user_email = quickstart.get_email()
    print("Logged in with - " + str(user_email))
    return user_email

