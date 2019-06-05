# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

input_line = input()
strikeCt = 0
ballCt = 0

for i in range(int(input_line)):
    inputBall = input()
    if("strike" == inputBall):
        if(strikeCt == 2):
            print("out!")
            break
        else:
            print("strike!")
        strikeCt+=1
    if("ball" == inputBall):
        if(ballCt == 3):
            print("fourball!")
            break
        else:
            print("ball!")
        ballCt+=1
