from PIL import Image, ImageDraw ,ImageColor
import json
tiles = ['rgb(0,150,0)','rgb(0,0,255)','rgb(255,0,0)','rgb(73,73,73)']
def GetWorld(filename:str):
	try:
		file = open(filename, 'r')
	except BaseException as err:
		print("[ERROR]: {}".format(err))
		input()
		
	try:
		array =  json.loads(file.read())["map"]
	except BaseException as err:
		print("[ERROR]: {}".format(err))
		return False
	return array
# bulding = ['rgb(0,255,0)','rgb(255,255,0)','rgb(80,80,80)','rgb(0,130,0)','rgb(255,150,0)','rgb(128,0,128)','rgb(100,50,0)','rgb(250,220,100)','rgb(0,0,0)','rgb(100,100,100)','rgb(200,200,200)','rgb(0,130,40)','rgb(0,130,60)','yellow','rgb(250,220,100)','rgb(0,0,0)','rgb(0,0,0)','rgb(250,250,100)','rgb(250,250,100)','rgb(250,250,100)']

def createPhoto(size, tiles , array):
	SEC_SIZE = size - 1
	image_size = len(array)
	img = Image.new('RGB',(image_size * size,image_size * size),'gray')
	draw = ImageDraw.Draw(img)
	for i in range(len(array)):
		for j in range(len(array)):
			draw.rectangle((size * i,size* j,(size* i) + SEC_SIZE,(size* j) + SEC_SIZE), fill = tiles[array[i][j]])
			print('[INFO] '+ size* i, tiles[array[i][j]])
	img.save("test.png")
	img.show()

if __name__ == '__main__':
	createPhoto(size=int(input("SIZE: ")),tiles= tiles, array = GetWorld(filename = str(input("file name: "))))

