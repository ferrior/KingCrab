# -*- coding: utf-8 -*-
import codecs
encoding = "utf-8"
# read file and read each sentence
# save all the index of nr elements to a list
# retreve the contex of each nr index element according to the window size, ingore other nr element
# compose all the nr index pairs and same to another list
# go through the nr index pair list. merge the content of two nr element and compose a pair context
# if there are any two nr pairs' name are the same, merge the content of these two pair context.

def parseSentence(sentence) :
    id = ''
    wordList = []
    typeList = []
    seq = sentence.split()
    for word in seq:
        wseq = word.split('/')
        name = wseq[0].replace('[','').replace(']','')
        type = wseq[1]
        if word.find('1998') >= 0 and seq.index(word) == 0:
            id = name
        else :
            wordList.append(name)
            typeList.append(type)
    if id == '' :
        id = 'id'
    return id, wordList, typeList

    
def findNrs(wordList, typeList) :
    nrList = []
    nrIdxList = []
    for i in range(len(typeList)):
        type = typeList[i]
        if type == 'nr' and len(wordList[i]) > 1:
            nr = wordList[i]
            nrList.append(nr)
            nrIdxList.append(i)
    return nrList, nrIdxList


def composeNrPairs( nrlist ):
    nrpairlist = []
    for nr1 in nrlist :
        for nr2 in nrlist :
            if nr1 != nr2 and (nr2, nr1) not in nrpairlist:
                if nr1 < nr2 :
                    nrpairlist.append((nr1,nr2))
                else :
                    nrpairlist.append((nr2,nr1))
    return nrpairlist

def extraNrPairs(sentence) :
    id, words, types = parseSentence(sentence)
    nrList, nrIdxList = findNrs(words, types)
    nrPiarList = composeNrPairs(nrList)
    return nrPiarList

def extraNrPairIdx(sentence) :
    id, words, types = parseSentence(sentence)
    nrList, nrIdxList = findNrs(words, types)
    nrIdxPairList = composeNrPairs(nrIdxList)
    return nrIdxPairList
    
def findWordContext(sentence, wordIdx, window) : 
    context = []
    seq = sentence.split()
    wordSeq = seq[wordIdx].split('/')
    word = wordSeq[0]
    type = wordSeq[1]
    
    start = wordIdx - 1
    targetSize = window
    while targetSize > 0 and start > 0 :
        targetSeq = seq[start].split('/')
        targetWord = targetSeq[0]
        targetType = targetSeq[1]
        if targetType != type :
            context.append(targetWord)
            targetSize -= 1
        start -= 1
    
    start = wordIdx + 1
    targetSize = window
    end = len(seq)
    while targetSize > 0 and start < end :
        targetSeq = seq[start].split('/')
        targetWord = targetSeq[0]
        targetType = targetSeq[1]
        if targetType != type :
            context.append(targetWord)
            targetSize -= 1
        start += 1
    return context
    
def findWordContextIdx(typeList, wordIdx, window, ignorTypes) : 
    contextIdx = []
    currentIdx = wordIdx - 1
    targetSize = window
    while targetSize > 0 and currentIdx > 0 :
        targetType = typeList[currentIdx]
        if targetType not in  ignorTypes:
            contextIdx.append(currentIdx)
            targetSize -= 1
        currentIdx -= 1
    
    currentIdx = wordIdx + 1
    targetSize = window
    end = len(typeList)
    while targetSize > 0 and currentIdx < end :
        targetType = typeList[currentIdx]
        if targetType not in  ignorTypes:
            contextIdx.append(currentIdx)
            targetSize -= 1
        currentIdx += 1
    return contextIdx
    
def mergeList(list1, list2) :
    return list(set(list1 + list2))

def convertIdx2Word(idxList, wordList) :
    result = []
    for idx in idxList :
        result.append(wordList[idx])
    return result
    
def extraNrPairsContext(sentence) :
    nrPairContextMap = {}
    id, words, types = parseSentence(sentence)
    nrPairIdxList = []
    nrPairIdxList = extraNrPairIdx(sentence)
    window = 2
    ignoreTypes = ['nr', 'w', 'f', 'c', 'm', 'p']
    for (nrIdx1, nrIdx2) in nrPairIdxList :
        nrContextIdx1 = findWordContextIdx(types,nrIdx1, window, ignoreTypes)
        nrContextIdx2 = findWordContextIdx(types,nrIdx2, window, ignoreTypes)
        nrPair = (words[nrIdx1], words[nrIdx2])
        if nrPair[0] == nrPair[1] :
            continue
        
        if nrPair[0] > nrPair[1]  :
            nrPair = (nrPair[1] , nrPair[0])
        
        nrPairContextIdx = mergeList(nrContextIdx1, nrContextIdx2)
        if nrPair not in nrPairContextMap.keys():
            nrPairContextMap[nrPair] = []
        nrPairContextMap[nrPair].extend(convertIdx2Word(nrPairContextIdx, words))
    return nrPairContextMap

    
        
#####



outputFiles = {}  
sentence0 = ' 江/nr  泽民/nr  、/w  胡锦涛/nr 国家/n  江泽民/nr 主席/n 泽民/nr '
sentence1 = '19980127-09-001-031/m  [共青团/n  宜昌/ns  市委/n]nt  的/u  干部/n  职工/n  自发/d  为/p  王国栋/nr  捐款/v  ９７５/m  元/q  ，/w  [宜昌/ns  市委/n  机要局/n]nt  也/d  捐款/v  １０００/m  元/q  。/w  被/p  王国栋/nr  资助/v  过/u  的/u  张祖德/nr  、/w  杨朝明/nr  已/d  毕业/v  走/v  上/v  工作/vn  岗位/n  ，/w  他们/r  又/d  反过来/d  资助/v  王国栋/nr  。/w  '

f = [sentence0,sentence1]
f = codecs.open('../selecteddata/peopledaily/fileutf8.txt', 'r',encoding)
#f = codecs.open('test.txt', 'r',encoding)
for line in f :
    result = extraNrPairsContext(line)
    for nrPair in result :
        if nrPair not in outputFiles.keys():
            outputFiles[nrPair] = codecs.open(nrPair[0] + "_" + nrPair[1] ,"w",encoding)
        else:
            outputFiles[nrPair] = codecs.open(nrPair[0] + "_" + nrPair[1] ,"a",encoding)
        for word in result[nrPair] :
            (outputFiles[nrPair]).write(word + ' ')
        (outputFiles[nrPair]).write('\n')
        (outputFiles[nrPair]).close()
f.close()




'''
context = findWordContex(sentence, 5, 3)
print(context)

id, words, types = parseSentence(sentence)
print(id)
print(words)
print(types)

nrList, nrIdxList = findNrs(words, types)
print(nrList)
print(nrIdxList)
nrIdxPairList = composeNrPairs(nrIdxList)
print(nrIdxPairList)
'''
'''
nrlist = findNrs(sentence)
print(nrlist)
nridlist = findNrIdx(sentence)
print(nridlist)
list = composeNrPairs(nrlist)
for nrpair in list :
    print(nrpair)
list = composeNrPairs(nridlist)
for nrpair in list :
    print(nrpair)
'''