import os
import statFileWords

inputFolder = 'testfolder'
inputFolder = '../extraNrPairContext/nrpaircontext'
outputFolder = inputFolder + '_result'
if os.path.exists(outputFolder) :
    os.remove(outputFolder) 
os.mkdir(outputFolder)    
files = os.listdir(inputFolder)
for fileName in files :
    inputFile = os.path.join(inputFolder,fileName)
    outputFile = os.path.join(outputFolder,fileName+'_stat.csv')
    statFileWords.statWord(inputFile, outputFile)
