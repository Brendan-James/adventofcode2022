data = """my input""".split("\n")

data = [[i for i in j] for j in data]

total = 0
for i in data:
    for j,v in enumerate(reversed(i)):
        if v == "-":
            num = -1
        elif v== "=":
            num = -2
        else:
            num = int(v)
        total+=5**j*num
result = ""
while total!=0:
    remainder = total%5
    if remainder == 3:
        total+=2
        result+="="
    elif remainder == 4:
        total+=1
        result+="-"
    else:
        total-=remainder
        result+=str(remainder)
    total=total//5
print("".join([i for i in reversed(result)]))
