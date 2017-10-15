def search(v,k):
    n = len(v)
    for i in range(n):
        if k == v[i]:
            return i
    return "nincs"

v = [1,4,7,3,"fing",False,123,"busz",7]

print search(v,"fing")

print search(v,"poo")

print(search(v,7))
