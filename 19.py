import copy

# not as bad as day 16

data = """Blueprint 01: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 14 clay. Each geode robot costs 2 ore and 16 obsidian.
Blueprint 02: Each ore robot costs 2 ore. Each clay robot costs 2 ore. Each obsidian robot costs 2 ore and 15 clay. Each geode robot costs 2 ore and 07 obsidian.
Blueprint 03: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 14 clay. Each geode robot costs 2 ore and 07 obsidian.
Blueprint 04: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 17 clay. Each geode robot costs 3 ore and 16 obsidian.
Blueprint 05: Each ore robot costs 2 ore. Each clay robot costs 2 ore. Each obsidian robot costs 2 ore and 17 clay. Each geode robot costs 2 ore and 10 obsidian.
Blueprint 06: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 17 clay. Each geode robot costs 4 ore and 08 obsidian.
Blueprint 07: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 09 clay. Each geode robot costs 2 ore and 20 obsidian.
Blueprint 08: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 3 ore and 14 obsidian.
Blueprint 09: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 20 clay. Each geode robot costs 3 ore and 18 obsidian.
Blueprint 10: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 16 clay. Each geode robot costs 4 ore and 16 obsidian.
Blueprint 11: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 05 clay. Each geode robot costs 3 ore and 15 obsidian.
Blueprint 12: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 14 clay. Each geode robot costs 3 ore and 08 obsidian.
Blueprint 13: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 20 clay. Each geode robot costs 2 ore and 17 obsidian.
Blueprint 14: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 19 clay. Each geode robot costs 3 ore and 10 obsidian.
Blueprint 15: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 17 clay. Each geode robot costs 4 ore and 20 obsidian.
Blueprint 16: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 14 clay. Each geode robot costs 3 ore and 20 obsidian.
Blueprint 17: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 12 clay. Each geode robot costs 3 ore and 15 obsidian.
Blueprint 18: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 19 clay. Each geode robot costs 3 ore and 13 obsidian.
Blueprint 19: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 18 clay. Each geode robot costs 2 ore and 19 obsidian.
Blueprint 20: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 16 clay. Each geode robot costs 2 ore and 09 obsidian.
Blueprint 21: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 20 clay. Each geode robot costs 2 ore and 20 obsidian.
Blueprint 22: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 06 clay. Each geode robot costs 2 ore and 16 obsidian.
Blueprint 23: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 06 clay. Each geode robot costs 4 ore and 11 obsidian.
Blueprint 24: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 05 clay. Each geode robot costs 2 ore and 10 obsidian.
Blueprint 25: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 14 clay. Each geode robot costs 3 ore and 14 obsidian.
Blueprint 26: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 15 clay. Each geode robot costs 4 ore and 16 obsidian.
Blueprint 27: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 18 clay. Each geode robot costs 4 ore and 11 obsidian.
Blueprint 28: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 4 ore and 17 obsidian.
Blueprint 29: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 11 clay. Each geode robot costs 3 ore and 14 obsidian.
Blueprint 30: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 08 clay. Each geode robot costs 4 ore and 14 obsidian.""".split("\n")

data2 = """Blueprint 01: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 07 obsidian.
Blueprint 02: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 08 clay. Each geode robot costs 3 ore and 12 obsidian.""".split("\n")

data = [[int(i[35]),int(i[64]),int(i[97]),int(i[107:109]),int(i[139]),int(i[149:151])] for i in data]



total = 0
for n,blue in enumerate(data):
    print(n)
    orecost, claycost, obscostO, obscostC, geocostOr, geocostOb = blue
    maxor = max(orecost,claycost,obscostO,geocostOr)
    posibilities = [[0,[1,0,0,0],[0,0,0,0],[]],[1,[1,0,0,0],[0,0,0,0],[]]]
    for rounds in range(24):
        print(rounds,len(posibilities))
        newposibilities = []
        for i in posibilities:
            target, bots, resources, trace = i
            if rounds == 23:
                for j in range(4):
                    resources[j]+=bots[j]
                newposibilities.append([target,bots,resources,trace])
                continue
            if target == 0:
                if resources[0]>=orecost:
                    trace.append(0)
                    for j in range(4):
                        resources[j]+=bots[j]
                    bots[0]+=1
                    resources[0]-=orecost
                    if bots[0]<maxor:
                        newposibilities.append(copy.deepcopy([0,bots,resources,trace]))
                    if bots[1]<obscostC:
                        newposibilities.append(copy.deepcopy([1,bots,resources,trace]))
                    if bots[1]>0:
                        if bots[2]<geocostOb:
                            newposibilities.append(copy.deepcopy([2,bots,resources,trace]))
                        if bots[2]>0:
                            newposibilities.append(copy.deepcopy([3,bots,resources,trace]))
                else:
                    for j in range(4):
                        resources[j]+=bots[j]
                    newposibilities.append(copy.deepcopy([target,bots,resources,trace]))
            elif target == 1:
                if resources[0]>=claycost:
                    trace.append(1)
                    for j in range(4):
                        resources[j]+=bots[j]
                    bots[1]+=1
                    resources[0]-=claycost
                    if bots[0]<maxor:
                        newposibilities.append(copy.deepcopy([0,bots,resources,trace]))
                    if bots[1]<obscostC:
                        newposibilities.append(copy.deepcopy([1,bots,resources,trace]))
                    if bots[2]<geocostOb:
                        newposibilities.append(copy.deepcopy([2,bots,resources,trace]))
                    if bots[2]>0:
                        newposibilities.append(copy.deepcopy([3,bots,resources,trace]))
                else:
                    for j in range(4):
                        resources[j]+=bots[j]
                    newposibilities.append(copy.deepcopy([target,bots,resources,trace]))
            elif target == 2:
                if resources[0]>=obscostO and resources[1]>=obscostC:
                    trace.append(2)
                    for j in range(4):
                        resources[j]+=bots[j]
                    bots[2]+=1
                    resources[0]-=obscostO
                    resources[1]-=obscostC
                    if bots[0]<maxor:
                        newposibilities.append(copy.deepcopy([0,bots,resources,trace]))
                    if bots[1]<obscostC:
                        newposibilities.append(copy.deepcopy([1,bots,resources,trace]))
                    if bots[2]<geocostOb:
                        newposibilities.append(copy.deepcopy([2,bots,resources,trace]))
                    newposibilities.append(copy.deepcopy([3,bots,resources,trace]))
                else:
                    for j in range(4):
                        resources[j]+=bots[j]
                    newposibilities.append(copy.deepcopy([target,bots,resources,trace]))
            elif target == 3:
                if resources[0]>=geocostOr and resources[2]>=geocostOb:
                    trace.append(3)
                    for j in range(4):
                        resources[j]+=bots[j]
                    bots[3]+=1
                    resources[0]-=geocostOr
                    resources[2]-=geocostOb
                    if bots[0]<maxor:
                        newposibilities.append(copy.deepcopy([0,bots,resources,trace]))
                    if bots[1]<obscostC:
                        newposibilities.append(copy.deepcopy([1,bots,resources,trace]))
                    if bots[2]<geocostOb:
                        newposibilities.append(copy.deepcopy([2,bots,resources,trace]))
                    newposibilities.append(copy.deepcopy([3,bots,resources,trace]))
                else:
                    for j in range(4):
                        resources[j]+=bots[j]
                    newposibilities.append(copy.deepcopy([target,bots,resources,trace]))
        best = 0
        for i in newposibilities:
            if i[2][3]+i[1][3]*(23-rounds)>best:
                best = i[2][3]+i[1][3]*(23-rounds)
        posibilities = []
        for i in newposibilities:
            if i[2][3]+i[1][3]*(23-rounds)+max(((23-rounds)*(22-rounds))//2,0)>=best:
                posibilities.append(i)
    best = 0
    for i in posibilities:
        if i[2][3]>best:
            best = i[2][3]
    total+=(n+1)*best
    print("Result:",n,best)

print(total)

data = """Blueprint 01: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 14 clay. Each geode robot costs 2 ore and 16 obsidian.
Blueprint 02: Each ore robot costs 2 ore. Each clay robot costs 2 ore. Each obsidian robot costs 2 ore and 15 clay. Each geode robot costs 2 ore and 07 obsidian.
Blueprint 03: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 14 clay. Each geode robot costs 2 ore and 07 obsidian.""".split("\n")

data = [[int(i[35]),int(i[64]),int(i[97]),int(i[107:109]),int(i[139]),int(i[149:151])] for i in data]

total = 1
for n,blue in enumerate(data):
    print(n)
    orecost, claycost, obscostO, obscostC, geocostOr, geocostOb = blue
    maxor = max(orecost,claycost,obscostO,geocostOr)
    posibilities = [[0,[1,0,0,0],[0,0,0,0],[]],[1,[1,0,0,0],[0,0,0,0],[]]]
    for rounds in range(32):
        print(rounds,len(posibilities))
        newposibilities = []
        for i in posibilities:
            target, bots, resources, trace = i
            if rounds == 31:
                for j in range(4):
                    resources[j]+=bots[j]
                newposibilities.append([target,bots,resources,trace])
                continue
            if target == 0:
                if resources[0]>=orecost:
                    trace.append(0)
                    for j in range(4):
                        resources[j]+=bots[j]
                    bots[0]+=1
                    resources[0]-=orecost
                    if bots[0]<maxor:
                        newposibilities.append(copy.deepcopy([0,bots,resources,trace]))
                    if bots[1]<obscostC:
                        newposibilities.append(copy.deepcopy([1,bots,resources,trace]))
                    if bots[1]>0:
                        if bots[2]<geocostOb:
                            newposibilities.append(copy.deepcopy([2,bots,resources,trace]))
                        if bots[2]>0:
                            newposibilities.append(copy.deepcopy([3,bots,resources,trace]))
                else:
                    for j in range(4):
                        resources[j]+=bots[j]
                    newposibilities.append(copy.deepcopy([target,bots,resources,trace]))
            elif target == 1:
                if resources[0]>=claycost:
                    trace.append(1)
                    for j in range(4):
                        resources[j]+=bots[j]
                    bots[1]+=1
                    resources[0]-=claycost
                    if bots[0]<maxor:
                        newposibilities.append(copy.deepcopy([0,bots,resources,trace]))
                    if bots[1]<obscostC:
                        newposibilities.append(copy.deepcopy([1,bots,resources,trace]))
                    if bots[2]<geocostOb:
                        newposibilities.append(copy.deepcopy([2,bots,resources,trace]))
                    if bots[2]>0:
                        newposibilities.append(copy.deepcopy([3,bots,resources,trace]))
                else:
                    for j in range(4):
                        resources[j]+=bots[j]
                    newposibilities.append(copy.deepcopy([target,bots,resources,trace]))
            elif target == 2:
                if resources[0]>=obscostO and resources[1]>=obscostC:
                    trace.append(2)
                    for j in range(4):
                        resources[j]+=bots[j]
                    bots[2]+=1
                    resources[0]-=obscostO
                    resources[1]-=obscostC
                    if bots[0]<maxor:
                        newposibilities.append(copy.deepcopy([0,bots,resources,trace]))
                    if bots[1]<obscostC:
                        newposibilities.append(copy.deepcopy([1,bots,resources,trace]))
                    if bots[2]<geocostOb:
                        newposibilities.append(copy.deepcopy([2,bots,resources,trace]))
                    newposibilities.append(copy.deepcopy([3,bots,resources,trace]))
                else:
                    for j in range(4):
                        resources[j]+=bots[j]
                    newposibilities.append(copy.deepcopy([target,bots,resources,trace]))
            elif target == 3:
                if resources[0]>=geocostOr and resources[2]>=geocostOb:
                    trace.append(3)
                    for j in range(4):
                        resources[j]+=bots[j]
                    bots[3]+=1
                    resources[0]-=geocostOr
                    resources[2]-=geocostOb
                    if bots[0]<maxor:
                        newposibilities.append(copy.deepcopy([0,bots,resources,trace]))
                    if bots[1]<obscostC:
                        newposibilities.append(copy.deepcopy([1,bots,resources,trace]))
                    if bots[2]<geocostOb:
                        newposibilities.append(copy.deepcopy([2,bots,resources,trace]))
                    newposibilities.append(copy.deepcopy([3,bots,resources,trace]))
                else:
                    for j in range(4):
                        resources[j]+=bots[j]
                    newposibilities.append(copy.deepcopy([target,bots,resources,trace]))
        best = 0
        for i in newposibilities:
            if i[2][3]+i[1][3]*(31-rounds)>best:
                best = i[2][3]+i[1][3]*(31-rounds)
        posibilities = []
        for i in newposibilities:
            if i[2][3]+i[1][3]*(31-rounds)+max(((31-rounds)*(30-rounds))//2,0)>=best:
                posibilities.append(i)
    best = 0
    for i in posibilities:
        if i[2][3]>best:
            best = i[2][3]
    total*=best
    print("Result:",n,best)

print(total)
