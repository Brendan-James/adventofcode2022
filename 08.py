data = """my input""".split("\n")

data = [[int(i) for i in j] for j in data]

truthtable = [[0 for i in j] for j in data]

for i in range(len(data)):
    highest = -1
    for j in range(len(data)):
        if data[i][j]>highest:
            highest = data[i][j]
            truthtable[i][j] = 1
    highest = -1
    for j in range(len(data)):
        if data[j][i]>highest:
            highest = data[j][i]
            truthtable[j][i] = 1
    highest = -1
    for j in reversed(range(len(data))):
        if data[i][j]>highest:
            highest = data[i][j]
            truthtable[i][j] = 1
    highest = -1
    for j in reversed(range(len(data))):
        if data[j][i]>highest:
            highest = data[j][i]
            truthtable[j][i] = 1

print(sum([sum(i) for i in truthtable]))

best = 0
cool = [0,0]

for i in range(len(data)):
    for j in range(len(data)):
        height = data[i][j]
        total = 1
        count = 0
        for n in reversed(range(i)):
            count+=1
            if data[n][j]>=height:
                break
        total*=count
        count = 0
        for n in reversed(range(j)):
            count+=1
            if data[i][n]>=height:
                break
        total*=count
        count = 0
        for n in range(i+1,len(data)):
            count+=1
            if data[n][j]>=height:
                break
        total*=count
        count = 0
        for n in range(j+1,len(data)):
            count+=1
            if data[i][n]>=height:
                break
        total*=count
        if total>best:
            best = total
            cool = [i,j]


print(best)
