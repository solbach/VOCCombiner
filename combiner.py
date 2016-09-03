import os
import sys
import glob
import random

######################
# Combines
#
# trainval.txt
# test.txt
# train.txt
# val.txt
#
# of all subfolders
######################

def init(inputParam):
    print "\n##############"
    print "Pascal VOC style DATA-SET COMBINER"
    print " by Markus Solbach "
    print "    solbach@cse.yorku.ca"
    print "##############\n"

    if len(inputParam) < 2:
        print "\nNot enough arguments (%i)" % len(inputParam)
        print "Usage: combiner.py <folder>"
        print "<folder> needs sub-subfolders: Annotations with .xml and JPEGImages .JPEG"
        print "exit"
        sys.exit()
    return

def readTxtFilesAndShuffle(pathTest):
    txtFilesTest = glob.glob(pathTest)
    testData = []
    for files in txtFilesTest:
        with open(files, 'r') as myfile:
            fileRead = myfile.read()
            testData = testData + fileRead.split("\n")
    random.shuffle(testData)
    return testData


def writeToTxt(filePath, data):
    fileTest = open(filePath, 'w+')
    count = 0
    for item in data:
        count = count + 1
        if count < len(data):
            fileTest.write("%s\n" % item)
        else:
            fileTest.write("%s" % item)

################## Main

init(sys.argv)
path = str(sys.argv[1])
outputDir = path + "ImageSets/"

if not os.path.exists(outputDir):
        os.makedirs(outputDir)

# Combine test.txt files
pathTest = path + "*/ImageSets/test.txt"
testData = readTxtFilesAndShuffle(pathTest)
writeToTxt(outputDir + "test.txt", testData)

# Combine train.txt files
pathTest = path + "*/ImageSets/train.txt"
testData = readTxtFilesAndShuffle(pathTest)
writeToTxt(outputDir + "train.txt", testData)

# Combine val.txt files
pathTest = path + "*/ImageSets/val.txt"
testData = readTxtFilesAndShuffle(pathTest)
writeToTxt(outputDir + "val.txt", testData)

# Combine trainval.txt files
pathTest = path + "*/ImageSets/trainval.txt"
testData = readTxtFilesAndShuffle(pathTest)
writeToTxt(outputDir + "trainval.txt", testData)
