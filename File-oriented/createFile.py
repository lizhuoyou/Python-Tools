#this is used to make new files easily
def makePythonFile(name):
    new = open(str(name)+'.py','w')
    new.close()
def makeTextP(name):
    new = open(str(name)+'.txt','w')
    new.close()
amount = int(input('How many open:'))
usedName = input('name:')
for x in range(1,amount+1):
    makePythonFile(usedName+str(x))
