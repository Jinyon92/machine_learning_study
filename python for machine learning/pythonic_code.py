#일반 코드
colors = ["red", "blue", 'yellow', 'green']
result = ""

for s in colors:
    result += s

print(result)

#pythonic code
colors = ["red", "blue", 'yellow', 'green']
result = "".join(colors)

print(result)
