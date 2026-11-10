N = int(input("Enter a number: "))

for i in range(N):
    # ch = chr(65 + (2 * i + 1) // 2)
    for j in range(N-i-1):
        print(" ", end="")
    for j in range(i+1):
        print(chr(65+j),  end="" )
    for j in range(i-1, -1, -1):
        print(chr(65 + j), end="")
    print()