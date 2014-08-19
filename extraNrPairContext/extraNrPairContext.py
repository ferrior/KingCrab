# -*- coding: utf-8 -*-
import codecs

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
    seq = sentence.split()
    for i in range(len(typeList)):
        type = typeList[i]
        if type == 'nr' :
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
    
def findWordContext(wordList, wordIdx, window) : 


#####
def findWordContex(sentence, wordIdx, window) : 
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
    

sentence = ' 江/nr  泽民/nr  、/w  胡锦涛/nr 国家/n  江泽民/nr 主席/n 泽民/nr '
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