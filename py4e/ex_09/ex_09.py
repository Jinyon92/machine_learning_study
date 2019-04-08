fname = input('Enter filename:')
if len(fname) < 1 : fname = 'crown.txt'
fopen = open(fname)

di = dict()
for line in fopen:
    line = line.rstrip()
    words = line.split()
    for w in words:
        di[w] = di.get(w, 0) + 1

max_num = 0
word = None
for key,value in di.items():
    if max_num < value:
        max_num = value
        word = key

print("largest Word:",word)
print("count:",max_num)
