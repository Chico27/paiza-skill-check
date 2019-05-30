# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

def change(recieve):
    if("A" == recieve):
        return 4
    elif("E" == recieve):
        return 3
    elif("G" == recieve):
        return 6
    elif("I" == recieve):
        return 1
    elif("O" == recieve):
        return 0
    elif("S" == recieve):
        return 5
    elif("Z" == recieve):
        return 2
    else:
        return recieve

input_line = input()
output_line = ""

for char in input_line:
    output_line+=str(change(char))

print(output_line)
