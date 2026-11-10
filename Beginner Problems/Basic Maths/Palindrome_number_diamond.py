n = int(input("Enter a number: "))

for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for j in range(i + 1, 0, -1):
        print(j, end=" ")
    for j in range(2, i + 2):
        print(j, end=" ")
    print()
for i in range(1, n):
    for j in range(1, i + 1):
        print(" ", end=" ")
    for j in range(n-i, 0, -1):
        print(j, end=" ")
    for j in range(2, n - i + 1):
        print(j, end=" ")
    print()