def merge_invertido(l1,l2):
    i = len(l1) - 1
    j = len(l2) - 1 
    result = []

    while i>=0 and j>=0:
        if l1[i]>l2[j]:
            result.append(l1[i])
            i -=1

        else:
            result.append(l2[j])
            j -=1

    while i>=0:
        result.append(l1[i])
        i-=1

    while j>=0:
        result.append(l2[j])
        j-=1

    return result



