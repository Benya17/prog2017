from random import random

TESTS = 100


def f(i):
    global counts
    counts += 1
    b = i <= maxlev
    if not b:
        global broken
        broken += 1
    return b



def fun():
    i = 1
    while f(i):
        i += 1
    return i-1

        


breaklist = []
countlist = []
maxlevs = []
corrects = []

for testno in range(TESTS):
    broken = 0
    counts = 0
    maxlev = int(random() * 100) + 1
    check = fun()
    correct = (check == maxlev)
    maxlevs.append(maxlev)
    countlist.append(counts)
    breaklist.append(broken)
    corrects.append(correct)


if sum(corrects)==TESTS:
    print "All correct"
else:
    print "WRONG:"
    print corrects
    print maxlevs



print 'Maximum broken eggs:', max(breaklist)

print "\n"

print 'Average drop count: ', sum(countlist)/float(TESTS)
print 'Average max height: ', sum(maxlevs)/float(TESTS)

print "\n"

print 'Maximum drop count: ', max(countlist)
print 'Maximum max height: ', max(maxlevs)

print "\n"

print 'Minimum drop count: ', min(countlist)
print 'Minimum max height: ', min(maxlevs)

