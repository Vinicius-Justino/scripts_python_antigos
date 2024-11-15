n1 = 0
n2 = 1
n3 = n1 + n2

print(n1)
print(n2)

for fibonacci in range(1, 101):
    n1 = n2
    n2 = n3
    n3 = n1 + n2
    print(n3)
