def search(v,k):
    n = len(v)
    for i in range(n):
        if k == v[i]:
            return i
    return "nincs"






t = [1,4,7,3,"fing",False,123,"busz",7]

print search(t,"fing")

print search(t,"poo")

print search(t,7)



tof = ['jajj',True,87,11,"busz"]

i = 0

while search(t,tof[i]) == "nincs":
    i = i+1
    print "nincs meg: ", tof[i-1]
    print "most keresem: ", tof[i]

print "megvan"

