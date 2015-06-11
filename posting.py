#!/usr/bin/python
print "Content-Type: text/html\n\n"

import cgi, cgitb, datetime
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
actualPost = d["postText"]

def htmlify(code):
    header = "<!DOCTYPE><html> \n<header><title>User | Post</title></header> \n<body>\n <h3>User's Newsfeed</h3>\n"
    footer = "</body>\n</html>"#default HTML stuff
    return header + code + footer

def addPost(post,location):
    instream = open(location,'a+r')
    instream.write("<div>" + post + "</div><br><br>\n")#add this formated text to the Newsfeed
    instream.close()

def processingPost(post,location):
    retStr = ""
    addPost(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')+" "+post, location)
    located = open(location,"r")#open entirety of your Newsfeed (or other location)
    located = located.readlines()
    for entry in located:
        retStr = entry + retStr
    return htmlify(retStr)#return the entire newsfeed

print processingPost(actualPost,"Newsfeed")
