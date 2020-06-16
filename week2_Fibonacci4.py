
while True:
    x = input().split()
    n0 = int(x[0])
    n1 = int(x[1])
    if not 0 <= n0 <= n1 <= pow(10, 14) : break
    result = [0, 1]
    for i in range(2, n0+1):
        result.append((result[i-2] + result[i-1]) % 10)
    sum = result[n0]
    if n0 == n1: break
    for j in range(n0+1, n1+1):
        result.append((result[j - 2] + result[j - 1]) % 10)
        sum = sum + result[j]
    break

x = len(str(sum))
print(str(sum)[x-1])