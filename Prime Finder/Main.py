__author__ = 'Jure'
x = 3
while True:
    for i in range(2, x):
        if x % i == 0:
            break
        elif i >= x / 2:
            print(x)
            break
    x += 1