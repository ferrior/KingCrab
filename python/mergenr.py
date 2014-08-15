f = open('199801.txt', 'r')
fo = open('199801.merged.txt','w')

max = 100000000
for line in f:
    #fo.write(line)
    seq = line.split()
    nrcache = ''
    metnr = False
    for word in seq:
        wseq = word.split('/')
        str = wseq[0]
        type =  wseq[1]
        if type == 'nr':
            #print('handle nr:' , word)
            nrcache += str
            metnr = True
            #print(nrcache,':',type)
        else:
            #print('handle non-nr:', word , ' current nr is:',metnr)
            if metnr:
                #print('afaf')
                fo.write(nrcache+'/'+'nr  ')
                metnr = False
                nrcache = ''
            fo.write(word+'  ')
        #handle the case which nr at the last of the sentence
    if metnr:
        #print('finish the sentence')
        fo.write(nrcache+'/'+'nr ')
        metnr = False
        nrcache = ''
    #print('next line')
    fo.write('\n')
    max -= 1
    if max < 0:
        break

f.close()
fo.close()