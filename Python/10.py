# Write a function to get the count of even numbers in list from the user. Handle any 
# possible error
# <= input  = [5,7,7,8,8,8,10] 
# => output = 4
def even_counter(list_A):
    counter=0
    try:
        for element in list_A:
            if (int(element)%2) == 0:
                counter=counter+1
        return counter
    except ValueError:
        print("Invalid input")