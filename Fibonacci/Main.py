__author__ = 'Jure'
x = 1
y = 0
c = 0
while True:
    print(x + y)
    if c % 2 == 0:
        x += y
    else:
        y += x
    c += 1