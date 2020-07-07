from PIL import ImageTk
import PIL.Image
from tkinter import filedialog
from tkinter import *
import imageFilters as IF

#global variables
newIm = ""
originalWidth = 0
originalHeight = 0
mode = ""

def openFile():
    #Gets the user to select a file
    filename = filedialog.askopenfilename(title='Select a file', filetypes = (("jpeg files","*.jpg"),("png files","*.png")))
    #Displays the location of the file in the filename label
    fileLabel.config(text=filename)
    return filename

def openImg():
    global newIm, originalWidth, originalHeight, mode
    mode = "og"
    #Try and except blocks to handle "cancel"
    try:
        file = openFile() #gets the filename
        img = PIL.Image.open(file)
        newIm = img
        originalWidth = newIm.size[0]
        originalHeight = newIm.size[1]
        img = img.resize((300, 300), PIL.Image.ANTIALIAS) #Better quality and resizes the image
        img = ImageTk.PhotoImage(img)
        viewer.config(image = img) #Makes the viewer label show the image
        viewer.image = img
    except:
        print("File was not chosen.")

def grayFilter():
    global newIm, originalWidth, originalHeight, mode
    mode = "gray"
    ##imageName = "elton.jpg"
    filename = fileLabel.cget("text")
    im = IF.openImage(filename)
    pix = IF.openPix(im)
    newIm = IF.grayScale(im, pix) #Uses the grayScale 
    originalWidth = newIm.size[0]           #   function in imageFilters.py
    originalHeight = newIm.size[1] 
    newIm = newIm.resize((300, 300), PIL.Image.ANTIALIAS) #resize to fit viewer label
    img = ImageTk.PhotoImage(newIm)
    viewer.config(image = img) #Makes the viewer label show the image
    viewer.image = img

def sepiaFilter():
    global newIm, originalWidth, originalHeight, mode
    mode = "sepia"
    filename = fileLabel.cget("text")
    im = IF.openImage(filename)
    pix = IF.openPix(im)
    newIm = IF.sepia(im, pix) #Uses the sepia function
    originalWidth = newIm.size[0]       #   in imageFilters.py
    originalHeight = newIm.size[1] 
    newIm = newIm.resize((300, 300), PIL.Image.ANTIALIAS) #resize to fit viewer label
    img = ImageTk.PhotoImage(newIm)
    viewer.config(image = img) #Makes the viewer label show the image
    viewer.image = img

def revert():
    global newIm, originalWidth, originalHeight, mode
    mode = "og"
    filename = fileLabel.cget("text")
    newIm = PIL.Image.open(filename)
    originalWidth = newIm.size[0]
    originalHeight = newIm.size[1]
    newIm = newIm.resize((300, 300), PIL.Image.ANTIALIAS)
    img = ImageTk.PhotoImage(newIm)
    viewer.config(image = img)
    viewer.image = img


def save():
    global newIm, originalWidth, originalHeight, mode
    #Try and except blocks to handle "cancel"
    try:
        toSave = filedialog.asksaveasfile(mode='w',defaultextension='.jpg')
        newIm = newIm.resize((originalWidth, originalHeight), PIL.Image.ANTIALIAS)
    #These conditionals below increase quality of the image
    #It makes the images much sharper
    #I still need to add a fix to images that are Unaltered.
        if (mode=="og"):
            filename = fileLabel.cget("text")
            im = IF.openImage(filename)
            im.save(toSave)
        elif (mode=="sepia"):
            filename = fileLabel.cget("text")
            im = IF.openImage(filename)
            pix = IF.openPix(im)
            newIm = IF.sepia(im, pix)
            newIm.save(toSave)
        elif (mode=="gray"):
            filename = fileLabel.cget("text")
            im = IF.openImage(filename)
            pix = IF.openPix(im)
            newIm = IF.grayScale(im, pix)
            newIm.save(toSave)
    except:
        print("File was not saved.")
    


root = Tk()
root.title("Image Editor") #rename the GUI
root.geometry("900x700") #resize the GUI
root.resizable(width=False, height=False) #Make the GUI not resizeable

#The save button. Uses the save function.
save = Button(root, text='Save', width=10, command=save)
save.pack(side=TOP, anchor=NE, pady=(100, 0), padx=(0, 60))

#The grayscale button. Uses the grayFilter function.
gray = Button(root, text='Add grayscale filter', width=25, command=grayFilter) # gray button
gray.pack(side=LEFT, anchor=SE, pady=20, padx=(20, 0))

#The sepia button. Uses the sepiaFilter function.
sepia = Button(root, text='Add sepia filter', width=25, command=sepiaFilter) # sepia button
sepia.pack(side=RIGHT, anchor=SW, pady=20, padx=(0, 20))

#The revert button. Uses the revert function.
revert = Button(root, text='Revert', width=25, command=revert)
revert.pack(side = BOTTOM, pady=(0, 20))

#The choose an image button. Uses the openImg function.
pickImage = Button(root, text='Choose an image', width=25, command=openImg)
pickImage.pack(side = BOTTOM, pady=(20, 50))

#The filename label. Shows where the file is located.
fileLabel = Label(root, borderwidth = 3, relief="sunken", text="File name goes here")
fileLabel.pack(side = BOTTOM, pady=20)

#The viewer label. Displays the image.
viewer = Label(root, borderwidth = 3, relief="sunken", width=300, height=300)
viewer.pack(side = BOTTOM, pady=20)


root.mainloop()

