import random

randList = []

while len(randList) < 12:
    randList.append(random.randint(1,40))

def bubbleSort(seq):
    indexLen = len(seq) - 1
    sorted = False
    
    while sorted == False:
        sorted = True
        for i in range(0, indexLen):
            if seq[i] > seq[i+1]:
                sorted = False
                seq[i], seq[i+1] = seq[i+1], seq[i]
    return seq
    

print(randList)
print(bubbleSort(randList))