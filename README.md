a = input()
b = len(a) // 2
print(a[:b] == a[:len(a)-b-1:-1])
