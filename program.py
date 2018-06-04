import cv2 as cv
import myFunction as mF

#inisiasi kamera
cam = cv.VideoCapture(1)

# Deklarasi pengambilan pertama frame f(i-5), f(i), dan f(i+5)
fMin5Input = cv.blur(cam.read()[1], (10,10))
fInput = cv.blur(cam.read()[1], (10,10))
fPlus5Input = cv.blur(cam.read()[1], (10,10))

# Deklarasi awal gambar referensi
ret, imageRef = mF.otsuThresholding(mF.imgGrayscaling(fInput)) # akan berubah sesuai dengan interval
count = 0
times = 0
cap = 0
i = 0
while True :
    #display gambar
    mF.showVideo('camera', cam.read()[1])
    if count == 100 :
        refBlur = cv.blur(cam.read()[1], (10,10))
        _, imageRef = mF.otsuThresholding(mF.imgGrayscaling(refBlur))
        times = times + 1
        print('Gambar referensi baru telah diambil. ke-'+str(times))
        count = 0
    mF.showVideo('referensi', imageRef)

    # pengambilan nilai matriks D(i-5) dan D(i+5) dengan fungsi imgDiff kemudian
    # penentuan objek bergerak
    movObject = mF.imgDiff(fMin5Input, fInput, fPlus5Input)
    mF.showVideo('movObject', movObject)

    #penentuan background image
    bGround = mF.imgSub(movObject, imageRef)
    mF.showVideo('bGround', bGround)

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

    fPlus5Input = cv.blur(cam.read()[1], (10,10))
    #ret4, fPlus5 = mF.otsuThresholding(mF.imgGrayscaling(fPlusBlur))
    count = count + 1
    #print(count)
    key = cv.waitKey(10)
    if key == 27 or key == ord('q') or key == ord('Q'):
        cv.destroyAllWindows()
        break
    elif key == ord('c') :
        cap = cap+1
        cv.imwrite('mov'+str(cap)+'.jpg', movObject)
        print('mengambil gambar mov'+str(cap)+'.jpg')

print("Program Berhenti")
