data = """my input pt 1""".split("\n")

route = "my input pt 2"

variable = []
for i in data:
    new = []
    for j in range(len(data[0])):
        try:
            new.append(i[j])
        except Exception as e:
            new.append(" ")
    variable.append(new)

data = variable

for i in range(len(data[0])):
    if data[0][i]!=" ":
        position = [0,i]
        break

direction = "R"
nombre = "0123456789"

while len(route) > 0:
    if len(route)>1 and route[0] in nombre and route[1] in nombre:
        current = int(route[:2])
        route = route[2:]

    else:
        if route[0] in nombre:
            current = int(route[0])
            route = route[1:]
        else:
            current = route[0]
            route = route[1:]
            if current == "R":
                if direction == "U":
                    direction = "R"
                elif direction == "R":
                    direction = "D"
                elif direction == "D":
                    direction = "L"
                elif direction == "L":
                    direction = "U"
            if current == "L":
                if direction == "U":
                    direction = "L"
                elif direction == "L":
                    direction = "D"
                elif direction == "D":
                    direction = "R"
                elif direction == "R":
                    direction = "U"
            continue
    for i in range(current):
        if direction == "U":
            target = [position[0]-1,position[1]]
        if direction == "R":
            target = [position[0],position[1]+1]
        if direction == "D":
            target = [position[0]+1,position[1]]
        if direction == "L":
            target = [position[0],position[1]-1]
        if target[0]>=len(data) or target[1]>=len(data[0]) or data[target[0]][target[1]] == " " or target[0]<0 or target[1]<0:
            if direction == "U":
                tarsquare = [target[0]+1,target[1]]
            if direction == "R":
                tarsquare = [target[0],target[1]-1]
            if direction == "D":
                tarsquare = [target[0]-1,target[1]]
            if direction == "L":
                tarsquare = [target[0],target[1]+1]
            while not (tarsquare[0]>=len(data) or tarsquare[1]>=len(data[0]) or data[tarsquare[0]][tarsquare[1]] == " " or tarsquare[0]<0 or tarsquare[1]<0):
                target = tarsquare
                if direction == "U":
                    tarsquare = [target[0]+1,target[1]]
                if direction == "R":
                    tarsquare = [target[0],target[1]-1]
                if direction == "D":
                    tarsquare = [target[0]-1,target[1]]
                if direction == "L":
                    tarsquare = [target[0],target[1]+1]
        if data[target[0]][target[1]] == "#":
            break
        if data[target[0]][target[1]] == ".":
            position = target
            continue

if direction == "R":
    facescore = 0
if direction == "D":
    facescore = 1
if direction == "L":
    facescore = 2
if direction == "U":
    facescore = 3
print((position[0]+1)*1000+(position[1]+1)*4+facescore)

"""
     AB
     C
    ED
    F
"""

A = """my input pt 1A""".split("\n")
B = """my input pt 1B""".split("\n")
C = """my input pt 1C""".split("\n")
D = """my input pt 1D""".split("\n")
E = """my input pt 1E""".split("\n")
F = """my input pt 1F""".split("\n")

route = "my input pt 2"

position = [0,0]

direction = "R"

data = A
tardata = A


while len(route) > 0:
    if len(route)>1 and route[0] in nombre and route[1] in nombre:
        current = int(route[:2])
        route = route[2:]

    else:
        if route[0] in nombre:
            current = int(route[0])
            route = route[1:]
        else:
            current = route[0]
            route = route[1:]
            if current == "R":
                if direction == "U":
                    direction = "R"
                elif direction == "R":
                    direction = "D"
                elif direction == "D":
                    direction = "L"
                elif direction == "L":
                    direction = "U"
            if current == "L":
                if direction == "U":
                    direction = "L"
                elif direction == "L":
                    direction = "D"
                elif direction == "D":
                    direction = "R"
                elif direction == "R":
                    direction = "U"
            continue
    for i in range(current):
        if direction == "U":
            target = [position[0]-1,position[1]]
        if direction == "R":
            target = [position[0],position[1]+1]
        if direction == "D":
            target = [position[0]+1,position[1]]
        if direction == "L":
            target = [position[0],position[1]-1]
        tardirection = direction
        tardata = data
        y,x = target
        if target[0]<0 or target[1]<0 or target[0]>=len(data) or target[1]>=len(data[0]):
            # AB
            # C
            #ED
            #F
            if direction == "L":
                if data == A:
                    tardata = E
                    target[0] = len(data)-target[0]-1
                    target[1] = 0
                    tardirection = "R"
                if data == B:
                    tardata = A
                    target[1] = len(data[0])-1
                if data == C:
                    tardata = E
                    target[1] = target[0]
                    target[0] = 0
                    tardirection = "D"
                if data == D:
                    tardata = E
                    target[1] = len(data[0])-1
                if data == E:
                    tardata = A
                    target[0] = len(data)-target[0]-1
                    target[1] = 0
                    tardirection = "R"
                if data == F:
                    tardata = A
                    target[1] = target[0]
                    target[0] = 0
                    tardirection = "D"
            if direction == "R":
                if data == A:
                    tardata = B
                    target[1] = 0
                if data == B:
                    tardata = D
                    target[0] = len(data)-target[0]-1
                    target[1] = len(data[0])-1
                    tardirection = "L"
                if data == C:
                    tardata = B
                    target[1] = target[0]
                    target[0] = len(data)-1
                    tardirection = "U"
                if data == D:
                    tardata = B
                    target[0] = len(data)-target[0]-1
                    target[1] = len(data[0])-1
                    tardirection = "L"
                if data == E:
                    tardata = D
                    target[1] = 0
                if data == F:
                    tardata = D
                    target[1] = target[0]
                    target[0] = len(data[0])-1
                    tardirection = "U"
            if direction == "U":
                if data == A:
                    tardata = F
                    target[0] = target[1]
                    target[1] = 0
                    tardirection = "R"
                if data == B:
                    tardata = F
                    target[0] = len(data)-1
                if data == C:
                    tardata = A
                    target[0] = len(data)-1
                if data == D:
                    tardata = C
                    target[0] = len(data)-1
                if data == E:
                    tardata = C
                    target[0] = target[1]
                    target[1] = 0
                    tardirection = "R"
                if data == F:
                    tardata = E
                    target[0] = len(data)-1
            if direction == "D":
                if data == A:
                    tardata = C
                    target[0] = 0
                if data == B:
                    tardata = C
                    target[0] = target[1]
                    target[1] = len(data[0])-1
                    tardirection = "L"
                if data == C:
                    tardata = D
                    target[0] = 0
                if data == D:
                    tardata = F
                    target[0] = target[1]
                    target[1] = len(data[0])-1
                    tardirection = "L"
                if data == E:
                    tardata = F
                    target[0] = 0
                if data == F:
                    tardata = B
                    target[0] = 0
        if tardata[target[0]][target[1]] == "#":
            break
        if tardata[target[0]][target[1]] == ".":
            position = target
            data = tardata
            direction = tardirection
            continue

temp = copy.deepcopy(data)
temp[position[0]] = temp[position[0]][:position[1]]+"*"+temp[position[0]][position[1]+1:]
print(temp)
if data == A:
    print("A")
if data == B:
    print("B")
if data == C:
    print("C")
if data == D:
    print("D")
if data == E:
    print("E")
if data == F:
    print("F")

if direction == "R":
    facescore = 0
if direction == "D":
    facescore = 1
if direction == "L":
    facescore = 2
if direction == "U":
    facescore = 3
if data == A:
    position[1]+=50
if data == B:
    position[1]+=100
if data == C:
    position[0]+=50
    position[1]+=50
if data == D:
    position[0]+=100
    position[1]+=50
if data == E:
    position[0]+=100
if data == F:
    position[0]+=150
print((position[0]+1)*1000+(position[1]+1)*4+facescore)
