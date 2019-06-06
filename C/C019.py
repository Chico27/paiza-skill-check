# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


n = input()

for j in range(int(n)):
    aboutNumList = []
    numSum = 0
    inputnum = input()
    aboutNumList = make_divisors(int(inputnum))
    for k in range(len(aboutNumList)-1):
        numSum+=aboutNumList[k]
    if(int(inputnum) == numSum):
        print("perfect")
    elif(abs(int(inputnum)-numSum) <= 1):
        print("nearly")
    else:
        print("neither")
