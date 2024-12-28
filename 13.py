import functools
data = ["my input concatenated into one horrific list"]
data2 = ["my input without the empty lines and with a [[2]] and a [[6]]"]


def compare(a,b):
    if type(a)==int and type(b)==int:
        if a<b:
            return 1
        if b<a:
            return -1
        return 0
    if type(a)==int and type(b)==list:
        return compare([a],b)
    if type(a)==list and type(b)==int:
        return compare(a,[b])
    for i in range(min(len(a),len(b))):
        value = compare(a[i],b[i])
        if value!=0:
            return value

    if len(a)<len(b):
        return 1
    if len(b)<len(a):
        return -1
    return 0

def inverse(a,b):
    return compare(b,a)

count = 0

for i,v in enumerate(data):
    if compare(v[0],v[1])==1:
        count+=i+1

print(count)
total = 1
ordered = sorted(data2,key=functools.cmp_to_key(inverse))
for i,v in enumerate(ordered):
    if v == [[2]] or v == [[6]]:
        total*=i+1
print(total)
