# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

def evenCal(inputNum):
    if(int(inputNum) * 2) < 10:
        return inputNum*2
    else:
        outChar = str(inputNum*2)
        return int(outChar[0]) + int(outChar[1])
    

def cal(inputNum):

    evenNum = 0
    oddNum = 0

    for j in range(len(inputNum)):
        num = inputNum[j]
        if("X" == num):
            break
        if(int(j) % 2 == 0) :
            evenNum+=int(evenCal(int(num)))
        else:
            oddNum+=int(num)

    outputNum = 10 - ((evenNum + oddNum) % 10)
    if(outputNum != 10):
        return outputNum
    else:
        return 0

input_line = input()

for i in range(int(input_line)):
    inputNum = input()
    print(cal(inputNum))
