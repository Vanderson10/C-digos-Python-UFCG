l = [7,2,1,8,0,3,4,2]
troca = True

for j in range(len(l)-1,-1,-1):
    if not troca: break
    for i in range(j):
        troca = False
        if l[i]>l[i+1]:
            l[i],l[i+1] = l[i+1], l[i]
            troca = True 

print(l)
        
