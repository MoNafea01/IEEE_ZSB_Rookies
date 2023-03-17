# Write a python function that takes a list and returns a new list with unique elements of 
# the first list. Do not use built-in functions 
# <= input  = [5,7,7,8,8,8,10]
# => output = [5,7,8,10]
def unique_numbers(List_A):
    list_B=[]
    for x in List_A:
        if x not in list_B:
            list_B.append(x)
    return list_B
list2=[5,7,7,2,8,8,8,10,0]
print(unique_numbers(list2))