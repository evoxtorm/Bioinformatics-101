


someString = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

aCount = 0
cCount = 0
gCount = 0
tCount = 0

for i in someString:
    if i == 'A':
        aCount += 1
    elif i == 'C':
        cCount += 1
    elif i == 'G':
        gCount += 1
    else:
        tCount += 1
print(aCount, cCount, gCount, tCount)
