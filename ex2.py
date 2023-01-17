def print_factor(x):
    # your code here
    for i in range(x + 1):
        if (i == 0): continue
        if x % i == 0: print(i)