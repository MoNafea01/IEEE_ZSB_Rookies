# You are given a list of integers, write a function to get the index of the three numbers 
# that add up to a target number given.
# <= input  = [1,3,5,6,9]
# <= target = 9
# => output = 0,1,2
def target_sum(listx,target):
    for x in listx:
        for y in listx[listx.index(x)+1:]:
            for z in listx[listx.index(y)+1:]:
                if z+y+x==target:
                    return listx.index(x),listx.index(y),listx.index(z)