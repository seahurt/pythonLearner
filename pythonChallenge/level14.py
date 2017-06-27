#http://www.pythonchallenge.com/pc/return/italy.html
# in the source file: <!-- remember: 100*100 = (100+99+99+98) + (...  -->
# there is an image<10000x1>, which should be the one we should manipulate
# 

from PIL import Image

im = Image.open(r'C:\Users\fyj\Documents\Code\python\pythonLearner\pythonChallenge\wire.png')
#imd = list(im.getdata())

nim = Image.new('RGB',(100,100))
p = 0
x=-1
y=0
for i in range(200,0,-1):
    if i%4==0:
        v=(1,0)
    if i%4==3:
        v=(0,1)
    if i%4==2:
        v=(-1,0)
    if i%4==1:
        v=(0,-1)
    for j in range(i//2,0,-1):
        x+=v[0]
        y+=v[1]
        nim.putpixel((x,y),im.getpixel((p,0)))
        p+=1
nim.show()


# from PIL import Image
# im = Image.open(r'C:\Users\fyj\Documents\Code\python\pythonLearner\pythonChallenge\wire.png')
# delta = [(1,0),(0,1),(-1,0),(0,-1)]
# out = Image.new('RGB', [100,100])
# x,y,p = -1,0,0
# d = 200 
# while d/2>0:
#     for v in delta:
#         steps = d // 2
#         for s in range(steps):
#             x, y = x + v[0], y + v[1]
#             out.putpixel((x, y),im.getpixel((p,0)))
#             p += 1
#         d -= 1
# out.show()



# we got  a cat