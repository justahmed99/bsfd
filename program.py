import cv2 as cv
import myFunction as mF

#inisiasi kamera
cam = cv.VideoCapture(1)

# Deklarasi pengambilan pertama frame f(i-5), f(i), dan f(i+5)
fMin5Input = cv.blur(cam.read()[1], (5,5))
fInput = cv.blur(cam.read()[1], (5,5))
fPlus5Input = cv.blur(cam.read()[1], (5,5))

# Penerapan adaptive threshold mean c
#ret1, fMin5 = mF.otsuThresholding(fMin5Input)
#ret2, f = mF.otsuThresholding(fInput)
#ret3, fPlus5 = mF.otsuThresholding(fPlus5Input)

# Deklarasi awal gambar referensi
ret, imageRef = mF.otsuThresholding(mF.imgGrayscaling(fInput))    # jangan diubah
count = 0
while True :
    #display gambar
    #mF.showVideo("Binary image", mF.imgDiff(fMin5, f, fPlus5))
    #mF.showVideo('camera', cam.read()[1])
    if count == 100 :
        refBlur = cv.blur(cam.read()[1], (5,5))
        _, imageRef = mF.otsuThresholding(mF.imgGrayscaling(refBlur))
        print('reference image is captured.')
        count = 0
    mF.showVideo('referensi', imageRef)

    # pengambilan nilai matriks D(i-5) dan D(i+5) dengan fungsi imgDiff kemudian
    # penentuan objek bergerak
    movObject = mF.imgDiff(fMin5Input, fInput, fPlus5Input)
    mF.showVideo('movObject', movObject)
    #penentuan background image
    #bGround = mF.imgSub(movObject, imageRef)
    #mF.showVideo('bGround', bGround)

    # generate Revised Background Image (RBI)
    #RBI = cv.bitwise_and(imageRef, bGround)
    #imageRef = RBI
    #mF.showVideo('rbi', RBI)

    # pendeteksian objek bergerak
    #mov = cv.absdiff(RBI, f)
    #mF.showVideo('mov', mov)
    #mF.showVideo('f', imageRef)
    #if mov.all() != 0 :
    #    count += 1
    #    print("Warning, ", count)
    # swap frame
    fMin5Input = fInput
    fInput = fPlus5Input
    fPlus5 = cv.blur(cam.read()[1], (5,5))
    #ret4, fPlus5 = mF.otsuThresholding(mF.imgGrayscaling(fPlusBlur))
    count = count + 1
    #print(count)
    key = cv.waitKey(10)
    if key == 27 or key == ord('q'):
        cv.destroyAllWindows()
        break

print("Program Berhenti")
