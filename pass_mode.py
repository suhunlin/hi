def f1(x):
    x.append(1)
    print('f1:x(after append value 1 to x) =',x)

y = [0]
f1(y)
print('y(after passing y to f1) = ',y)


def f2(x):
    x += 1
    print('f2:x(after x += 1) =',x)

z = 0
f2(z)
print('z(after passing z to f2) =',z)