import hmac
import hashlib
import base64
import re # regular expression

SECRET = '5a7440da-437a-4b7a-9812-50fddbb7a6a8'

def hash_password(password):
    return hmac.new(SECRET.encode('utf-8'), password.encode('utf-8')).hexdigest()

def signup_validate(phone, email, first_name, last_name, password, confirm_password):
    
    # check phone
    if not phone_valid(phone): return False
    # check email
    if not email_valid(email): return False
    # check first name and last name
    if not (first_name and last_name): return False
    # check password
    if not check_password(password, confirm_password): return False
    return True

def phone_valid(phone):
    if len(phone) <= 15 and phone.isdigit():
        return True
    else:
        return False
    
def email_valid(email):
  return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

def check_password(password, confirm_password):
    print(password)
    print(confirm_password)
    if not password == confirm_password:
        return False
    if len(password) < 6:
        return False
    return True
