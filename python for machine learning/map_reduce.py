#map 활용
#python3에는 list를 꼭 붙여줘야
ex = [1,2,3,4,5]
f = lambda x: x ** 2
print(list(map(f,ex)))

f = lambda x, y : x+y
print(list(map(f,ex,ex)))
print(list(map(lambda x: x ** 2 if x % 2 == 0 else x, ex)))
print(list(map(lambda x: x+x, ex)))

f = lambda x: x ** 2
for i in map(f,ex):
    print(i)

result = map(f,ex)
print(result)
print(next(result))

#Reduce
from functools import reduce
print(reduce(lambda x,y : x+y, [1,2,3,4,5]))

def factorial(n):
    return reduce(lambda x, y :  x*y, range(1,n+1))

print(factorial(5))
