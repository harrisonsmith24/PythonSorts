import random

randList = []

while len(randList) < 12:
    randList.append(random.randint(1,40))

def InsertionSort(seq):
    indexLength = range(1, len(seq))
    for i in indexLength:
        sortValue = seq[i]

        while seq[i-1] > sortValue and i>0:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i=i-1
    return seq

print(randList)
print(InsertionSort(randList))