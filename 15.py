# this one is a little sketchy

data = """Sensor at x=1638847, y=3775370: closest beacon is at x=2498385, y=3565515
Sensor at x=3654046, y=17188: closest beacon is at x=3628729, y=113719
Sensor at x=3255262, y=2496809: closest beacon is at x=3266439, y=2494761
Sensor at x=3743681, y=1144821: closest beacon is at x=3628729, y=113719
Sensor at x=801506, y=2605771: closest beacon is at x=1043356, y=2000000
Sensor at x=2933878, y=5850: closest beacon is at x=3628729, y=113719
Sensor at x=3833210, y=12449: closest beacon is at x=3628729, y=113719
Sensor at x=2604874, y=3991135: closest beacon is at x=2498385, y=3565515
Sensor at x=1287765, y=1415912: closest beacon is at x=1043356, y=2000000
Sensor at x=3111474, y=3680987: closest beacon is at x=2498385, y=3565515
Sensor at x=2823460, y=1679092: closest beacon is at x=3212538, y=2537816
Sensor at x=580633, y=1973060: closest beacon is at x=1043356, y=2000000
Sensor at x=3983949, y=236589: closest beacon is at x=3628729, y=113719
Sensor at x=3312433, y=246388: closest beacon is at x=3628729, y=113719
Sensor at x=505, y=67828: closest beacon is at x=-645204, y=289136
Sensor at x=1566406, y=647261: closest beacon is at x=1043356, y=2000000
Sensor at x=2210221, y=2960790: closest beacon is at x=2498385, y=3565515
Sensor at x=3538385, y=1990300: closest beacon is at x=3266439, y=2494761
Sensor at x=3780372, y=2801075: closest beacon is at x=3266439, y=2494761
Sensor at x=312110, y=1285740: closest beacon is at x=1043356, y=2000000
Sensor at x=51945, y=2855778: closest beacon is at x=-32922, y=3577599
Sensor at x=1387635, y=2875487: closest beacon is at x=1043356, y=2000000
Sensor at x=82486, y=3631563: closest beacon is at x=-32922, y=3577599
Sensor at x=3689149, y=3669721: closest beacon is at x=3481800, y=4169166
Sensor at x=2085975, y=2190591: closest beacon is at x=1043356, y=2000000
Sensor at x=712588, y=3677889: closest beacon is at x=-32922, y=3577599
Sensor at x=22095, y=3888893: closest beacon is at x=-32922, y=3577599
Sensor at x=3248397, y=2952817: closest beacon is at x=3212538, y=2537816""".split("\n")

data2 = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".split("\n")


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
