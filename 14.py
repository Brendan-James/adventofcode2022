data = """my input""".split("\n")

data = [i.split(" -> ") for i in data]
data =[[i.split(",") for i in j] for j in data]
data = [[[int(i) for i in j] for j in k] for k in data]

grid = [["-" for j in range(1000)] for i in range(1000)]

best = 0

for i in data:
    for j in range(len(i)-1):
        if i[j][0]==i[j+1][0]:
            for n in range(min(i[j][1],i[j+1][1]),max(i[j][1],i[j+1][1])+1):
                grid[i[j][0]][n] = "#"
                if n > best:
                    best = n
        else:
            for n in range(min(i[j][0],i[j+1][0]),max(i[j][0],i[j+1][0])+1):
                grid[n][i[j][1]] = "#"
                if i[j][1] > best:
                    best = i[j][1]

best+=2

count = 0

while True:
    x = 500
    y = 0
    while y<999:
        if grid[x][y+1] == "-":
            y+=1
            continue
        if grid[x-1][y+1] == "-":
            x-=1
            y+=1
            continue
        if grid[x+1][y+1]== "-":
            x+=1
            y+=1
            continue
        grid[x][y] = "o"
        count+=1
        break
    else:
        break
print("a:",count)

grid = [["#" if i == "#" else "-" for i in j] for j in grid]

for i in range(1000):
    grid[i][best] = "#"

count = 0

while grid[500][0]!="o":
    x = 500
    y = 0
    while y<999:
        if grid[x][y+1] == "-":
            y+=1
            continue
        if grid[x-1][y+1] == "-":
            x-=1
            y+=1
            continue
        if grid[x+1][y+1]== "-":
            x+=1
            y+=1
            continue
        grid[x][y] = "o"
        count+=1
        break
    else:
        break
print("b:",count)
