# to be finished

last_number = 10000

max_max = 1
max_steps = 1
max_at = 1

print_path = False
print_numbers = False

for i in range(1, last_number):
    x = i
    steps = 0   # aka stopping time
    max = x
    if print_numbers:
        print(x, end='')
    while x != 1: 
        if x % 2 == 0:   # x is even
            x /= 2
            if print_path:
                print(".", end ='')
        else:
            x = 3 * x + 1
            if print_path:
                print("*", end='')
        if max < x:
            max = int(x)
        steps += 1
    if print_path:
        print(f", {max}, {steps}")
    if max_max < max:
        max_max = max
        max_at = i
    if max_steps < steps:
        max_steps = steps
print(f"For the investigated {last_number} numbers we reached a maximum height of {max_max} at {max_at}")
print(f"We also found a maximum of {max_steps} steps.")
