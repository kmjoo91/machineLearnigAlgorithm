from numpy import *
from os import listdir

import bookkNNAlgorithm

def img2vector(filename):
    returnVector = zeros((1, 32*32))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVector[0, 32*i+j] = int(lineStr[j])
    return returnVector

def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('digits/trainingDigits')
    m = len(trainingFileList)
    trainngMat = zeros((m, 1024))
    for i in range(m):
        fileName = trainingFileList[i]
        classNum = int(fileName.split('_')[0])
        hwLabels.append(classNum)
        trainngMat[i, :] = img2vector('digits/trainingDigits/%s' % fileName)
    testFileList = listdir('digits/testDigits')
    errorCount = 0
    mTest = len(testFileList)
    for i in range(mTest):
        fileName = testFileList[i]
        classNum = int(fileName.split('_')[0])
        testVector = img2vector('digits/testDigits/%s' % fileName)
        result = bookkNNAlgorithm.kNNAlgorithm(testVector, trainngMat, hwLabels, 3)
        print("the classifier came back with : %d, the real answer is : %d" % (result, classNum))
        if result != classNum:
            errorCount += 1
    print("\nthe total number of error is : %d" % (errorCount))
    print("\nthe total error rate is : %f" % ((errorCount/float(mTest))))
'''
handwritingClassTest()
'''
def TwoPrint(x,y,n):
    return round( (n-1) / (1/(x*1.0) + 1/(y*1.0)) + min(x,y))


print (TwoPrint(1,1,5))
print (TwoPrint(3,5,5))