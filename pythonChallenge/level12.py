#http://www.pythonchallenge.com/pc/return/evil.html
# title dealing evil
# contain a jpg called "evil1,jpg"
# so try http://www.pythonchallenge.com/pc/return/evil2.jpg
#  we got a img saying: not jpg gfx 
# so we try evil2.gfx
# it's an binary file
# try evil3.jpg we got a img saying: no more evil
# try evil4.jpg we got a error img, but in the http head, we got 
# a msg: Bert is evil! go back!
# so we have to deal with the gfx file
# in the evil1.jpg, each pile of card are five
# so we try to split the gfx in to five img



dat = open(r"C:\Users\fyj\Documents\Code\python\pythonLearner\pythonChallenge\evil2.gfx","rb").read()

for x in range(5):
    open(r"C:\Users\fyj\Documents\Code\python\pythonLearner\pythonChallenge\%d.jpg" %x,"wb").write(dat[x::5])


# we got 5 img
# dis
# pro
# port
# ional
# ity with
# disproportional