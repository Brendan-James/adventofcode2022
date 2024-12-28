data = """my input""".split("\n")

data = [i.split(" ") for i in data]

h = [0,0]
t = [0,0]
visited = [str(t)]
for i in data:
    for j in range(int(i[1])):
        if i[0]=="U":
            h[0]+=1
        if i[0]=="D":
            h[0]-=1
        if i[0]=="L":
            h[1]+=1
        if i[0]=="R":
            h[1]-=1
        difference = [h[0]-t[0],h[1]-t[1]]
        if difference[0]==2:
            t[0]+=1
            t[1]=h[1]
        elif difference[0]==-2:
            t[0]-=1
            t[1]=h[1]
        elif difference[1]==2:
            t[1]+=1
            t[0]=h[0]
        elif difference[1]==-2:
            t[1]-=1
            t[0]=h[0]
        else:
            continue
        if str(t) not in visited:
            visited.append(str(t))

#print(visited,len(visited))

def sign(n):
    if n==0:
        return 0
    if n>0:
        return 1
    return -1

def follow(a,b):
    difference = [a[0]-b[0],a[1]-b[1]]
    if abs(difference[0])>=2 or abs(difference[1])>=2:
        b[0]+=sign(difference[0])
        b[1]+=sign(difference[1])
    return b

print(follow([-1,2],[0,1]))

rope = [[0,0] for i in range(10)]
visited = [str(rope[-1])]
for i in data:
    for j in range(int(i[1])):
        if i[0]=="U":
            rope[0][0]+=1
        if i[0]=="D":
            rope[0][0]-=1
        if i[0]=="L":
            rope[0][1]+=1
        if i[0]=="R":
            rope[0][1]-=1
        for n in range(9):
            rope[n+1]=follow(rope[n],rope[n+1])
        if str(rope[-1]) not in visited:
            visited.append(str(rope[-1]))

print(visited,len(visited))
