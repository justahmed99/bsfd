import cv2 as cv
import numpy as nmp
import myFunction as mF
import time

#inisiasi kamera
cam = cv.VideoCapture(1)
cam.set(3, 640)
cam.set(4, 480)

# Deklarasi pengambilan pertama frame f(i-1), f(i), dan f(i+1)
fMin1Input = cv.blur(cam.read()[1], (10,10))
fInput = cv.blur(cam.read()[1], (10,10))
fPlus1Input = cv.blur(cam.read()[1], (10,10))

# Kontrol awal user
th, val = mF.userControl()

# Deklarasi awal gambar referensi
imageRef = mF.imgGrayscaling(fInput)
if th == 1 :
    _,imageRef = mF.binaryThresholding(imageRef, val)
elif th == 2 :
    _,imageRef = mF.otsuThresholding(imageRef, val)
elif th == 3 :
    imageRef = mF.adaptiveThresholding(imageRef, val)
print(th)
print(val)
# cap merupakan variabel yang digunakan untuk menjadi indikator
cap = 0

while True :
    #display gambar
    mF.showVideo('camera', cam.read()[1])
    mF.showVideo('referensi', imageRef)

    # pengambilan nilai matriks D(i-1) dan D(i+1) dengan fungsi imgDiff kemudian
    # penentuan objek bergerak
    movObject = mF.imgDiff(fMin1Input, fInput, fPlus1Input, th, val)
    mF.showVideo('movObject', movObject)

    # penentuan background image
    bGround = cv.absdiff(movObject, imageRef)
    mF.showVideo('bGround', bGround)

    # pendeteksian objek bergerak
    mov = cv.absdiff(bGround, imageRef)
    mF.showVideo('mov', mov)

    # pembaruan nilai imageRef
    if time.localtime()[5] == 30 or time.localtime()[5] == 0 :
        refBlur = cv.blur(cam.read()[1], (10,10))
        print('gambar referensi diperbaru')
        if th == 1 :
            __,imageRef = mF.binaryThresholding(mF.imgGrayscaling(refBlur), val)
        elif th == 2 :
            __,imageRef = mF.otsuThresholding(mF.imgGrayscaling(refBlur), val)
        elif th == 3 :
            imageRef = mF.adaptiveThresholding(mF.imgGrayscaling(refBlur), val)

    # swap frame
    fMin1Input = fInput
    fInput = fPlus1Input
    fPlus1Input = cv.blur(cam.read()[1], (10,10))

    # mekanisme keluar program
    key = cv.waitKey(10)
    if key == 27 or key == ord('q') or key == ord('Q'):
        cv.destroyAllWindows()
        break
    elif key == ord('c') :
        # mengambil gambar
        cap = cap+1
        cv.imwrite('mov'+str(cap)+'.jpg', mov)
        cv.imwrite('cap'+str(cap)+'.jpg', cam.read()[1])
        cv.imwrite('imageRef'+str(cap)+'.jpg', imageRef)
        cv.imwrite('movObject'+str(cap)+'.jpg', movObject)
        cv.imwrite('bGround'+str(cap)+'.jpg', bGround)
        print('mengambil gambar ke'+str(cap))

print("Program Berhenti")
