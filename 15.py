# this one is a little sketchy

data = """my input""".split("\n")


data = [[int(i[12:i.index(",")]),int(i[i.index(",")+4:i.index(":")]),int(i[i.index("s a")+7:i.index(",",20)]),int(i[i.index(",",20)+4:])] for i in data]

y = 2000000
#y = 10

def taxicab(ax,ay,bx,by):
    return abs(ax-bx)+abs(ay-by)

for i in data:
    i.append(taxicab(i[0],i[1],i[2],i[3]))

print(data)

ranges = []
for i in data:
    neg = taxicab(-100000000,y,i[0],i[1])
    pos = taxicab(100000000,y,i[0],i[1])
    if -100000000+(neg-i[4])<100000000-(pos-i[4]):
        ranges.append([-100000000+(neg-i[4]),100000000-(pos-i[4])])

def clean():
    global ranges
    for i,v in enumerate(ranges):
        for j,n in enumerate(ranges):
            if i>=j:
                continue
            if v[0]<=n[0]<=v[1] or v[0]<=n[1]<=v[1] or n[0]<=v[0]<=n[1] or n[0]<=v[1]<=n[1]:
                ranges.pop(j)
                ranges.pop(i)
                ranges.append([min(v[0],n[0]),max(v[1],n[1])])
                return True
    return False

while clean():
    print(ranges)


print(ranges)

count = 0
for i in ranges:
    count+=i[1]-i[0]+1
print(count-1)

print(3405562*4000000+3246513)

for y in range(0,4000000):
    ranges = []
    for i in data:
        neg = taxicab(-100000000,y,i[0],i[1])
        pos = taxicab(100000000,y,i[0],i[1])
        if -100000000+(neg-i[4])<100000000-(pos-i[4]):
            ranges.append([-100000000+(neg-i[4]),100000000-(pos-i[4])])
    while clean():
        pass
    if len(ranges)>1:
        print(ranges,y)
