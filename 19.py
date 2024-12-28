import copy

# not as bad as day 16

data = """my input""".split("\n")

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

data = """only the first 3 lines of my input""".split("\n")

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
