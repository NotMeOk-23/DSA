N = int(input("Enter a number:"))

for i in range(N):
    ch = chr(65 + i)
    for j in range(i+1):
        print(ch, end="")
    print()