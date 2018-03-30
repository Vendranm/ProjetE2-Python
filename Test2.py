from PIL import Image
import PIL
import numpy as np
from resizeimage import resizeimage    
import math
import os
import shutil

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
    marge =5
    compris = False
    pix1 = im1.load()
    imS2 = sobel(im2)
    imC2 = imS2.convert("L")
    pix2 = im2.load()
    #print(im1.mode, im2.mode)
    for x in range(im1.size[0]):
        for y in range(im1.size[1]):
            l = pix1[x,y]
            L = pix2[x+dx,y+dy]
    if abs(l-L)<=marge :
        compris =True
    if compris:
        print("Ceci est un visage") 
    return compris 

def comparaison(im):
    imMoy = Image.open('images/imMoy.jpg')
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
                    difference(imMoy,im,x,y)
                    
#comparaison(Image.open('images/imTest.JPG'))
#ouvImage()
#imMoy()
im = Image.open("images/PhotoIdTest1.jpeg")
comparaison(im)
#for i in tabim:
    #i.show()    
    #print("Hauteur = ", i.size[0], "Largeur : ", i.size[1])
pass#pass sert juste a ce que ca compile    
