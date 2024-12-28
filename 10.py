data = """my input""".split("\n")

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
