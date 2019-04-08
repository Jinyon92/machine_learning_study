fopen = open('romeo.txt')

di = dict()
for line in fopen:
    line = line.rstrip()
    words = line.split()
    for w in words:
        di[w] = di.get(w, 0) + 1

lst = list()
for key, val in di.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)
for val, key in lst[:10]:
    print(key, val)
