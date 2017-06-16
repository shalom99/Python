
def SubFib(startNumber, endNumber):
    n = 0
    cur = f(n)
    while cur <= endNumber:
        if startNumber <= cur:
            print cur
        n += 1
        cur = f(n)

answer = SubFib(0,4000000)
print answer