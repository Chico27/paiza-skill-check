N = input()

listP = []

for i in range(int(N)):
    listP.append(input())

numMap = {T:int(B), B:int(T), L:int(R), R:int(L), U:int(D), D:int(U)}

rotateNum = 0
currentPlace = T

for j in range(len(listP)):
    if (listP[j] == currentPlace):
        continue
    if(int(listP[j]) == numMap[currentPlace]):
        rotateNum+=2
        currentPlace = listP[j]
        continue
    rotateNum+=1
    currentPlace = listP[j]

print(rotateNum)
