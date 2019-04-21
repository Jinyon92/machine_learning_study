u = [2,2]
v = [2,3]
z = [3,5]

result = [sum(t) for t in zip(u,v,z)]
print(result)

u = [1,2,3]
v = [4,5,6]
alpha = 2

result = [alpha * sum(t) for t in zip(u,v)]
print(result)
