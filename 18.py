data = """my input""".split("\n")




data = [i.split(",") for i in data]
data = [[int(i) for i in j] for j in data]

grid = [[[False for i in range(23)] for j in range(23)] for k in range(23)]

for i in data:
    grid[i[0]][i[1]][i[2]] = True

count = 0
for i in data:
    for x in [-1,1]:
        if i[0]+x<0:
            count+=1
        else:
            if not grid[i[0]+x][i[1]][i[2]]:
                count+=1
        if i[1]+x<0:
            count+=1
        else:
            if not grid[i[0]][i[1]+x][i[2]]:
                count+=1
        if i[2]+x<0:
            count+=1
        else:
            if not grid[i[0]][i[1]][i[2]+x]:
                count+=1
print(count)

positions = [[22,22,22]]

while len(positions)!=0:
    newpositions = []
    for i in positions:
        for x in [-1,1]:
            if 0<=i[0]+x<23:
                if grid[i[0]+x][i[1]][i[2]] == False:
                    grid[i[0]+x][i[1]][i[2]] = "x"
                    newpositions.append([i[0]+x,i[1],i[2]])
            if 0<=i[1]+x<23:
                if grid[i[0]][i[1]+x][i[2]] == False:
                    grid[i[0]][i[1]+x][i[2]] = "x"
                    newpositions.append([i[0],i[1]+x,i[2]])
            if 0<=i[2]+x<23:
                if grid[i[0]][i[1]][i[2]+x] == False:
                    grid[i[0]][i[1]][i[2]+x] = "x"
                    newpositions.append([i[0],i[1],i[2]+x])
    positions = newpositions

count = 0
for i in data:
    for x in [-1,1]:
        if i[0]+x<0:
            count+=1
        else:
            if grid[i[0]+x][i[1]][i[2]] == "x":
                count+=1
        if i[1]+x<0:
            count+=1
        else:
            if grid[i[0]][i[1]+x][i[2]] == "x":
                count+=1
        if i[2]+x<0:
            count+=1
        else:
            if grid[i[0]][i[1]][i[2]+x] == "x":
                count+=1
print(count)
