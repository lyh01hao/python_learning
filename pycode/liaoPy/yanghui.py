def triangles():
    l = [1]
    while True:
        yield l
        l = [l[i - 1] + l[i] for i in range(1, len(l))]
        l.insert(0, 1)
        l.append(1)
n = 0
results = []
for t in triangles():
        results.append(t)
        n = n + 1
        if n == 10:
            break

for t in results:
    print(t)

