fopen = open('mbox-short.txt')

for line in fopen:
    line.rstrip()
    words = line.split()
    #guardian pattern
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])
