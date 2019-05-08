import sys, mytimer
reps = 10000
replisr = range(reps)
def forLoop():
    res =[]
    for x in replisr:
        res.append(abs(x))
    return res
def listComp():
    return [abs(x) for x in replisr]
def mapCall():
    return list(map(abs,replisr))
def genExpr():
    return list(abs(x) for x in replisr)
def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
        return list(gen())
print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    elapsed, result = mytimer.timer(test)
    print('-' *33)
    print(' % -9s: % .5f = > [ % s... % s]'%
          (test.__name__, elapsed, result[0], result[-1]))
