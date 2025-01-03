import copy
data = """my input""".split("\n")

data = [[i for i in j] for j in data]

dirs = ["N","S","W","E"]


def embiggen(grid):
    x = len(grid[0])
    y = len(grid)
    expand = [False, False]
    for i in range(y):
        if grid[i][0] == "#":
            expand[0] = True
        if grid[i][x-1] == "#":
            expand[1] = True
        if expand[0] and expand[1]:
            break
    if expand[1]:
        x+=1
        for i in range(y):
            grid[i].append(".")
    if expand[0]:
        x+=1
        for i in range(y):
            grid[i].insert(0, ".")
    expand = [False, False]
    for i in range(x):
        if grid[0][i] == "#":
            expand[0] = True
        if grid[y-1][i] == "#":
            expand[1] = True
        if expand[0] and expand[1]:
            break
    if expand[1]:
        grid.append(["." for i in range(x)])
    if expand[0]:
        grid.insert(0,["." for i in range(x)])
    return grid

def ensmallen(grid):
    width = len(grid[0])
    height = len(grid)
    for i in range(width):
        if grid[0][i]=="#":
            break
    else:
        grid.pop(0)
        height-=1
    for i in range(width):
        if grid[height-1][i]=="#":
            break
    else:
        grid.pop()
        height-=1
    for i in range(height):
        if grid[i][0]=="#":
            break
    else:
        for i in range(height):
            grid[i].pop(0)
        width-=1
    for i in range(height):
        if grid[i][width-1]=="#":
            break
    else:
        for i in range(height):
            grid[i].pop()
        width-=1

    return grid

rounds = 0
Flag = True
while Flag:
    data = embiggen(data)
    Flag = False
    #print("\n".join(["".join(i) for i in data]))
    #print("\n")
    width = len(data[0])
    height = len(data)
    for x in range(width):
        for y in range(height):
            if data[y][x]=="#":
                if data[y-1][x-1]!="#" and data[y-1][x]!="#" and data[y-1][x+1]!="#" and data[y][x+1]!="#" and data[y+1][x+1]!="#" and data[y+1][x]!="#" and data[y+1][x-1]!="#" and data[y][x-1]!="#":
                    continue
                for direction in dirs:
                    if direction == "N":
                        if data[y-1][x-1] != "#" and data[y-1][x] != "#" and data[y-1][x+1] != "#":
                            if data[y-1][x] == "*" or data[y-1][x] == "X":
                                data[y-1][x] = "X"
                            else:
                                data[y-1][x] = "*"
                            break
                    if direction == "S":
                        if data[y+1][x-1] != "#" and data[y+1][x] != "#" and data[y+1][x+1] != "#":
                            if data[y+1][x] == "*" or data[y+1][x] == "X":
                                data[y+1][x] = "X"
                            else:
                                data[y+1][x] = "*"
                            break
                    if direction == "W":
                        if data[y-1][x-1] != "#" and data[y][x-1] != "#" and data[y+1][x-1] != "#":
                            if data[y][x-1] == "*" or data[y][x-1] == "X":
                                data[y][x-1] = "X"
                            else:
                                data[y][x-1] = "*"
                            break
                    if direction == "E":
                        if data[y-1][x+1] != "#" and data[y][x+1] != "#" and data[y+1][x+1] != "#":
                            if data[y][x+1] == "*" or data[y][x+1] == "X":
                                data[y][x+1] = "X"
                            else:
                                data[y][x+1] = "*"
                            break
    newdata = copy.deepcopy(data)
    for x in range(width):
        for y in range(height):
            if data[y][x]=="#":
                if data[y-1][x-1]!="#" and data[y-1][x]!="#" and data[y-1][x+1]!="#" and data[y][x+1]!="#" and data[y+1][x+1]!="#" and data[y+1][x]!="#" and data[y+1][x-1]!="#" and data[y][x-1]!="#":
                    continue
                for direction in dirs:
                    if direction == "N":
                        if data[y-1][x-1] != "#" and data[y-1][x] != "#" and data[y-1][x+1] != "#":
                            if data[y-1][x]!="X":
                                newdata[y][x] = "."
                                newdata[y-1][x] = "#"
                                Flag = True
                            break
                    if direction == "S":
                        if data[y+1][x-1] != "#" and data[y+1][x] != "#" and data[y+1][x+1] != "#":
                            if data[y+1][x]!="X":
                                newdata[y][x] = "."
                                newdata[y+1][x] = "#"
                                Flag = True
                            break
                    if direction == "W":
                        if data[y-1][x-1] != "#" and data[y][x-1] != "#" and data[y+1][x-1] != "#":
                            if data[y][x-1]!="X":
                                newdata[y][x] = "."
                                newdata[y][x-1] = "#"
                                Flag = True
                            break
                    if direction == "E":
                        if data[y-1][x+1] != "#" and data[y][x+1] != "#" and data[y+1][x+1] != "#":
                            if data[y][x+1]!="X":
                                newdata[y][x] = "."
                                newdata[y][x+1] = "#"
                                Flag = True
                            break
    data = newdata
    for x in range(width):
        for y in range(height):
            if data[y][x]!="#":
                data[y][x] = "."
    dirs.append(dirs.pop(0))
    rounds+=1
    if rounds==10:
        data = ensmallen(ensmallen(data))
        width = len(data[0])
        height = len(data)
        count = 0
        for x in range(width):
            for y in range(height):
                if data[y][x]==".":
                    count+=1
        print(count)

print(rounds)
