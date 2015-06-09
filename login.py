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




d = FStoD()

def md5Pass(password):#takes a password input and returns a hashed version
    m = hashlib.md5()
    m.update(password)
    return m.hexdigest()

enteredUser = d['user']
enteredPass = d['pass']
enteredPass = md5Pass(enteredPass)

proper = '''<!DOCTYPE html>\n
<html>\n
   <head>\n
      <title>SOCIAL NETWORK | Log In</title>\n
   </head>\n
   <body>\n
   <p><font color="red">You did it!!!</font></p>\n
      <form name="input" method="POST" action="login.py">\n
         Username:\n
         <input type="text" name="user" placeholder="" required>\n
         <br>\n
         Password:\n
         <input type="password" name="pass" placeholder="" required>\n
         <br>\n
         <input type="submit" value="Log In"\n
         <br><br><br>\n
         <a href="create.html">Sign Up Here</a> \n
      </form>\n
   </body>\n
</html> '''

wrongPass = '''<!DOCTYPE html>\n
<html>\n
   <head>\n
      <title>SOCIAL NETWORK | Log In</title>\n
   </head>\n
   <body>\n
   <p><font color="red">Password does not match username. Try again.</font></p>\n
      <form name="input" method="POST" action="login.py">\n
         Username:\n
         <input type="text" name="user" placeholder="" required>\n
         <br>\n
         Password:\n
         <input type="password" name="pass" placeholder="" required>\n
         <br>\n
         <input type="submit" value="Log In"\n
         <br><br><br>\n
         <a href="create.html">Sign Up Here</a> \n
      </form>\n
   </body>\n
</html> '''

noUser = '''<!DOCTYPE html>\n
<html>\n
   <head>\n
      <title>SOCIAL NETWORK | Log In</title>\n
   </head>\n
   <body>\n
   <p><font color="red">You do not exist. Register in the link below. </font></p>\n
      <form name="input" method="POST" action="login.py">\n
         Username:\n
         <input type="text" name="user" placeholder="" required>\n
         <br>\n
         Password:\n
         <input type="password" name="pass" placeholder="" required>\n
         <br>\n
         <input type="submit" value="Log In"\n
         <br><br><br>\n
         <a href="create.html">Sign Up Here</a> \n
      </form>\n
   </body>\n
</html> ''' 

def usercheck():
    userData = open('userInfo.csv', 'r')
    userInfo = userData.readlines()
    userData.close()
    for dataset in userInfo:
        if enteredUser in dataset:#if your username exists
            if dataset[1] == enteredPass:#if you check out
                return proper #you're in
            else:
                return wrongPass#wrong password
    #else:#your username doesn't exist
    return noUser
    
print usercheck()
