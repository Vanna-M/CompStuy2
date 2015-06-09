#!/usr/bin/python
# ========= HASHBANG LINE ABOVE IS MAGIC! =========
# ========= (Must be first line of file.) =========
print "Content-Type: text/html\n\n"

import hashlib
import cgi
import cgitb
cgitb.enable()  #diag info --- comment out once full functionality achieved

# ~~~~~~~~~~~~~~~ support functions ~~~~~~~~~~~~~~~
def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import cgi
import cgitb
cgitb.enable()

def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d

d = FStoD()
enteredUser = d['user']
enteredPass = d['pass']
enteredPass2 = d['pass2']
enteredEmail = d['email']

userTaken = '''<!DOCTYPE html>
\n<html>
\n   <head>
\n      <title>SOCIAL NETWORK | Sign Up!</title>
\n   </head>
\n   <body>
\n   <p> <font color=red> Sorry, that username is taken!</p>
\n      <form name="input" method="POST" action="create.py">
\n         <br>
\n         Email:
\n         <input type="text" name="email" placeholder="Email" required>@stuy.edu
\n         <br>
\n         Username:
\n         <input type="text" name="user" placeholder="Username" required>
\n         <br>
\n         Password:
\n         <input type="password" name="pass" placeholder="Password" required>
\n         <br>
\n         Retype Password:
\n         <input type="password" name="pass2" placeholder="RetypePassword" required>
\n         <br>
\n         <input type="submit" value="Sign Up">
\n         <br><br><br>
\n         Already have an account? <a href="index.html">Log in here!</a> 
\n      </form>
\n   </body>
\n</html> '''

emailTaken = '''<!DOCTYPE html>
\n<html>
\n   <head>
\n      <title>SOCIAL NETWORK | Sign Up!</title>
\n   </head>
\n   <body>
\n   <p> <font color=red> Sorry, that email is taken!</p>
\n      <form name="input" method="POST" action="create.py">
\n         <br>
\n         Email:
\n         <input type="text" name="email" placeholder="Email" required>@stuy.edu
\n         <br>
\n         Username:
\n         <input type="text" name="user" placeholder="Username" required>
\n         <br>
\n         Password:
\n         <input type="password" name="pass" placeholder="Password" required>
\n         <br>
\n         Retype Password:
\n         <input type="password" name="pass2" placeholder="RetypePassword" required>
\n         <br>
\n         <input type="submit" value="Sign Up">
\n         <br><br><br>
\n         Already have an account? <a href="index.html">Log in here!</a> 
\n      </form>
\n   </body>
\n</html> '''

nonMatch = '''<!DOCTYPE html>
\n<html>
\n   <head>
\n      <title>SOCIAL NETWORK | Sign Up!</title>
\n   </head>
\n   <body>
\n   <p> <font color=red> Sorry, the passwords do not match!</p>
\n      <form name="input" method="POST" action="create.py">
\n         <br>
\n         Email:
\n         <input type="text" name="email" placeholder="Email" required>@stuy.edu
\n         <br>
\n         Username:
\n         <input type="text" name="user" placeholder="Username" required>
\n         <br>
\n         Password:
\n         <input type="password" name="pass" placeholder="Password" required>
\n         <br>
\n         Retype Password:
\n         <input type="password" name="pass2" placeholder="RetypePassword" required>
\n         <br>
\n         <input type="submit" value="Sign Up">
\n         <br><br><br>
\n         Already have an account? <a href="index.html">Log in here!</a> 
\n      </form>
\n   </body>
\n</html> '''

invalidChars = '''<!DOCTYPE html>
\n<html>
\n   <head>
\n      <title>SOCIAL NETWORK | Sign Up!</title>
\n   </head>
\n   <body>
\n   <p> <font color=red> Sorry, there are invalid characters in your password!</p>
\n      <form name="input" method="POST" action="create.py">
\n         <br>
\n         Email:
\n         <input type="text" name="email" placeholder="Email" required>@stuy.edu
\n         Username:
\n         <input type="text" name="user" placeholder="Username" required>
\n         <br>
\n         Password:
\n         <input type="password" name="pass" placeholder="Password" required>
\n         <br>
\n         Retype Password:
\n         <input type="password" name="pass2" placeholder="RetypePassword" required>
\n         <br>
\n         <input type="submit" value="Sign Up">
\n         Already have an account? <a href="index.html">Log in here!</a> 
\n      </form>
\n   </body>
\n</html> '''

proper = '''<!DOCTYPE html>\n
\n<html>
\n   <head>
\n      <title>SOCIAL NETWORK | You're in!</title>
\n   </head>
\n   <body>
\n   <p>You're in!</p>
\n   </body>
\n</html> '''

invalid = "(){}[]|`!\"$%^&*\'<>:;#~_-+=,@.\\"

def md5Pass(password):#takes a password input and returns a hashed version
    m = hashlib.md5()
    m.update(password)
    return m.hexdigest()

def usercheck():
    userData = open('userInfo.csv', 'r')
    userInfo = userData.readlines()
    userData.close()
    for dataset in userInfo:
        if enteredUser in dataset:
            return userTaken #if you're username exists
        elif enteredEmail in dataset:
            return emailTaken
        else:
            if enteredPass != enteredPass2:
                return nonMatch#you're password's don't match
            else:
                for character in invalid:
                    if character in enteredPass:
                        return invalidChars#you didn't follow the password rules!
                userData = open('userInfo.csv','a')
                userData.write(enteredUser +"," + md5Pass(enteredPass) +"," + enteredEmail+"@stuy.edu" + "\n")
                userData.close()
                return proper#otherwise, you're in

print usercheck()
#p = open("userInfo.csv",'a')
#p.write("username,password,email")
#p.close
