N = int(input("Enter a number: "))
for i in range(N):
    for j in range(N-i):
        print(chr(65 + j), end="")
    print()