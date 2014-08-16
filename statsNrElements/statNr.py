# -*- coding: utf-8 -*-
import codecs
import sys

encoding = "utf-8-sig"
f = codecs.open('../selecteddata/peopledaily/fileutf8.txt', 'r',encoding)
fo = codecs.open("resut.csv","w",encoding) 
nrDic = {}
nrNumDic = {}
total = 0

for line in f :
    seq = line.split()
    for word in seq:
        wseq = word.split('/')
        name = wseq[0]
        name = name.replace('[','')
        type =  wseq[1]
        if type == 'nr' and len(name) > 1:
            if name not in nrDic.keys():
                nrDic[name] = 0
            nrDic[name] += 1
            total += 1
            

print("total nr elements:",total)

total  = 0
for key in sorted(nrDic.keys()) :
        newline = key+' , '+ repr(nrDic[key])+'\n'
        fo.write(newline)
        if nrDic[key] not in nrNumDic.keys():
            nrNumDic[nrDic[key]] = 0
        nrNumDic[nrDic[key]] += 1
        
for key in sorted(nrNumDic.keys()) :
    print(key, ',' , nrNumDic[key])

f.close()
fo.close
