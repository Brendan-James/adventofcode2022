data = """my input""".split("\n")

data = [[i,int(v)] for i,v in enumerate(data)]

for tar in range(len(data)):
    for i in range(len(data)):
        if data[i][0] == tar:
            cur = data.pop(i)
            n = (i+cur[1])%len(data)
            data.insert(n,cur)
            break 
print(data)


index = 0
total = 0
while True:
    if data[index][1]==0:
        break
    index+=1

for i in range(3000):
    if (i+1)%1000==0:
        total+=data[(i+index+1)%len(data)][1]    

print(total)

data = """my input but again""".split("\n")

data = [[i,int(v)*811589153] for i,v in enumerate(data)]

for mixes in range(10):
    for tar in range(len(data)):
        for i in range(len(data)):
            if data[i][0] == tar:
                cur = data.pop(i)
                n = (i+cur[1])%len(data)
                data.insert(n,cur)
                break 


index = 0
total = 0
while True:
    if data[index][1]==0:
        break
    index+=1

for i in range(3000):
    if (i+1)%1000==0:
        total+=data[(i+index+1)%len(data)][1]    

print(total)
