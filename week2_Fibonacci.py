while True:
    n = int(input())
    if n>45: break
    result = [0, 1]
    if n==0 or n==1: break
    for i in range(2, n+1):
        result.append(result[i-2] + result[i-1])
    break
print(result[n])