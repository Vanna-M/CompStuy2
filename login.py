#!/usr/bin/python
# ========= HASHBANG LINE ABOVE IS MAGIC! =========
# ========= (Must be first line of file.) =========

import os
import cgi
import cgitb
cgitb.enable()  #diag info --- comment out once full functionality achieved

 #####################################################
 ## Back-End Script for USER ACCOUNT CREATION
 ## by
 ##   ___|  |             |                            
 ##  |      |  |   |   _` |   _ \                      
 ##  |      |  |   |  (   |   __/                      
 ## \____| _| \__, | \__,_| \___|                      
 ##  | ) __ __|__|/     |          _|   _|         | ) 
 ## V V     |    __ \   |  |   |  |    |    |   | V V  
 ##         |    | | |  |  |   |  __|  __|  |   |      
 ##        _|   _| |_| _| \__,_| _|   _|   \__, |      
 ##   ___|  _)               |        _)   ____/       
 ## \___ \   |  __ \    __|  |   _` |  |   __|         
 ##       |  |  |   |  (     |  (   |  |  |            
 ## _____/  _| _|  _| \___| _| \__,_| _| _|            
 #####################################################


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


# ~~~~~~~~~~~~~~~ auxiliary files ~~~~~~~~~~~~~~~~~
#file to store users and their passwords:
userfile="users.csv"

#file to store users currently logged in:
currentUsersFile="loggedin.csv" 

#login page:
loginPage="login.html" 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#store querystring var/val pairs in dictionary
fsd=FStoD()


#validate user input
def valid():
    if not ('uname' in fsd) or not ('upass1' in fsd) or not ('upass2' in fsd):
        return False    
    if fsd['uname'] == '':
        return False
    if fsd['upass1'] != fsd['upass2']:
        return False
    return True


#check for existence of a user in CSV file
def userExists(u):
    try:
        userlist = open(userfile,'r').readlines()
    except:
        return False
    for row in userlist:
        if row.strip().split(',')[0]==u:
            return True
    return False


#create a user, as long as she does not yet exist
def createUser(u,p):
    u = u.lower()
    if userExists(u):
        return False
    try: 
        f = open(userfile,'a')
        f.write(u + "," + p + "\n")
        f.close()
    except:
        return False
    return True

#create a profile page for this user
def createProfile(name):
    user = str(name)
    userFile = user +".html"
    userFile = open(userFile,'w')#creates a new file with the name userFile
    userFile.write('''<!DOCTYPE html>
    <html> 
    <header><title>''' + user + '''</title></header> 
    <body> ''' + user + '''s profile page</body>
    </html>''')
    userFile.close()

# ========= CONTENT-TYPE LINE REQUIRED. ===========
# ======= Must be beginning of HTML string ======== 
htmlStr = "Content-Type: text/html\n\n" #NOTE there are 2 '\n's !!! 
htmlStr += "<html><head><title> User Account Creation Results </title></head></html>\n"
htmlStr += "<body>"

# ~~~~~~~~~~~~~ HTML-generating code ~~~~~~~~~~~~~~
#htmlStr += "<h4>Dictionary of form data:</h4>"
#htmlStr += str( fsd )
#htmlStr += str( userExists(fsd[uname]) )
if not valid():
    htmlStr += "invalid input"
else:
    if createUser( fsd['uname'], fsd['upass1'] ):
        htmlStr += "<h3>Account created. You're in!</h3>"
        htmlStr += '<br>Click <a href="'+ loginPage + '">'
        htmlStr += "here</a> to log in."
        createProfile( fsd['uname'])
    else:
        htmlStr += '<br> Account creation failed. Username taken. Click back or click <a href=createAcct.html> here </a> to try again <p> Already have an account? Log in <a href=login.html> here!</a></p>'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


htmlStr += "</body></html>"


print htmlStr
