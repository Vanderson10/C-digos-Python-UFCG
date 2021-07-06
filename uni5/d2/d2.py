
n = int(input())
quant = len(str(n))

i=quant
e = 0
while i>0:
    num = (n//(10**e)%10)
    e+=1
    i-=1
    print(num)


