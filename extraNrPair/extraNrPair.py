# -*- coding: utf-8 -*-
import codecs

# read file and read each sentence
# save all the nr elements to a list
# compose all the nr pairs and same to another list

def findSentenceId(sentence) :
    seq = sentence.split()
    id = seq[0]
    id = id.split('/')[0]
    return id
    
def findNrs(sentence) :
    nrlist = []
    seq = sentence.split()
    for word in seq:
        wseq = word.split('/')
        name = wseq[0]
        name = name.replace('[','')
        type = wseq[1]
        if type == 'nr' and len(name) > 1 and name not in nrlist:
            nrlist.append(name)
    return nrlist
 
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

'''
nrlist = ['jhon', 'jim', '刘翔', '王jhon']
list = composeNrPairs(nrlist)
print(list)
'''
'''
sentence = '江/nr  泽民/nr  、/w  胡锦涛/nr 国家/n  江泽民/nr 主席/n 泽民/nr '
nrlist = findNrs(sentence)
list = composeNrPairs(nrlist)
for nrpair in list :
    print(nrpair)
'''
encoding = "utf-8-sig"
f = codecs.open('../selecteddata/peopledaily/fileutf8.txt', 'r',encoding)
fo = codecs.open("nrpairlistbysentence.txt","w",encoding) 
fo1 =  codecs.open("nrpairlist.txt","w",encoding) 
#f = open('../selecteddata/peopledaily/file.txt', 'r')
#fo = open("nrpairlist.txt","w") 

totallist = []
for sentence in f :
    nrlist = findNrs(sentence)
    nrpiarlist = composeNrPairs(nrlist)
    fo.write(findSentenceId(sentence)+'\n')
    for nrpair in nrpiarlist :
        fo.write(repr(nrpair)+'\n')
        if nrpair not in totallist :
            totallist.append(nrpair)
    



for nrpair in totallist :
    fo1.write(repr(nrpair)+'\n')
print('total number of nr pairs is:', len(totallist))