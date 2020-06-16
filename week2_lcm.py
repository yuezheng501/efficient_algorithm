# a,b = [int(x) for x in input().split()]
x = input().split()
a = int(x[0])
b = int(x[1])
while True:
    if a<1 or b>pow(10, 9)*2: break
    if b == 0:
        result = a
        break
    while a!=0 and b!=0 :
        if a==b:
            result = a
            break
        elif a>b: a = a%b
        else: b = b%a
    if b== 0: result= a; break
    else: result= b; break
result = int((int(x[0])/result)*int(x[1]))
print(result)

