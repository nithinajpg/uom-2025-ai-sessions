
def print_christmas_tree():
    x = int(input("Enter height: "))

    for i in range(1, x + 1):
        print(" " * (x - i) + "*" * (2 * i - 1))

def is_subsequence(x0, y0):
    j = 0
    for c in x0:
        while j < len(y0) and y0[j] != c:
            j += 1
        if j == len(y0):
            print(False)
            break
        j += 1
    else:
        print(True)

