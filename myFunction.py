import cv2 as cv

# fungsi yang digunakan
def imgDiff(f0, f1, f2) :
    diff1 = cv.absdiff(f1, f0)
    diff2 = cv.absdiff(f2, f1)
    gs1 = imgGrayscaling(diff1)
    gs2 = imgGrayscaling(diff2)
    _,bin1 = binaryThresholding(gs1)
    __,bin2 = binaryThresholding(gs2)
    return cv.bitwise_and(bin1, bin2)

def imgSub(f1, f0) :
    return cv.absdiff(f1, f0)

def imgGrayscaling(f) :
    return cv.cvtColor(f, cv.COLOR_RGB2GRAY)

def adaptiveThresholding(f) :
    return cv.adaptiveThreshold(f, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 115, 1)

def otsuThresholding(f):
    return cv.threshold(f, 50, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

def binaryThresholding(f) :
    return cv.threshold(f, 50, 255, cv.THRESH_BINARY)

def showVideo(name, source) :
    cv.namedWindow(name, cv.WINDOW_NORMAL)
    cv.resizeWindow(name, 300, 200)
    cv.imshow(name, source)
