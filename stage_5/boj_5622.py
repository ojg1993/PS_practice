# 5622

dial = {2:'ABC', 3:'DEF', 4:'GHI', 5:'JKL',
        6:'MNO', 7:'PQRS', 8:'TUV', 9:'WXYZ'}

tot = 0

for i in input():
    for k, v in dial.items():
        if i in v:
            tot += k+1
print(tot)