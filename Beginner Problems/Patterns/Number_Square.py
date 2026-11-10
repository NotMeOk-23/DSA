n = int(input("Enter a number: "))

for i in range(2 * n - 1):
    for j in range(2 * n - 1):
        top = i
        left = (2 * n - 2) - i
        bottom = j
        right = (2 * n - 2) - j
        minDist = min(top, bottom, left, right)
        print(n - minDist, end=" ")
    print()