# Given a list of integers, write a function to sort a list and another function to return the 
# first and last appearance of a given target in the sorted list.
# <= input  = [5,7,7,8,8,8,10]
# <= target = 8
# => output = [3,5]
def fl_appearance(x1,target):
    sorter(x1)
    target1=x1.index(target)
    x2=[]
    n1=0
    n2=len(x1)-1
    for x in x1:
        x2.insert(n1,x1[n2])
        n1+=1
        n2-=1
    target2=len(x2) - x2.index(target) - 1
    return target1,target2
def sorter(listh):
    listh.sort()
    return listh
x1=[5,7,2,8,8,8,10]
target = 8