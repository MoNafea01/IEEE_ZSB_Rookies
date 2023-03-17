# Import the functions from problem 1 to a different script and get user input and the 
# result in that script. Handle any possible error
from fl_stream import firstlast,sorter
input1= input("Enter The list separated: ").split()
lst=[]
for x in input1:
    lst.append(int(x))
target=int(input("Target: "))
print(sorter(lst))
print(firstlast(lst,target))