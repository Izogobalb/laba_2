n = int(input())
a = [None]*n
for i in range(n):
    a[i] = list(map(int, input().split()))


for j in range(1, n):
    key = a[j][1]
    key2 = a[j]
    key3 = a[1][j]
    i = j - 1
    while i >= 0 and a[i][1] < key:
        a[i], a[j] = a[j], a[i]
        i -= 1
    a[i + 1] = key2

for i in range(n):
    print(*a[i])
