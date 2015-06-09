#!/usr/bin/python
# ========= HASHBANG LINE ABOVE IS MAGIC! =========
# ========= (Must be first line of file.) =========
print "Content-Type: text/html\n\n"

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
actualPost = d["post"]

def htmlify(code):
    header = "<!DOCTYPE><html> \n<header><title>Formalizing</title></header> \n<body bgcolor=#66CCFF>"
    footer = "</body>\n</html>"#default HTML stuff
    return header + code + footer

def formatting(post):
    thisPost = post
    post = post.split(" ")
    counter =  0
    for i in post:
        if i == "bold":
            post[counter] = "<b>"
        if i == "endbld":
            post[counter] = "</b>"
        if i == "und":
            post[counter] = "<u>"
        if i == "endun":
            post[counter] = "</u>"
        if i == "ita":
            post[counter] = "<i>"
        if i == "endit":
            post[counter] = "</i>"
        counter += 1
    return " ".join(post)

#print formatting('f is for friends bold who endbld do stuff')

def addPost(post,location):
    newPost = formatting(d['post'])#add the bolding, italics, etc.
    instream = open(location,'a+r')
    instream.write("<p>" + newPost + "</p>")#add this formated text to the Newsfeed
    return instream

def continuePost(post):
    p = d.keys()
    boldSet = ""
    italicSet = ""
    underlineSet = ""
    if "bold" in p:
        boldSet = " bold "
    if "endbld" in p:
        boldSet = " endbld "
    if "und" in p:
        underlineSet = " und "
    if "endun" in p:
        underlineSet = " endun "
    if "it" in p:
        italicSet = " ita "
    if "endita" in p:
        italicSet = " endit "
    return '''<!DOCTYPE html>\n
<html> \n
<header><title>Make a Post</title></header> \n
<body> \n
    <form name="input" method="POST" action="posting.py" required>
        <input type="text" name="post" value="'''+str(actualPost)+boldSet + italicSet + underlineSet+'''">\n
        <p> <input type="submit" name="bold" value="Bold"><br>\n
            <input type="submit" name="endbld" value="End Bold"><br>\n
    		<input type="submit" name="und" value="Underline"><br>\n
            <input type="submit" name="endun" value="End Underline"><br>\n
            <input type="submit" name="ita" value="Italicize"><br>\n
            <input type="submit" name="endit" value="End Italics"><br>\n
            <input type="submit" name="fred" value="Submit">\n
    </form>\n
    \n
</body>\n
</html>'''#the code for our html page, returns w/first part of your post


def processingPost(post,location):
    retString = ""
    ThisPost = open("ThisPost.csv","r+a+w")#read, append, write
    ThisPost.write(actualPost)#add your post to the end
    if "fred" in d.keys():#if you submitted, not bolded
        addPost(ThisPost,location)#fullPost is the entirety of the Newsfeed
        fullPost = open(location,"r")
        for i in fullPost:
            retString += "<p>" + i + "</p>" #add all previous posts (but new post is at the end)
        ThisPost.write("")#clear ThisPost (resets for next post)
        fullPost.close
        located = open(location,"r")#open entirety of your Newsfeed (or other location)
        located = located.readlines()
        return htmlify(str(located))#return the entire newsfeed
    else:
        return continuePost(ThisPost)#else, continue writing your post
            
print processingPost(actualPost,"Newsfeed.csv")


