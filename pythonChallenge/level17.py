# http://www.pythonchallenge.com/pc/return/romance.html
# title:eat?
# in this picture there exist a small picture which is also in level 4
# and the picture is called cokies
# so we have to go back to level 4 to check the cokies info
# and it is saying: you should follow busynothing
# since we did the similar thing 
# let's visit http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing
# it is saying: and the next busynothing is 72758
# let's follow up

# from urllib import request
# from urllib.parse import unquote_plus, unquote_to_bytes
# import re
# import bz2
# base = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
# num='12345'
# ref=''
# while(True):
#     url=base+num
#     print(url)
#     page = request.urlopen(url)
#     cont=page.read().decode("utf-8")
#     cookie=page.getheader("Set-Cookie")   # collect the cookie
#     ref+=re.search("info=(.*?);",cookie).group(1)
#     num = re.search("the next busynothing is ([0-9]+)",cont)
#     if num!=None:
#         num=num.group(1)
        
#         continue
#     else:
#         break
# print(cont)
# print(ref)
# info=unquote_to_bytes(ref.replace("+"," "))
# print(bz2.decompress(info))

# we got b'is it the 26th already? call his father and inform him that "the flowers are on their way". he\'ll understand.'
# so we have to go back to level 13 to call the num
# find mozart's father
# his name is Leopold 
# so we got 555-VIOLIN
# we visit http://www.pythonchallenge.com/pc/return/violin.html
# but we got : no! i mean yes! but ../stuff/violin.php.
# so visit http://www.pythonchallenge.com/pc/stuff/violin.php
# we got a picture of his father
# now we have to give this php page a message tell him "the flowers are on their way"
# 
from urllib.request import Request, urlopen
from urllib.parse import quote_plus
url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
msg = "the flowers are on their way"
req = Request(url, headers = { "Cookie": "info=" + quote_plus(msg)})
print(urlopen(req).read().decode("utf-8"))
# # we got:
# <html>
# <head>
#   <title>it's me. what do you want?</title>
#   <link rel="stylesheet" type="text/css" href="../style.css">
# </head>
# <body>
# 	<br><br>
# 	<center><font color="gold">
# 	<img src="leopold.jpg" border="0"/>
# <br><br>
# oh well, don't you dare to forget the balloons.</font>
# </body>
# </html>

# so next level is balloons