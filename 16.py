import copy
from collections import OrderedDict
from itertools import chain, combinations, permutations

# oh boy day 16

predata = """Valve OK has flow rate=0; tunnels lead to valves RW, FX
Valve JY has flow rate=13; tunnel leads to valve TT
Valve FX has flow rate=16; tunnels lead to valves OK, LF, GO, IV
Valve TD has flow rate=0; tunnels lead to valves XZ, ED
Valve VF has flow rate=9; tunnels lead to valves DS, LU, TR, WO
Valve TT has flow rate=0; tunnels lead to valves XZ, JY
Valve KR has flow rate=8; tunnels lead to valves VL, CI, GO, JJ, TQ
Valve HN has flow rate=0; tunnels lead to valves YG, AA
Valve MC has flow rate=24; tunnels lead to valves MI, EE, TH, YG
Valve XM has flow rate=0; tunnels lead to valves AF, JL
Valve XE has flow rate=0; tunnels lead to valves XP, AF
Valve ZF has flow rate=0; tunnels lead to valves EM, EI
Valve DS has flow rate=0; tunnels lead to valves VF, LF
Valve AF has flow rate=7; tunnels lead to valves AW, XE, CI, BJ, XM
Valve NL has flow rate=0; tunnels lead to valves KF, EM
Valve LF has flow rate=0; tunnels lead to valves FX, DS
Valve XZ has flow rate=25; tunnels lead to valves TD, TT
Valve TQ has flow rate=0; tunnels lead to valves AA, KR
Valve WO has flow rate=0; tunnels lead to valves VF, NE
Valve TH has flow rate=0; tunnels lead to valves LU, MC
Valve AA has flow rate=0; tunnels lead to valves TQ, KF, HN, XP, TY
Valve KB has flow rate=0; tunnels lead to valves WP, XL
Valve IV has flow rate=0; tunnels lead to valves PK, FX
Valve MI has flow rate=0; tunnels lead to valves JF, MC
Valve EX has flow rate=22; tunnels lead to valves JL, ZZ, SL
Valve ZZ has flow rate=0; tunnels lead to valves EX, JS
Valve KF has flow rate=0; tunnels lead to valves NL, AA
Valve PK has flow rate=11; tunnels lead to valves IV, HP
Valve TR has flow rate=0; tunnels lead to valves DI, VF
Valve YG has flow rate=0; tunnels lead to valves HN, MC
Valve JL has flow rate=0; tunnels lead to valves EX, XM
Valve VL has flow rate=0; tunnels lead to valves JS, KR
Valve XP has flow rate=0; tunnels lead to valves AA, XE
Valve TY has flow rate=0; tunnels lead to valves JS, AA
Valve EM has flow rate=4; tunnels lead to valves JJ, NL, ZF, WP, AW
Valve BJ has flow rate=0; tunnels lead to valves WK, AF
Valve JJ has flow rate=0; tunnels lead to valves EM, KR
Valve RW has flow rate=14; tunnels lead to valves NE, OK
Valve EI has flow rate=0; tunnels lead to valves ZF, JS
Valve SL has flow rate=0; tunnels lead to valves HP, EX
Valve EE has flow rate=0; tunnels lead to valves MC, XL
Valve WK has flow rate=0; tunnels lead to valves BJ, JS
Valve AW has flow rate=0; tunnels lead to valves EM, AF
Valve XL has flow rate=21; tunnels lead to valves EE, KB
Valve JF has flow rate=0; tunnels lead to valves MI, ED
Valve LU has flow rate=0; tunnels lead to valves TH, VF
Valve CI has flow rate=0; tunnels lead to valves AF, KR
Valve ED has flow rate=23; tunnels lead to valves JF, TD
Valve JS has flow rate=3; tunnels lead to valves VL, ZZ, EI, TY, WK
Valve NE has flow rate=0; tunnels lead to valves RW, WO
Valve DI has flow rate=12; tunnel leads to valve TR
Valve WP has flow rate=0; tunnels lead to valves KB, EM
Valve GO has flow rate=0; tunnels lead to valves FX, KR
Valve HP has flow rate=0; tunnels lead to valves SL, PK""".split("\n")

predata2 = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".split("\n")

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
