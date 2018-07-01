import cv2 as cv
import time

# fungsi yang digunakan

def userControl() :
    while True :
        print('Pilih jenis threshold :')
        print('1. Binary Threshold')
        print('2. Otsu Threshold')
        print('3. Adaptive Threshold')
        tVal = int(raw_input('Pilih jenis threshold : '))
        if tVal == 1 :
            print('Threshold yang dipilih adalah Binary Threshold')
            inputVal = int(raw_input('Masukkan nilai threshold : '))
            if inputVal >= 0 and inputVal <= 255 :
                return tVal, inputVal
                break
            else :
                print('Masukkan nilai antara 0 dan 255!')
                inputVal = int(raw_input('Masukkan nilai threshold : '))
        elif tVal == 2 :
            print('Threshold yang dipilih adalah Otsu Threshold')
            inputVal = int(raw_input('Masukkan nilai threshold : '))
            if inputVal >= 0 and inputVal <= 255 :
                return tVal, inputVal
                break
            else :
                print('Masukkan nilai antara 0 dan 255!')
                inputVal = int(raw_input('Masukkan nilai threshold : '))
        elif tVal == 3 :
            print('Threshold yang dipilih adalah Adaptive Threshold')
            inputVal = int(raw_input('Masukkan nilai block-size : '))
            if inputVal % 2 == 0 :
                print('Masukkan nilai ganjil!')
                inputVal = int(raw_input('Masukkan nilai threshold : '))
            else :
                return tVal, inputVal
                break
        else :
            print('Pilih jenis threshold :')
            print('1. Binary Threshold')
            print('2. Otsu Threshold')
            print('3. Adaptive Threshold')
            input = int(raw_input('Pilih jenis threshold : '))

def imgDiff(f0, f1, f2, th, val) :
    diff1 = cv.absdiff(f1, f0)
    diff2 = cv.absdiff(f2, f1)
    gs1 = imgGrayscaling(diff1)
    gs2 = imgGrayscaling(diff2)
    if th == 1 :
        _,bin1 = binaryThresholding(gs1, val)
        __,bin2 = binaryThresholding(gs2, val)
        return cv.bitwise_and(bin1, bin2)
    elif th == 2 :
        _,otsu1 = otsuThresholding(gs1, val)
        __,otsu2 = otsuThresholding(gs2, val)
        return cv.bitwise_and(otsu1, otsu2)
    elif th == 3 :
        adap1 = adaptiveThresholding(gs1, val)
        adap2 = adaptiveThresholding(gs2, val)
        return cv.bitwise_and(adap1, adap2)
def imgSub(f1, f0) :
    return cv.absdiff(f1, f0)

def imgGrayscaling(f) :
    return cv.cvtColor(f, cv.COLOR_RGB2GRAY)

def adaptiveThresholding(f, bSize) :
    return cv.adaptiveThreshold(f, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, bSize, 1)

def otsuThresholding(f, th):
    return cv.threshold(f, th, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

def binaryThresholding(f, th) :
    return cv.threshold(f, th, 255, cv.THRESH_BINARY)

def showVideo(name, source) :
    cv.namedWindow(name, cv.WINDOW_NORMAL)
    cv.resizeWindow(name, 320, 240)
    cv.imshow(name, source)
