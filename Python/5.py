# Find the minimum distance between the same numbers in a list
# <= input  = [2, 5, 3, 4, 5 , 2]        
# <= target = 2
# => output = 5
# <= input  = [2, 5, 3, 4, 5 , 2] 
# <= target = 5
# => output = 3
x,num = [2, 5, 3, 4, 5 , 2],5
print(x[x.index(num)+1:].index(num)+1)