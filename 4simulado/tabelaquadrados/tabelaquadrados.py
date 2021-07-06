x = int(input())
y = int(input())

if x>y:
    print("---")
    exit()

menos = y-x
for i in range(0,menos+1):
    atu = x+i
    print(f'{atu} {atu*atu}')                         
