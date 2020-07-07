from PIL import Image

def openImage(imageName):
    im = Image.open(imageName).convert('RGB') #opens the image
    return im

def openPix(im):
    pix = im.load() #Allocates storage for the image and loads it from the file
    return pix

def grayScale(im, pix):    
    done = False
    indexX = 0
    indexY = 0
    counter = 0
    while (done!=True):
        red = pix[indexX,indexY][0]
        green = pix[indexX,indexY][1]
        blue = pix[indexX,indexY][2]
        grayscale = red + green + blue
        grayscale = int(grayscale/3)
        pix[indexX,indexY] = (grayscale, grayscale, grayscale)
        indexY = indexY + 1
        if (indexY == im.size[1]):
            counter = counter + 1
            indexY = 0
            indexX = indexX + 1
        if (indexX == im.size[0]):
            done = True
    return im


def sepia(im, pix):
    done = False
    indexX = 0
    indexY = 0
    counter = 0
    while (done!=True):
        red = pix[indexX,indexY][0]
        green = pix[indexX,indexY][1]
        blue = pix[indexX,indexY][2]
        sepiaRed = 0.393 * red + 0.769 * green + 0.189 * blue
        sepiaGreen = 0.349 * red + 0.686 * green + 0.168 * blue
        sepiaBlue = 0.272 * red + 0.534 * green + 0.131 * blue
        if (sepiaRed > 255):
            sepiaRed = 255
        if (sepiaGreen > 255):
            sepiaGreen = 255
        if (sepiaBlue > 255):
            sepiaBlue = 255 
        pix[indexX,indexY] = (int(sepiaRed), int(sepiaGreen), int(sepiaBlue))
        indexY = indexY + 1
        if (indexY == im.size[1]):
            counter = counter + 1
            indexY = 0
            indexX = indexX + 1
        if (indexX == im.size[0]):
            done = True
    return im

    
