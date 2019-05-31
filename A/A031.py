# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！


def cal(x,y,z):
    return 1*x*y*z

x,y,z,k = input().split(" ")

numList = []

for i in range (100):
    for j in range (100):
        for h in range (100):
            numList.append(cal(int(x)**i, int(y)**j, int(z)**h))

numList.sort()
print(str(numList[int(k)-1]))
