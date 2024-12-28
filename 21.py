data = """my input""".split("\n")

monke = {}

for i in data:
    monke[i[:4]] = i[6:]

def calculate(m):
    global monke
    if len(monke[m]) == 11:
        if monke[m][5]=="+":
            return calculate(monke[m][:4])+calculate(monke[m][-4:])
        if monke[m][5]=="-":
            return calculate(monke[m][:4])-calculate(monke[m][-4:])
        if monke[m][5]=="*":
            return calculate(monke[m][:4])*calculate(monke[m][-4:])
        if monke[m][5]=="/":
            return calculate(monke[m][:4])//calculate(monke[m][-4:])
    else:
        return int(monke[m])

print(calculate("root"))

# just decided to binary search this one by hand
monke["humn"] = str(3587647562851)
print(calculate("fglq")-calculate("fzbp"))
