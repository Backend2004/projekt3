# python referense (boglash)  link obektga yonaltirilgan link
""""
a='python'
print(id(a))
print(hex(id(a)))"""

# mutable ozgartirib boladi
# immutable ozgartirib bolmaydi
# pip3 install cowsay
"""import cowsay
cowsay.cow("dckjdkj")"""
"""
def boluvchilar(son):
    c=0
    boluvchi = []
    for i in range(1, son + 1):
        if son % i == 0:
            c+=1
            boluvchi.append(i)
    return c
print(boluvchilar(12)) """
"""
def tub_Count(list1: list[int]) -> int:
    result = 0
    for i in list1:
        c = 0
        for j in range(1, i + 1):
            if i % j == 0:
                c += 1
        if c == 2:
            result += 1
    return result
list1 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(tub_Count(list1))"""

"""
def tub(num):
    c=0
    for i in range(1,num+1):
        if num%i==0:
            c+=1
    if c==2:
        return 'tub son'
    else:
        return 'tub emas'
print(tub(7))           """ 
 

l1=[0,1,2,3,4,5,6,7]
l2=[3,5,7,2,1,0,3,4]
l3=[0,1,2,3,4,5,6,7]
if l1==l3:
    print(True)
else:
    print(False)    
def next_id(arr):
    arr1=sorted(arr)
    if arr1==arr:
        return len(arr)
    else:
        return 0
print(next_id(l2))    


