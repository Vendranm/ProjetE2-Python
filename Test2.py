from PIL import Image
import numpy as np
from resizeimage import resizeimage    
import math
def sobel(im):
    imConv = im.convert("L")
    buff =imConv.load()
    result = im.copy()
    rbuffer = result.load()
    Gx = [[-1,0,1],[-2,0,2],[-1,0,1]]
    Gy = [[-1,-2,-1],[0,0,0],[1,2,1]]
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            gx=0
            gy=0
            G=0
            for x2 in range(0,3):
                for y2 in range(0,3):
                    if x+x2-1>=0 and y+y2-1>=0 and x+x2-1<im.size[0] and y+y2-1 < im.size[1]:
                        gx += Gx[x2][y2]*buff[x+x2-1,y+y2-1]
                        gy += Gy[x2][y2]*buff[x+x2-1,y+y2-1]
            G = math.sqrt(gx**2+gy**2)
            rbuffer[x,y]=int(G)
    return result 
def average_images(images):
    #mettre du code ici
    result = Image.new('RGB', (images[0].size[0],images[0].size[1]))
    pixres = result.load()
    for x in range(images[0].size[0]):
        for y in range(images[0].size[1]): 
            mr,mg,mb=0,0,0
            for i in images:
                pixi = i.load()
                r,g,b = pixi[x,y]
                mr +=r
                mg +=g
                mb +=b
            R = mr//len(images)
            G = mg//len(images)
            B = mb//len(images)
            pixres[x,y]=R,G,B
    result.show()
    return result
Taille=[32,64]
im1 = Image.open('images/im1.jpeg')
im1R = resizeimage.resize_contain(im1,Taille)
im1S = sobel(im1R)
im2 = Image.open('images/im2.jpg')
im2R = resizeimage.resize_contain(im2,Taille)
im2S = sobel(im2R)
im3 = Image.open('images/im3.jpeg')
im3R = resizeimage.resize_contain(im3,Taille)
im3S = sobel(im3R)
im4 = Image.open('images/im4.jpeg')
im4R = resizeimage.resize_contain(im4,Taille)
im4S = sobel(im4R)
im5 = Image.open('images/im5.jpg')
im5R = resizeimage.resize_contain(im5,Taille)
im5S = sobel(im5R)
im6 = Image.open('images/im6.jpg')
im6R = resizeimage.resize_contain(im6,Taille)
im6S = sobel(im6R)
tabimR  =[im1R,im2R,im3R,im4R,im5R,im6R]
tabimS = [im1S,im2S,im3S,im4S,im5S,im6S]
imMoy = average_images(tabimS)

def difference(im1,im2):
    marge =20
    compris = false
    pix1 = im1.load()
    pix2 = im2.load()
    for x in range(im1.size[0]):
        for y in range(im.size[1]):
            r,g,b = pix1[x,y]
            R,G,B = pix2[x,y]
            if abs(r-R)<=marge and abs(b-B)<=marge and abs(g-G)<=marge:
                compris = true
    if visage:
        print("Ceci est un visage") 
    return compris 

def comparaison(im):
    pix=imMoy.load()
    pixTest = im.load()
    L = im.size[0]
    lmoy = imMoy.size[1]
    H = im.size[1]
    hmoy = imMoy.size[1]
    marge = 20
    for x in range(0,L - lmoy):
        for y in range(0,H - hmoy):
            for i in range(lmoy):
                for j in range(hmoy):
                    difference(im,imMoy)
                    x+=im
                    y+=j
#for i in tabim:
    #i.show()    
    #print("Hauteur = ", i.size[0], "Largeur : ", i.size[1])
pass#pass sert juste a ce que ca compile    