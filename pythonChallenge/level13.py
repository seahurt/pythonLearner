# http://www.pythonchallenge.com/pc/return/disproportional.html
# title: call him
# a img of a dial
# num 5 in the img is clickable
# click it and we get a XML error page,the url is a php page
# url: http://www.pythonchallenge.com/pc/phonebook.php
# so we use xmlrpc to process this page
#

import xmlrpc.client

connect = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

# we have to know how to communicate with the server
# use connect.system.listMethods() to show the useable method
# we got a method called "phone"
# then we have to know how to use, use connect.system.methodHelp("phone") 
# and connect.system.methodSignature("phone")
# we get two msg
# 1. 'return the phone of a person'
# 2. [['string','string]]
# so we have to pass a person's name to get the useful msg
# try connect.phone('evil'), we got "he is not the evil"
# last level, we got a msg :"Bert is evil! go back!"
# so we try this name
print(connect.phone('Bert'))
# we get the msg: "555-ITALY"
# try 555-ITALY.html we get 404
# try ITALY.html we get a msg:SMALL letters
# try italy.html we get next level

# level 17
print(connect.phone('Leopold'))