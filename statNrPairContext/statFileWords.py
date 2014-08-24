# -*- coding: utf-8 -*-
import codecs

def statWord(inPutFileName, outPutFileName) :
    encoding = "utf-8-sig"
    f = codecs.open(inPutFileName, 'r',encoding)
    fo = codecs.open(outPutFileName,"w",encoding) 

    wordNumDic = {}

    for line in f :
        seq = line.split()
        for word in seq:
            if word not in wordNumDic.keys() :
                wordNumDic[word] = 0
            wordNumDic[word] += 1
                
    for word in wordNumDic.keys() :
        fo.write(word + ', ' + repr(wordNumDic[word]) +'\n')

    f.close()
    fo.close

if __name__ == '__main__':
    fileName = 'testfolder/test'
    statWord(fileName, fileName+'_stat.csv')
