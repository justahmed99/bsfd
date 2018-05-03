import cv2 as cv
import myFunction as mF

#inisiasi kamera
cam = cv.VideoCapture(0)

# Deklarasi pengambilan pertama frame f(i-5), f(i), dan f(i+5)
fMin5Input = mF.imgGrayscaling(cam.read()[1])
fInput = mF.imgGrayscaling(cam.read()[1])
fPlus5Input = mF.imgGrayscaling(cam.read()[1])

# Penerapan adaptive threshold mean c
fMin5 = mF.adaptiveThreshold(fMin5Input)
f = mF.adaptiveThreshold(fInput)
fPlus5 = mF.adaptiveThreshold(fPlus5Input)

# Deklarasi awal gambar referensi
imageRef = f    # jangan diubah
count = 0
while True :
    #display gambar
    mF.showVideo("Binary image", mF.imgDiff(fMin5, f, fPlus5))
    #showVideo("Monitor", cam.read()[1])

    # pengambilan nilai matriks D(i-5) dan D(i+5) dengan fungsi imgDiff kemudian
    # penentuan objek bergerak
    movObject = mF.imgDiff(fMin5, f, fPlus5)

    #penentuan background image
    bGround = mF.imgSub(movObject, f)

    # generate Revised Background Image (RBI)
    RBI = cv.bitwise_or(imageRef, bGround)
    imageRef = RBI

    # pendeteksian objek bergerak
    mov = cv.absdiff(RBI, f)
    if mov.all() != RBI.all() :
        count += 1
        print("Warning, ", count)
    # swap frame
    fMin5 = f
    f = fPlus5


    fPlus5 = mF.adaptiveThreshold(mF.imgGrayscaling(cam.read()[1]))

    key = cv.waitKey(10)
    if key == 27 :
        cv.destroyAllWindows()
        break

print("Program Berhenti")
