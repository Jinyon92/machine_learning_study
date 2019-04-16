items = 'zero one two three'.split()
print(items)
#['zeor' 'one' 'two' 'three']

example = 'python, jquery,javascript'
print(example.split(","))
#['python', 'jquery','javascript']

example = 'python, jquery, javascript'
a,b,c = example.split(",")
print(a)
#python

example = 'cs50.gachon.edu'
subdomain, domain, tld = example.split(".")
#subdomain = cs50, domain = gachon, tld = edu
