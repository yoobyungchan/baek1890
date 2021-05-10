t = int(input())

a = [list(map(int, input().split())) for _ in range(t)]

d = [[0]*t for _ in range(t)]

d[0][0] = 1

for i in range(t):
    for j in range(t):
        if a[i][j] == 0:
            continue
        if a[i][j] + i < t:
            d[i+a[i][j]][j] += d[i][j]
        if a[i][j] + j < t:
            d[i][a[i][j] + j] += d[i][j]

print(d[t-1][t-1])


