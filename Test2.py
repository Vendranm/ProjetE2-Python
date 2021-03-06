#Code rédigé par Maxime Vendrand Maillet 
#Copyrigt Sur l'utilisation du code 

from PIL import Image
import PIL
import numpy as np
from resizeimage import resizeimage    
import math
import os
import shutil
from FctCarre import *

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
                ic = i.convert("RGB")
                #print(i.mode)
                pixi = ic.load()
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
def ouvImage():
    for dossier, sous_dossiers, fichiers in os.walk('images/faces94'):
        #print("dossier",dossier)
        #print("sdossier",sous_dossiers)
        #print(fichiers)  
        for fichier in fichiers:
            shutil.copy(dossier+"/"+fichier, 'images/DataBase')

def imMoy():
    Taille =[30,40]
    tabimS = []
    for dossier, sous_dossier, fichiers in os.walk('images/DataBaseTest'):
        for files in fichiers:
            if files.endswith('.jpg'):
                im = Image.open(os.path.join(dossier,files))
                #imR = resizeimage.resize_contain(im,Taille)
                imR = im.resize(Taille, PIL.Image.ANTIALIAS)
                imC = imR.convert("L")       
                imS = sobel(imC)
                tabimS.append(imS)
    imMoy = average_images(tabimS)
    imMoy.save('imMoy.jpg')
    imMoy.show()

#Taille=[32,64]
#im1 = Image.open('images/im1.jpeg')
#im1C = im1.convert("RGB")
#im1R = resizeimage.resize_contain(im1C,Taille)
#im1S = sobel(im1R)
#im2 = Image.open('images/im2.jpg')
#im2C = im2.convert("RGB")
#im2R = resizeimage.resize_contain(im2C,Taille)
#im2S = sobel(im2R)
#im3 = Image.open('images/im3.jpeg')
#im3C = im3.convert("RGB")
#im3R = resizeimage.resize_contain(im3C,Taille)
#im3S = sobel(im3R)
#im4 = Image.open('images/im4.jpeg')
#im4C = im4.convert("RGB")
#im4R = resizeimage.resize_contain(im4C,Taille)
#im4S = sobel(im4R)
#im5 = Image.open('images/im5.jpg')
#im5C = im5.convert("RGB")
#im5R = resizeimage.resize_contain(im5C,Taille)
#im5S = sobel(im5R)
#im6 = Image.open('images/im6.jpg')
#im6C = im6.convert("RGB")
#im6R = resizeimage.resize_contain(im6C,Taille)
#im6S = sobel(im6R)
#tabimR  =[im1R,im2R,im3R,im4R,im5R,im6R]
#tabimS = [im1S,im2S,im3S,im4S,im5S,im6S]
#imMoy = average_images(tabimS)

def difference(im1,im2, dx, dy):
    compris = False
    pix1 = im1.load()
    pix2 = im2.load()
    s = 0
    #print(im1.mode, im2.mode)
    for x in range(im1.size[0]):
        for y in range(im1.size[1]):
            l = pix1[x,y][0]
            L = pix2[x+dx,y+dy]
            s+= (abs(l-L))**2
    return s    

def comparaison(im, marge):
    imMoy = Image.open('images/imMoy.jpg')
    #imMoy.show()
    #im.show()
    pix=imMoy.load()
    pixTest = im.load()
    L = im.size[0]
    lmoy = imMoy.size[1]
    H = im.size[1]
    hmoy = imMoy.size[1]
    visage = False
    results = []
    for x in range(0,L - lmoy):
        #print(x,"/",L - lmoy)
        for y in range(0,H - hmoy):
            s = difference(imMoy,im,x,y)
            if s < marge*1.3:
                print("visage : ",x,y,s)
                results.append((x,y))
                if s < marge :
                    marge = s
                visage = True
    return marge,results
#comparaison(Image.open('images/imTest.JPG'))
#ouvImage()
#imMoy()
imMoy = Image.open("images/imMoy.jpg")
#im = Image.open("test.jpg")
im = Image.open("test.jpg")
imC2 = im.convert("L")
if(imC2.size[0]>700 or imC2.size[1]>700):
    imR1 = imC2.resize((int(imC2.size[0]/3),int(imC2.size[1]/3)), Image.ANTIALIAS)
else: 
    imR1 = imC2
#print("x : ", imR.size[0], "y :", imR.size[1])
xmoy = imMoy.size[0]
ymoy = imMoy.size[1]
marge = 20000000

#imR = imC2
imR = imR1
fact = 1.1
resize = 1
total_results = []
while(imR.size[0]>xmoy and imR.size[1]>ymoy): 
    print("RESIZE", resize)
    imS2 = sobel(imR)
    marge,results = comparaison(imS2, marge)
    total_results.append((resize, results))
    resize*=fact
    imR = imR1.resize((int(imR1.size[0]/resize),int(imR1.size[1]/resize)), Image.ANTIALIAS)

print(*total_results, sep="\n")
for z, l in total_results:
    for x,y in l:
        x2 = (x+xmoy)*z
        y2 = (y+ymoy)*z
        x*=z
        y*=z
        if(im.size[0]>700 or im.size[1]>700):
            x*=3
            y*=3
            x2*=3
            y2*=3
        afficher(im, x, x2, y, y2)
#for i in tabim:
    #i.show()    
    #print("Hauteur = ", i.size[0], "Largeur : ", i.size[1])
pass#pass sert juste a ce que ca compile    
