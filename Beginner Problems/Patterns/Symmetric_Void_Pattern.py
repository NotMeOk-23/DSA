N = int(input("Enter a number: "))
iniS = 0
for i in range(N):
    print("*" * (N-i), end="")
    print(" " * iniS, end="")
    print("*" * (N-i), end="")
    print()
    iniS += 2
iniS = 2 * N - 2
for i in range(N):
    print("*" * (i + 1), end="")
    print(" " * iniS, end="")
    print("*" * (i + 1), end="")
    print()
    iniS -= 2