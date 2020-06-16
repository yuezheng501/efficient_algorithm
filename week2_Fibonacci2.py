while True:
    n = int(input())
    if n>pow(10, 7): break
    result = [0, 1]
    if n==0 or n==1: break
    for i in range(2, n+1):
        result.append((result[i-2] + result[i-1]) % 10)
    break
x = len(str(result[n]))
print(str(result[n])[x-1])