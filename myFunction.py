import cv2 as cv

# fungsi yang digunakan
def imgDiff(f0, f1, f2) :
    diff1 = cv.absdiff(f1, f0)
    diff2 = cv.absdiff(f2, f1)
    gs1 = imgGrayscaling(diff1)
    gs2 = imgGrayscaling(diff2)
    _, otsu1 = cv.threshold(gs1, 50, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    __, otsu2 = cv.threshold(gs2, 50, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    return cv.bitwise_and(diff1, diff2)

def imgSub(f1, f0) :
    return cv.absdiff(f1, f0)

def imgGrayscaling(f) :
    return cv.cvtColor(f, cv.COLOR_RGB2GRAY)

def adaptiveThreshold(f) :
    return cv.adaptiveThreshold(f, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 115, 1)

def otsuThresholding(f):
    return cv.threshold(f, 50, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

def showVideo(name, source) :
    cv.namedWindow(name, cv.WINDOW_NORMAL)
    cv.resizeWindow(name, 600, 400)
    return cv.imshow(name, source)
