#coding: utf-8

#1-es feladat:

def search(v,k):
    n = len(v)
    for i in range(n):
        if k == v[i] and type(k) == type(v[i]):
            return i
    return "nincs"




def metszet(l1,l2):
    n = len(l1)
    for i in range(n):
        talal = search(l2,l1[i])
        if talal != "nincs":
            return [i,l1[i]]
    return "nincs"    


t = [1,4,7,3,"fing",False,123,"busz",7]


tof = ['fing3',True,87,11,1.2,"busz",876,46464,42]

tof2 = ['kaja',23,11.2,'NEMJO',876,'kocsi']

print '1-es:'

print metszet(t,tof)

print metszet(t,tof2)

print metszet(tof,tof2)

print metszet(tof2,tof)

#2-es feladat:
def mod(v):
    c = 0
    for i in range(len(v)):
        n = 0
        for j in range(i,len(v)):
            if v[i] == v[j] and type(v[i]) == type(v[j]):
                n +=1
        if n > c:
            c = n
            ind = i
            val = v[i]
    return [val,c]


print '2-es:'

print mod([1,44,6,5,3,21,21,1,1,3,21,9,9,9,9])

print mod([1,'boo','foo','ajjajj',12,13,9,'boo',0,True,False])



#a programban legyen egy függvény ami elvégzi tetszőleges szám prímtényezős felbontását és visszaadja a prímosztóinak listáját:

def isprime(n):
    if n == 2:
        return True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def factors(n):
    primes = []
    for i in range(2,n):
       if n % i == 0 and isprime(i):
           primes.append(i)
    return primes


print "primfelbontas:"

print "21:  ", factors(21)

print "123: ",factors(123)

print "20000: ",factors(20000)

print "32450: ",factors(32450)

print "7124361: ",factors(7124361)


#írj egy függvényt, ami megadja két szám lekisebb közös többszörösének és legnagyobb közös osztójának hányadosát:

#nagyon lassú és béna megoldás, de működik! egyelőre ennyi kell

def lkt(a,b):
    c = a
    while c % b != 0 or c % a != 0:
        c = c+1
    return c

def lko(a,b):
    c = a
    while b % c != 0 or a % c != 0:
        c = c-1
    return c

def ratio(a,b):
    return float(lkt(a,b))/float(lko(a,b))

print "LKT/LKO: "


print "23 és 35:"
print lkt(23,35)
print lko(23,35)
print ratio(23,35)


print "18 és 60:"
print lkt(60,18)
print lko(60,18)
print ratio(60,18)


print "240 és 45:"
print lkt(240,45)
print lko(45,240)
print ratio(240,45)



#versenyfeladat:

#a programban nem vehet fel egyetlen változó (vagy tömbváltozó eleme) sem 9-nél nagyobb abszolút értékű egész számot, vagy bármilyen tört számot. nem csak kezdőértékként, egyetlen állapotban sem.

#nem szerepelhet benne sehol 9 eleműnél hosszabb tömb

#nem lehet több mint 8 sor

print "sokáig futó program: az elágazás feltételét kb 18^9 * 9 = 1785233613312 alkalommal ellenőrzi le"
t = [-9,-9,-9,-9,-9,-9,-9,-9,-9]
while t[8] < 9:
    for i in range(9):
        if t[i] == 9:
            t[i] = -9
            t[i+1] = t[i+1] + 1
    t[0] += 1








