data = """my input"""

pieces = [["....","....","....","####"],["....",".#..","###.",".#.."],["....","..#.","..#.","###."],["#...","#...","#...","#..."],["....","....","##..","##.."]]

well = [["." for j in range(7)] for i in range(8)]
well.append(["#" for i in range(7)])

def intersect(x,y):
    global pieces
    global piece
    global well
    for i in range(4):
        for j in range(4):
            if pieces[piece][j][i]=="#":
                if i+x>=7 or i+x<0:
                    return True
                if well[y+j-3][x+i] == "#":
                    return True
    return False

piece = 0
height = 0
movement = 0
seen = {}
cool = 0
goal = 0
target = 1000000000000
# 1000000000000
while goal<target:
    if str(piece)+","+str(movement) in seen:
        if seen[str(piece)+","+str(movement)][0] == 1:
            seen[str(piece)+","+str(movement)] = [2,goal,height]
        elif seen[str(piece)+","+str(movement)][0] == 2:
            distance = goal - seen[str(piece)+","+str(movement)][1]
            dankness = (target-goal-1)//distance
            goal+=dankness*distance
            cool += (height-seen[str(piece)+","+str(movement)][2])*dankness
    else:
        seen[str(piece)+","+str(movement)] = [1]
    x = 2
    y = 4
    while True:
        if data[movement] == ">":
            if not intersect(x+1,y):
                x+=1

        else:
            if not intersect(x-1,y):
                x-=1
        movement+=1
        movement%=len(data)
        if not intersect(x,y+1):
            y+=1
        else:
            break
    for i in range(4):
        for j in range(4):
            if pieces[piece][j][i] == "#":
                well[y+j-3][x+i] = "#"
                if len(well)-1-(y+j-3)>height:
                    height = len(well)-1-(y+j-3)

    while len(well)<height+9:
        well.insert(0,["." for i in range(7)])
    piece+=1
    piece%=5
    goal+=1

print(height+cool)
