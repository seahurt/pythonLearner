#url:http://www.pythonchallenge.com/pc/def/274877906944.html

#http://www.pythonchallenge.com/pc/def/map.html

import string
table=string.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab') 
text=string.translate('''g fmncwms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq
rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. ''',table)
print text


url=string.translate('map',table)
print url