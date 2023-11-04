# to be finished

last_number = 100

for i in range(1, last_number):
    x = i
    steps = 1
    max = x
    print(x, end='')
    while x != 1: 
        if x % 2 == 0:   # x is even
            print(".", end='')
            x /= 2
        else:
            print("*", end='')
            x = 3 * x + 1
        if max < x:
            max = x
        steps += 1
    print(f", {int(max)}, {steps}")
