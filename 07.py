data = """my input""".split("\n")

dank =  0
goal = 0
best = 0

def size(dirt):
    global dank
    global goal
    global best
    total = 0
    for x,i in enumerate(dirt):
        if x==0:
            continue
        if type(i)==list:
            total+=size(i)
        else:
            total+=i
    if total <=100000:
        dank+= total
    if goal<=total<=best:
        best = total
    return total


structure = ["/"]
trace = []
for i in data:
    if i[0]=="$":
        if i[2]=="c":
            target = i[5:]
            if target=="..":
                trace.pop()
            else:
                pointer = structure
                for j in trace:
                    pointer = pointer[j]
                for x,j in enumerate(pointer):
                    if type(j)==list:
                        if j[0]==target:
                            trace.append(x)
                            break
        continue
    pointer = structure
    for j in trace:
        pointer = pointer[j]
    if i[0]=="d":
        pointer.append([i[4:]])
    else:
        cool = i.split(" ")
        pointer.append(int(cool[0]))


goal = size(structure) - 40000000
best = 99999999999999999999999999999
dank = 0
size(structure)
print(dank)
print(best)
