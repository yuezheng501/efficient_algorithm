while True:
    n = int(input())
    if n>pow(10, 14) or n<0: break
    result = [0, 1]
    if n == 0 : sum = 0; break
    if n == 1: sum = 1; break
    # sum = 1
    for i in range(2, n+1):
        result.append((result[i-2] + result[i-1]) % 10)
        # sum = (sum + pow(result[i],2)%10 )%10
    break
sum = result[n]*(result[n]+result[n-1])
x = len(str(sum))
print(str(sum)[x-1])