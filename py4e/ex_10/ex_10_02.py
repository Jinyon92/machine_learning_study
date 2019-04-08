fname = input('Enter Filename: ')
if len(fname) < 1 : fname = 'clown.txt'
fopen = open(fname)

di = dict()
for line in fopen:
    line = line.rstrip()
    words = line.split()
    for w in words:
        di[w] = di.get(w,0) + 1

lst = list()
for key, val in di.items():
    newt = (val,key)
    lst.append(newt)

lst = sorted(lst, reverse = True)
for v,k in lst[:5]:
    print(k,v)
