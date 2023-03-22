
from PIL import ImageColor , Image
print(ImageColor.getcolor('whitesmoke','RGBA'))

catIm = Image.open('./images/zophie.png')
print(catIm)

catIm.save('zophie.jpg')

im = Image.new('RGBA', (100, 200), 'purple')
im.save('purpleImage.png')

croppedIM = catIm.crop((335, 345 ,565 ,560))
croppedIM.save('cropped.png')

width, height = catIm.size
quarterSizedIm= catIm.resize((int(width/2),int(height/2)))
quarterSizedIm.save('quarterSizedIM.png')

catIm.rotate(90, expand=True).save('rotate90.png')

im = Image.new('RGBA',(100,100))
im.getpixel((0,0))
for x in range(100):
    for y in range(50):
        im.putpixel((x,y),(210,210,210))
""" im.getpixel((0,0))
im.getpixel((0,50)) """

im.save('putpixel.png')
