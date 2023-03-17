# Find the minimum distance between the same numbers in a list
# <= input  = [2, 5, 3, 4, 5 , 2]        
# <= target = 2
# => output = 5
# <= input  = [2, 5, 3, 4, 5 , 2] 
# <= target = 5
# => output = 3
x,num = [2, 5, 3, 4, 5 , 2],5
def min_dist(x,num):
    import random
    lst_=[]
    lst_rnd=[]
    min_=9999
    for i in x:
        if i==num :
            n=random.random()
            lst_.append(n)
            lst_rnd.append(n)
        else:
            lst_.append(i)
    for i in lst_rnd[:(len(lst_rnd))-1]:
                min_ = min((lst_.index(lst_rnd[lst_rnd.index(i)+1])) - lst_.index(i),min_)
    return min_
