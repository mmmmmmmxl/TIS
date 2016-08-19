from db import select


g = (x*x for x in range(10))

l = [next(g) for i in range(10)]

print l