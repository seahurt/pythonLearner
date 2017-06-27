#http://www.pythonchallenge.com/pc/return/5808.html
#
# this image called "odd even"
# so just remove half piexl we get a new img
from PIL import Image

im = Image.open(r'C:\Users\fyj\Documents\Code\python\pythonLearner\pythonChallenge\cave.jpg')
w, h = im.size
img1 = Image.new('RGB',(w,h),255)
img2 = Image.new('RGB',(w,h//2),(255,255,255))
print (w,h)
img1 = im
imd = list(img1.getdata())

imd_new = [imd[x] for x in range(len(imd)) if x%2==1]
for x in range(50):
    print(imd_new[x])

img2.putdata(imd_new)
img2.show()
#img2.save(r"C:\Users\fyj\Documents\Code\python\pythonLearner\pythonChallenge\cave_2.jpg","JPEG")


# get an img with a word "evil"
# next level is http://www.pythonchallenge.com/pc/return/evil.html