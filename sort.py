import random

randList = []

while len(randList) < 12:
    randList.append(random.randint(1,200))

def QuickSort(seq):
    if (len(seq) <= 1):
        return seq
    else:
       pivot = seq.pop()

    listHigh = []
    listLow = []

    for item in seq:
        if item > pivot:
            listHigh.append(item)
        else:
            listLow.append(item)
    
    return QuickSort(listLow) + [pivot] + QuickSort(listHigh)

print(randList)
print(QuickSort(randList))
