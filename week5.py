def search(v,k):
    n = len(v)
    for i in range(n):
        if k == v[i] and type(k) == type(v[i]):
            return i
    return "nincs"






t = [1,4,7,3,"fing",False,123,"busz",7]

print search(t,"fing")

print search(t,"poo")

print search(t,7)



tof = ['fing3',True,87,11,1.2,"busz",876,46464,42]

i = 0

while search(t,tof[i]) == "nincs":
    i = i+1
    print "nincs meg: ", tof[i-1]
    print "most keresem: ", tof[i]


print "megvan"

