import cv2 as cv
import numpy as np

# fungsi yang digunakan
def imgDiff(f0, f1, f2) :
    diff1 = cv.absdiff(f2, f1)
    diff2 = cv.absdiff(f1, f2)
    return cv.bitwise_and(diff1, diff2)

def imgSub(f1, f0) :
    return cv.absdiff(f1, f0)

def imgGrayscaling(f) :
    return cv.cvtColor(f, cv.COLOR_RGB2GRAY)

def adaptiveThreshold(f) :
    return cv.adaptiveThreshold(f, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 115, 1)

def showVideo(name, source) :
    cv.namedWindow(name, cv.WINDOW_NORMAL)
    cv.resizeWindow(name, 600, 400)
    return cv.imshow(name, source)

#inisiasi kamera
cam = cv.VideoCapture(0)

# Bagian pendeklarasian tampilan window
#windowName = "Deteksi gerak"
#cv.namedWindow(windowName, cv.WINDOW_NORMAL)
#cv.resizeWindow(windowName, 600, 400)

#mainWindow = "Monitor"
#cv.namedWindow(mainWindow, cv.WINDOW_NORMAL)
#cv.resizeWindow(mainWindow, 600,400)


# Deklarasi pengambilan pertama frame f(i-5), f(i), dan f(i+5)
fMin5Input = imgGrayscaling(cam.read()[1])
fInput = imgGrayscaling(cam.read()[1])
fPlus5Input = imgGrayscaling(cam.read()[1])

# Penerapan adaptive threshold mean c
fMin5 = adaptiveThreshold(fMin5Input)
f = adaptiveThreshold(fInput)
fPlus5 = adaptiveThreshold(fPlus5Input)

# Deklarasi awal gambar referensi
imageRef = f    # jangan diubah
count = 0
while True :
    #display gambar
    #cv.imshow(windowName, imgDiff(fMin5, f, fPlus5))
    #cv.imshow(mainWindow, cam.read()[1])
    showVideo("Binary image", imgDiff(fMin5, f, fPlus5))
    showVideo("Monitor", cam.read()[1])
    # pengambilan nilai matriks D(i-5) dan D(i+5) dengan fungsi imgDiff kemudian
    # penentuan objek bergerak
    movObject = imgDiff(fMin5, f, fPlus5)

    #penentuan background image
    bGround = imgSub(movObject, f)

    # generate Revised Background Image (RBI)
    RBI = cv.bitwise_or(imageRef, bGround)
    imageRef = RBI

    # pendeteksian objek bergerak
    mov = cv.absdiff(RBI, f)
    if mov.all() != f.all() :
        count += 1
        print("Warning, ", count)
    # swap frame
    fMin5 = f
    f = fPlus5


    fPlus5 = adaptiveThreshold(imgGrayscaling(cam.read()[1]))

    key = cv.waitKey(10)
    if key == 27 :
        cv.destroyAllWindows()
        break

print("Program Berhenti")
