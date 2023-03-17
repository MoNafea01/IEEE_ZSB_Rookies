# Write a program to find the second largest and second smallest number in a list. [ Do 
# not use any built-in functions]
lst_old=input("enter a list separated by space: ").split()
lst=[]
while lst_old:
    minimum=lst_old[0]
    for x in lst_old:
        if x<minimum:
            minimum = x
    lst.append(minimum)
    lst_old.remove(minimum)
print(lst)
print("Second max number is: ",lst[len(lst)-2] , "and second min number is: ",lst[1])