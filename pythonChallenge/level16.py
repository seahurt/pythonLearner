# http://www.pythonchallenge.com/pc/return/mozart.html
# the title: let me get this straight
# each line contained pink dot
# we need to rotate each line, to make the dots to one line
# find the pink dot's color code is 195
# use image.getpixel to get the color value

from PIL import Image,ImageChops
im = Image.open(r"C:\Users\fyj\Documents\Code\python\pythonLearner\pythonChallenge\mozart.gif")
nrow=im.size[1]
lenrow=im.size[0]
for y in range(nrow):
    for x in range(lenrow):
        if im.getpixel((x,y))==195:
            box=(0,y,lenrow,y+1)
            ibox=im.crop(box)
            #byts=ibox.tobytes()
            #x=ibox.index(195)
            ibox=ImageChops.offset(ibox,-x+1)              # core code!!!!
            im.paste(ibox,box)
            break
im.show()

# we got a picture saying: romance

