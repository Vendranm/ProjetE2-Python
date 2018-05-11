from PIL import Image


def draw_vline2(im, x1,x2,y, color):
    buffer = im.load()
    for x in range (min(x1,x2),max(x1,x2)):
        buffer[x,y]=color
    #mettre du code ici
    pass#pass sert juste a ce que ca compile


def draw_hline2(im, y2,y1,x, color):
    buffer=im.load()
    for y in range (min(y1,y2),max(y1,y2)):
        buffer [x,y]=color
    #mettre du code ici
    pass#pass sert juste a ce que ca compile

def afficher(): 
#	im = Image.new("RGB", (30,40))
	color=0,255,0
#	x1 = 5
#	y1 = 5
#	x2 = 25
#	y2= 35
	buffer=im.load()
	draw_vline2(im,x1,x2,y2,  color)
	draw_vline2(im, x1,x2,y1, color)
	draw_hline2(im, y1,y2,x1, color)
	draw_hline2(im, y1,y2,x2, color)
	buffer=im.load()
	im.save("image.jpg")
	pass

afficher()

