from PIL import Image, ImageDraw ,ImageColor
import json
file = open(str(input("file name: ")), 'r')
array =  json.loads(file.read())
SIZE = int(input("SIZE: "))
image_size = len(array)
SEC_SIZE = SIZE - 1
img = Image.new('RGB',(image_size * SIZE,image_size * SIZE),'gray')
draw = ImageDraw.Draw(img)

bulding = ['rgb(0,255,0)','rgb(255,255,0)','rgb(80,80,80)','rgb(0,130,0)','rgb(255,150,0)','rgb(128,0,128)','rgb(100,50,0)','rgb(250,220,100)','rgb(0,0,0)','rgb(100,100,100)','rgb(200,200,200)','rgb(0,130,40)','rgb(0,130,60)','yellow','rgb(250,220,100)','rgb(0,0,0)','rgb(0,0,0)','rgb(250,250,100)','rgb(250,250,100)','rgb(250,250,100)']
colors = ['rgb(0,150,0)','rgb(0,0,255)','rgb(255,0,0)','rgb(73,73,73)']
for i in range(len(array)):
	for j in range(len(array)):
		draw.rectangle((SIZE * i,SIZE * j,(SIZE * i) + SEC_SIZE,(SIZE * j) + SEC_SIZE), fill = colors[array[i][j]])
		print(SIZE * i, colors[array[i][j]])

img.save("test.png")
img.show()