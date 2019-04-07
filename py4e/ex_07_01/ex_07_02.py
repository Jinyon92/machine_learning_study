fname = input("Enter the file name: ")

try:
    fopen = open(fname)
except:
    print("File cannnot be opened:",fname)
    quit()

count = 0
sum = 0
for line in fopen:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence'):
        pos = line.find(':')
        fnum = line[pos+1:]
        fnum = float(fnum)
        sum = sum + fnum
        count = count + 1
avg = sum/count
print("Average spam Confidence:",avg)
