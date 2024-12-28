import copy
data = """my input""".split("\n")

blizzards = []
width = len(data[0])
height = len(data)
for x in range(1,width-1):
    for y in range(1,height-1):
        if data[y][x]!=".":
            blizzards.append([x,y,data[y][x]])

def step(blizzards,width,height):
    gizzards = copy.deepcopy(blizzards)
    for i in gizzards:
        if i[2]=="^":
            i[1]-=1
            if i[1]==0:
                i[1] = height-2
        if i[2]=="v":
            i[1]+=1
            if i[1]==height-1:
                i[1] = 1
        if i[2]=="<":
            i[0]-=1
            if i[0]==0:
                i[0] = width-2
        if i[2]==">":
            i[0]+=1
            if i[0]==width-1:
                i[0] = 1
    return gizzards

positions = [[1,0]]
steps = 0
project = 0
while True:
    #print(steps,len(positions))
    steps+=1
    blizzards = step(blizzards,width,height)
    newpositions = set()
    for i in positions:
        newpositions.add(str(i[0])+","+str(i[1]))
        newpositions.add(str(i[0]+1)+","+str(i[1]))
        newpositions.add(str(i[0]-1)+","+str(i[1]))
        newpositions.add(str(i[0])+","+str(i[1]+1))
        newpositions.add(str(i[0])+","+str(i[1]-1))
    spaces = set()
    for i in blizzards:
        spaces.add(str(i[0])+","+str(i[1]))
    positions = []
    for i in newpositions:
        if i not in spaces:
            temp = i.split(",")
            temp[0] = int(temp[0])
            temp[1] = int(temp[1])
            if 0<temp[0]<width-1 and 0<temp[1]<height-1:
                positions.append([temp[0],temp[1]])
                continue
            if temp[0]==1 and temp[1]==0:
                if project == 1:
                    print(steps)
                    positions = [[1,0]]
                    project = 2
                    break
                else:
                    positions.append([temp[0],temp[1]])
                continue
            if temp[0]==width-2 and temp[1]==height-1:
                if project == 0:
                    print("a:",steps)
                    positions = [[width-2,height-1]]
                    project = 1
                    break
                elif project == 2:
                    print("b:",steps)
                    assert False
                else:
                    positions.append([temp[0],temp[1]])
