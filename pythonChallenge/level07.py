#oxygen
#url:http://www.pythonchallenge.com/pc/def/oxygen.html
#tips: PIL 
# grey color reflected to ASCII code
#use chr() to change a number to its corresponding ASCII character

from PIL import Image

im=Image.open('oxygen.png')
color=[]
for x in range(0,607,7):
	color.append(chr(im.getpixel((x,45))[0]))
print ''.join(color)


array=[105, 110, 116, 101, 103, 114, 105, 116, 121]

print ''.join(chr(x) for x in array)


#answer is 'integrity'
