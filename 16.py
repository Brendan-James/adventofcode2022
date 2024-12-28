import copy
from collections import OrderedDict
from itertools import chain, combinations, permutations

# oh boy day 16

predata = """my input""".split("\n")

data = {}
nonzeroes = {}

for i in predata:
    whole = []
    whole.append(i[6:8])
    whole.append(int(i[i.index("=")+1:i.index(";")]))
    if whole[-1] != 0:
        nonzeroes[whole[0]]=False
    splits = []
    while i[-1]!="v" and i[-1] != "e":
        splits.append(i[-2:])
        i=i[:-4]
    whole.append(splits)
    data[whole[0]] = whole[1:]

#print(data,nonzeroes)
positions = [[0,"AA",copy.deepcopy(nonzeroes)]]

for rounds in range(26):
    print(rounds)
    newpositions = []
    for i in positions:
        for j in i[2]:
            if i[2][j]:
                i[0]+=data[j][0]
        if i[1] in nonzeroes and not i[2][i[1]]:
            j = copy.deepcopy(i)
            j[2][i[1]] = True
            newpositions.append(j)
        for j in data[i[1]][1]:
            i[1] = j
            newpositions.append(copy.deepcopy(i))
    bests = {}
    for i in newpositions:
        if str(i[1:]) not in bests:
            bests[str(i[1:])] = [i[0],i]
        elif i[0]>bests[str(i[1:])][0]:
            bests[str(i[1:])] = [i[0],i]
    positions = []
    for i in bests:
        positions.append(bests[i][1])

best = 0

for i in positions:
    if i[0]>best:
        best = i[0]
print(best)

# PART 2
total = sum([data[i][0] for i in nonzeroes])
twentysixer = 1567
# 1327

pathdata = {}
for i in nonzeroes:
    positions = ["AA"]
    steps = 0
    flag = True
    while flag:
        steps+=1
        newpositions = []
        for j in positions:
            for k in data[j][1]:
                if k == i:
                    flag = False
                    break
                newpositions.append(k)
            if not flag:
                break
        positions = newpositions
    pathdata["AA"+i]=steps

for i in nonzeroes:
    for j in nonzeroes:
        positions = [i]
        if i == j:
            continue
        steps = 0
        flag = True
        while flag:
            steps+=1
            newpositions = []
            for l in positions:
                for k in data[l][1]:
                    if k == j:
                        flag = False
                        break
                    newpositions.append(k)
                if not flag:
                    break
            positions = newpositions
        pathdata[i+j] = steps


def partition(L):
    n = len(L)//2 + 1
    xs = chain(*[combinations(L, i) for i in range(1, n)])
    pairs = reversed([(x, tuple(set(L) - set(x))) for x in xs])
    return OrderedDict.fromkeys(pairs).keys()

bestest = 0
lonk = len(partition(nonzeroes))
for x,sets in enumerate(partition(nonzeroes)):
    print(x,lonk)
    dank = 0
    for xfactor,subseti in enumerate(sets):
        bestA = 0
        subset = {}
        for i in subseti:
            subset[i] = False
        total = sum([data[i][0] for  i in subset])
        if total*24+dank<bestest*xfactor or dank+twentysixer<bestest*xfactor or total*24+twentysixer<bestest:
            print("skippy")
            break
        positions = [[0,"AA",copy.deepcopy(subset),0,0]]
        finishers = []
        for rounds in range(-1,26):
            newpositions = []
            for i in positions:
                county = 0
                for j in i[2]:
                    if not i[2][j]:
                        county+=1
                if county==0:
                    finishers.append(i[0])
                    continue
                i[4] = 0
                for j in i[2]:
                    if i[2][j]:
                        i[4]+=data[j][0]
                i[0]+=i[4]
                if i[3]==0:
                    if i[1]!="AA":
                        i[2][i[1]]=True
                    for n in i[2]:
                        if i[2][n]:
                            continue
                        newf = copy.deepcopy(i)
                        newf[1] = n
                        newf[3] = pathdata[i[1]+n]
                        newpositions.append(newf)
                else:
                    i[3]-=1
                    newpositions.append(i)
                if county==1:
                    newpositions.append(i)
            best = -999999999999
            for i in finishers:
                if i>best:
                    best = i
            if len(finishers) > 0:
                finishers = [best+total]
            bests = {}
            for i in newpositions:
                if i[0]<best:
                    continue
                if str(i[1:]) not in bests:
                    bests[str(i[1:])] = [i[0],i]
                elif i[0]>bests[str(i[1:])][0]:
                    bests[str(i[1:])] = [i[0],i]
            pools = {}
            positions = []
            for i in bests:
                positions.append(bests[i][1])
            maxi = 0
            for i in positions:
                if i[4]*(26-rounds) + i[0]>maxi:
                    maxi = i[4]*(26-rounds) + i[0]>maxi
            newpositions = []
            for i in positions:
                if i[0]+total*(26-rounds)>maxi:
                    newpositions.append(i)
            positions = newpositions
        for i in finishers:
            if i>bestA:
                bestA = i
        for i in positions:
            if i[0]>bestA:
                bestA = i[0]
        dank+=bestA
    if dank>bestest:
        bestest = dank
print(bestest)
