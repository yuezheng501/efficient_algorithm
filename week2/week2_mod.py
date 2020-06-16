x = input().split()
n = int(x[0])
m = int(x[1])
count = 0
while True:
    if n<1 or n>pow(10, 14) or m<2 or m>pow(10, 3): break
    fibonacci = [0, 1]
    y = [int(0%m), int(1%m)]
    if n == 1: result = fibonacci[n] % m; break
    else:
        for i in range(2, n + 1):
            fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])
            count = count+1
            y.append(fibonacci[i]%m)
            if ((fibonacci[i])%m) ==1 and ((fibonacci[i-1])%m) ==0:
                break
        if count<(n-1):
            result = y[n % count]
            break
        else:
            result = fibonacci[n] % m
            break
print(result)
