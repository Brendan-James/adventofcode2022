monkeys = [[77, 69, 76, 77, 50, 58],[75, 70, 82, 83, 96, 64, 62],[53],[85, 64, 93, 64, 99],[61, 92, 71],[79, 73, 50, 90],[50, 89],[83, 56, 64, 58, 93, 91, 56, 65]]

counts = [0,0,0,0,0,0,0,0]

for rounds in range(10000):
    for i in range(8):
        for j,v in enumerate(monkeys[i]):
            monkeys[i][j] = v%(2*3*5*7*11*13*17*19)
    print(rounds)
    while len(monkeys[0])>0:
        counts[0]+=1
        monkeys[0][0] *= 11
        #monkeys[0][0] = monkeys[0][0]//3
        if monkeys[0][0]%5==0:
            monkeys[1].append(monkeys[0][0])
        else:
            monkeys[5].append(monkeys[0][0])
        monkeys[0].pop(0)
    while len(monkeys[1])>0:
        counts[1]+=1
        monkeys[1][0] += 8
        #monkeys[1][0] = monkeys[1][0]//3
        if monkeys[1][0]%17==0:
            monkeys[5].append(monkeys[1][0])
        else:
            monkeys[6].append(monkeys[1][0])
        monkeys[1].pop(0)
    while len(monkeys[2])>0:
        counts[2]+=1
        monkeys[2][0] *= 3
        #monkeys[2][0] = monkeys[2][0]//3
        if monkeys[2][0]%2==0:
            monkeys[0].append(monkeys[2][0])
        else:
            monkeys[7].append(monkeys[2][0])
        monkeys[2].pop(0)
    while len(monkeys[3])>0:
        counts[3]+=1
        monkeys[3][0] += 4
        #monkeys[3][0] = monkeys[3][0]//3
        if monkeys[3][0]%7==0:
            monkeys[7].append(monkeys[3][0])
        else:
            monkeys[2].append(monkeys[3][0])
        monkeys[3].pop(0)
    while len(monkeys[4])>0:
        counts[4]+=1
        monkeys[4][0] *= monkeys[4][0]
        #monkeys[4][0] = monkeys[4][0]//3
        if monkeys[4][0]%3==0:
            monkeys[2].append(monkeys[4][0])
        else:
            monkeys[3].append(monkeys[4][0])
        monkeys[4].pop(0)
    while len(monkeys[5])>0:
        counts[5]+=1
        monkeys[5][0] += 2
        #monkeys[5][0] = monkeys[5][0]//3
        if monkeys[5][0]%11==0:
            monkeys[4].append(monkeys[5][0])
        else:
            monkeys[6].append(monkeys[5][0])
        monkeys[5].pop(0)
    while len(monkeys[6])>0:
        counts[6]+=1
        monkeys[6][0] += 3
        #monkeys[6][0] = monkeys[6][0]//3
        if monkeys[6][0]%13==0:
            monkeys[4].append(monkeys[6][0])
        else:
            monkeys[3].append(monkeys[6][0])
        monkeys[6].pop(0)
    while len(monkeys[7])>0:
        counts[7]+=1
        monkeys[7][0] += 5
        #monkeys[7][0] = monkeys[7][0]//3
        if monkeys[7][0]%19==0:
            monkeys[1].append(monkeys[7][0])
        else:
            monkeys[0].append(monkeys[7][0])
        monkeys[7].pop(0)

print(counts)
counts.sort()
print(counts)
print(counts[-1]*counts[-2])
