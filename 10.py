data = """noop
noop
noop
addx 6
addx -1
noop
addx 5
noop
noop
addx -12
addx 19
addx -1
noop
addx 4
addx -11
addx 16
noop
noop
addx 5
addx 3
addx -2
addx 4
noop
noop
noop
addx -37
noop
addx 3
addx 2
addx 5
addx 2
addx 10
addx -9
noop
addx 1
addx 4
addx 2
noop
addx 3
addx 2
addx 5
addx 2
addx 3
addx -2
addx 2
addx 5
addx -40
addx 25
addx -22
addx 2
addx 5
addx 2
addx 3
addx -2
noop
addx 23
addx -18
addx 2
noop
noop
addx 7
noop
noop
addx 5
noop
noop
noop
addx 1
addx 2
addx 5
addx -40
addx 3
addx 8
addx -4
addx 1
addx 4
noop
noop
noop
addx -8
noop
addx 16
addx 2
addx 4
addx 1
noop
addx -17
addx 18
addx 2
addx 5
addx 2
addx 1
addx -11
addx -27
addx 17
addx -10
addx 3
addx -2
addx 2
addx 7
noop
addx -2
noop
addx 3
addx 2
noop
addx 3
addx 2
noop
addx 3
addx 2
addx 5
addx 2
addx -5
addx -2
addx -30
addx 14
addx -7
addx 22
addx -21
addx 2
addx 6
addx 2
addx -1
noop
addx 8
addx -3
noop
addx 5
addx 1
addx 4
noop
addx 3
addx -2
addx 2
addx -11
noop
noop
noop""".split("\n")

clock = 0
x = 1
total = 0
output = ""

def increment():
    global clock
    global x
    global total
    global output
    if clock%40==x or clock%40==x-1 or clock%40==x+1:
        output+="#"
    else:
        output+="."
    clock+=1
    if clock%40==20:
        total+=x*clock
    if clock%40==0:
        output+="\n"

for i in data:
    increment()
    if i[0] == "a":
        increment()
        x+=int(i[5:])
        
print(total)
print(output)
