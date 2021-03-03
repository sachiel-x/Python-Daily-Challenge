def checkprime(inp):
    l1=[]
    for i in range(2,inp):
        if inp%i == 0:
            l1.append(i)    
    return len(l1)==0

def getfactor(inp):
    l1=[]
    for i in range(2,inp):
        if inp%i == 0:
            l1.append(i)    
    return l1

def Semiprime(inp):
    l2=getfactor(inp)
    l3=[]
    for i in l2:
        if checkprime(i):
            l3.append(i)
    
    print(l2)
    print(l3)
    
    if len(l3)==1:
        return "Semiprime"
    elif len(l3)>1:
        return "Squarefree Semiprime"
    else:
        return "Neither"

Semiprime(49)