# You are given a list of integers, print the index of the two numbers that add up to a
# target number given. 
# <= input = [1,4,5,6]
# <= target = 5 
# => output = 0,1
list_targetted =[1,2,3,4,5]
target= 6
for xx in list_targetted:
    for yy in list_targetted[xx+1:]:
        if xx + yy == target:
            print(list_targetted.index(xx),list_targetted.index(yy))
