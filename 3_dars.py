def ArifmeticOperators(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
print(ArifmeticOperators(3,8))    

def Divition(a,b):
    print(a//b)
    print(a/b)
Divition(3,6)    

def loops(n):
    for i in range(n):
        print(i*i)
print(loops(5))

def Function(n):
    s=""
    for i in range(1,n+1):
        s+=str(i)
    print(int(s))
Function(5)    


def List_Comprehensions(x,y,z,n):
    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) 
    for k in range(z + 1) if i + j + k != n]
    print(coordinates)


def lists(N):
    lst = []
    for _ in range(N):
        command = input().split()
        if command[0] == "insert":
            lst.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(lst)
        elif command[0] == "remove":
            lst.remove(int(command[1]))
        elif command[0] == "append":
            lst.append(int(command[1]))
        elif command[0] == "sort":
            lst.sort()
        elif command[0] == "pop":
            lst.pop()
        elif command[0] == "reverse":
            lst.reverse()
lists(12)


def toq_juft(n):
    if n%2==0:
        print("juft")
    else:
        print("toq") 
print(toq_juft(5))        
    

"""
gitga faylni update qilish
git add .
git commit -m "update"    
git push -u origin main
"""

