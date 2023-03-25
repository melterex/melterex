a = int(input())
b = int(input())
c = int(input())
x = 0
maxl = max(a, b, c)
midl = a+b+c - min(a,b,c) - max(a,b,c)
minl = min(a, b, c)
print(minl + midl - maxl)