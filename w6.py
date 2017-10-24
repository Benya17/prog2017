def mod(v):
    c = 0
    for i in range(len(v)):
        n = 0
        for j in range(i,len(v)):
            if v[i] == v[j]:
                n +=1
        if n > c:
            c = n
            ind = i
            val = v[i]
    return [c,ind,val]


print mod([1,44,6,5,3,21,21,1,1,3,21,9,9,9,9])
