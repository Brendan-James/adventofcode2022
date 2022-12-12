data = """abccccccccccccccccaaccccccccccccccccccccaaaaaaaaaaaaacccccccccccccccccccccccccccccccccccccccccccccccccccccccaaaaaa
abcccccccccccccaaaaaccccccccccccccccccccaaaaaaaaaaaaaccccccccccccccccccccccccccccccccccccccccccccccccccccccccaaaaa
abccccccccccccccaaaaaccccccccccccccaaaaacccaaaaaacccccaaccccccccccccccccccccccccccccccccccccccccccccccccccccccaaaa
abccccccccccccccaaaaacccccccccaacccaaaaacccaaaaaaaccccaaaacaacaaccccccccccccccccccccccccaaaccccaaaccccccccccccaaaa
abcccccccccccccaaaaacccccccaaaaaccaaaaaacccaaaaaaaacaaaaaacaaaaaccccccccccccccccccccccccaaacccaaaaccccccccccccaaac
abccccccaacaaaccccaaccccccccaaaaacaaaaaaccaaaacaaaacaaaaaccaaaaaaccccccccccccccccccccccccaaaaaaaacccccccccccccaacc
abccccccaaaaaaccccccccccccccaaaaacaaaaaaccaaaaccaaaacaaaaacaaaaaacccccccccccccccccccccccaaaaaaaaaccccccccccccccccc
abccccccaaaaaacccccccccccccaaaaaccccaaccccaacccccaaccaacaacaaaaaccccccccccccccccccccccccccaaakkkkllllcccaaaccccccc
abccccccaaaaaaacccccccccccccccaaccccaacccccccccccccccccccccccaaaccccccaaaacccccccccjjjjkkkkkkkkkkllllccccaacaccccc
abcccccaaaaaaaacccccaaccccccccccccccaaaaaaccccccccccccccccccaaccccccccaaaaccccccccjjjjjkkkkkkkkkppllllcccaaaaacccc
abcccccaaaaaaaaccaaaacccccccccccccccaaaaaccccccccccccccccaacaaccccccccaaaacccccccjjjjjjjkkkkkppppppplllccaaaaacccc
abccccccccaaaccccaaaaaacccccccccccaaaaaaaccccccccccccccccaaaaacccccccccaacccccccjjjjoooooooppppppppplllcccaaaccccc
abccccccccaaccccccaaaaaccccaacccccaaaaaaaaccccaaacccccccccaaaaaaacccccccccccccccjjjooooooooppppuuppppllcccaaaccccc
abccccccaacccccccaaaaacccccaaaccaaaaaaaaaaccaaaaaaccccccaaaaaaaaaacaaaccccccccccjjjoooouuuoopuuuuupppllcccaaaccccc
abacccccaaccccccccccaacccccaaaaaaaccaaaaaaccaaaaaaccccccaaaaaccaaaaaaaccccaaccccjjoootuuuuuuuuuuuuvpqlllcccccccccc
abaccaaaaaaaacccccccccccccccaaaaaaccaacccccccaaaaacccccccacaaaccaaaaaaccaaaacaccjjooottuuuuuuuxyuvvqqljjccddcccccc
abcccaaaaaaaaccccccccccccaaaaaaaaacaacaaccccaaaaaccccccccccaaaaaaaaaacccaaaaaacciijootttxxxuuxyyyvvqqjjjjdddcccccc
abcccccaaaaccccaaacccccccaaaaaaaaacaaaaaccccaaaaaccccccccccccaaaaaaaaacccaaaaccciiinntttxxxxxxyyvvqqqqjjjddddccccc
abccccaaaaaccccaaaaacccccaaaaaaaaaaaaaaaaccccccccccccccccccccaaaaaaaaaaccaaaaccciiinntttxxxxxxyyvvvqqqqjjjdddccccc
abccccaaaaaaccaaaaaccccccccaaaaaaaaaaaaaacccccccccccccccccccccccaaacaaacaacaaccciiinnnttxxxxxyyyvvvvqqqqjjjdddcccc
SbccccaaccaaccaaaaacccccccccaaaaaaaaaaaaacccccccccccccccccccccccaaacccccccccccciiinnntttxxxEzzyyyyvvvqqqjjjdddcccc
abcccccccccccccaaaaacccccccaaaaaaaaacaaaccccccccccccccccccccccccaaccccccccccccciiinnnttxxxxyyyyyyyyvvvqqqjjjdddccc
abcccccccccccccaaccccccccccaaaaaaaaccccccccccccccccccccccccccccccccccccccccccciiinnntttxxyyyyyyyyyvvvvqqqjjjdddccc
abccccccccccccccccccccccccaaaaaaaacccccccccccccccccccccccccccccccccccccccccccciiinntttxxxwwwyyywwvvvvrqqjjjjdddccc
abcccccccccccccccccccccccccccaaaaaaccccccccccccccccccccccccccccccccccccccccccciinnntttxwwwwwyyywwvvvrrrqkkkeddcccc
abcccccccccccccccccccccccccccaaaaaaccccccccccccccccccccccccccccccccccccccccccchhnnntttsswwswwyywwrrrrrrkkkkeeecccc
abcccccccccccccccccccccccccccaaaaaacccccccccccccccccccaccccccccccccaaacccccccchhhnmmssssssswwwwwwrrrkkkkkeeeeecccc
abcccccccccccccccccccccccccccccaaacccccccccccccccccccaaccccccccccaaaaaacccccaahhhmmmmmsssssswwwwrrrkkkkkeeeeeccccc
abaacccccccccccccaccccccccccccccccccccccccccccccccaaaaacaacccccccaaaaaacaaaaaahhhhmmmmmmmmssswwwrrkkkkeeeeeacccccc
abacccccccccccccaaaaaaaaccccccccaaacccccccaaccccccaaaaaaaacccccccaaaaaacaaaaaaahhhhmmmmmmmmsssrrrrkkkeeeeeaacccccc
abaaaccccaaccccccaaaaaacccccccccaaacccaacaaaccccccccaaaacccccccccaaaaacccaaaaaaahhhhhhhmmmmlsssrrllkfeeeeaaaaacccc
abaaaccaaaaccccccaaaaaacccccccccaaaaaaaaaaaaaacccccaaaaacccccccccaaaaacccaaaaaaachhhhhgggmllsssrrllkffeaaaaaaacccc
abaacccaaaaaacccaaaaaaaacccccaaaaaaaaaaaaaaaaacccccaacaaacccccccccccccccaaaaaacccccchggggglllllllllfffaaaaaaaacccc
abaaccccaaaacccaaaaaaaaaaccccaaaaaaaaacaaaaaaaccaccaccaaacccccccccccccccaaaaaacccccccccgggglllllllffffaaaaaacccccc
abcccccaaaaacccaaaaaaaaaacccccaaaaaaaccaaaaacccaaaccccccccccccccccccccccccccaacccccccccagggglllllffffccccaaacccccc
abcccccaacaaccccccaaaaacaccaacccaaaaaaaaaaaaaccaaacccccccccccccccccccccccccccccccccccccaagggggffffffcccccccccccccc
abcccccccccccaaaaaaaaacccccaaccaaaaaaaccaaaaacaaaaccccccccccccccccccccccccccccccccccccaaaacgggfffffccccccccccccccc
abcccccccccccaaaaacaacccaaaaaaaaaaccaacccaaaaaaaacccaaccccccccccccccccccccccccccccccccccccccggfffccccccccccccaaaca
abccccccccccaaaaaaccccccaaaaaaaaacccccccccaaaaaaaaaaaacccccccccccccaaaccccccccccccccccccccccaaaccccccccccccccaaaaa
abccccccccccaaaaaaccccccccaaaacccccccccccccaaaaaaaaaaaaccccccccccccaaaaccccccccccccccccccccccaaaccccccccccccccaaaa
abcccccccccccaaaaacccccccaaaaaaccccccccccaaaaaaaaaaaaaaccccccccccccaaaaccccccccccccccccccccccccccccccccccccccaaaaa""".split("\n")

def onestep(start,end):
    alphabet = "SabcdefghijklmnopqrstuvwxyzE"
    if alphabet.index(start)+1>=alphabet.index(end) or (start=="y" or start=="z" and end=="E"):
        return True
    else:
        return False

best = [[5000 for j in data[0]] for i in data]

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j]=="S":
            paths = [[i,j,0]]
            best[i][j]=0
            break

target = [0,0]

while len(paths)>0:
    newpaths = []
    for i in paths:
        letter = data[i[0]][i[1]]
        if letter == "E":
            target = [i[0],i[1]]
            continue
        if i[0]>0:
            if onestep(letter,data[i[0]-1][i[1]]):
                if i[2]+1<best[i[0]-1][i[1]]:
                    best[i[0]-1][i[1]] = i[2]+1
                    newpaths.append([i[0]-1,i[1],i[2]+1])
        if i[1]>0:
            if onestep(letter,data[i[0]][i[1]-1]):
                if i[2]+1<best[i[0]][i[1]-1]:
                    best[i[0]][i[1]-1] = i[2]+1
                    newpaths.append([i[0],i[1]-1,i[2]+1])
        if i[0]<len(data)-1:
            if onestep(letter,data[i[0]+1][i[1]]):
                if i[2]+1<best[i[0]+1][i[1]]:
                    best[i[0]+1][i[1]] = i[2]+1
                    newpaths.append([i[0]+1,i[1],i[2]+1])
        if i[1]<len(data[0])-1:
            if onestep(letter,data[i[0]][i[1]+1]):
                if i[2]+1<best[i[0]][i[1]+1]:
                    best[i[0]][i[1]+1] = i[2]+1
                    newpaths.append([i[0],i[1]+1,i[2]+1])
    paths = newpaths

print(best[target[0]][target[1]])




bestest = 5000


for x in range(len(data)):
    for y in range(len(data[0])):
        if data[x][y]!="a" and data[x][y]!="S":
            continue
        paths = [[x,y,0]]
        best = [[5000 for j in data[0]] for i in data]
        best[x][y]=0

        target = [0,0]

        while len(paths)>0:
            newpaths = []
            for i in paths:
                letter = data[i[0]][i[1]]
                if letter == "E":
                    target = [i[0],i[1]]
                    continue
                if i[0]>0:
                    if onestep(letter,data[i[0]-1][i[1]]):
                        if i[2]+1<best[i[0]-1][i[1]]:
                            best[i[0]-1][i[1]] = i[2]+1
                            newpaths.append([i[0]-1,i[1],i[2]+1])
                if i[1]>0:
                    if onestep(letter,data[i[0]][i[1]-1]):
                        if i[2]+1<best[i[0]][i[1]-1]:
                            best[i[0]][i[1]-1] = i[2]+1
                            newpaths.append([i[0],i[1]-1,i[2]+1])
                if i[0]<len(data)-1:
                    if onestep(letter,data[i[0]+1][i[1]]):
                        if i[2]+1<best[i[0]+1][i[1]]:
                            best[i[0]+1][i[1]] = i[2]+1
                            newpaths.append([i[0]+1,i[1],i[2]+1])
                if i[1]<len(data[0])-1:
                    if onestep(letter,data[i[0]][i[1]+1]):
                        if i[2]+1<best[i[0]][i[1]+1]:
                            best[i[0]][i[1]+1] = i[2]+1
                            newpaths.append([i[0],i[1]+1,i[2]+1])
            paths = newpaths

        if best[target[0]][target[1]]<bestest:
            bestest = best[target[0]][target[1]]


print(bestest)
