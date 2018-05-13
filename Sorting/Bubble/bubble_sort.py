#Algorythm: Bubble Sort (also known as sinking sort)
#Description: This is a comparison sort. Meanwhile it is simple, it is too slow and impractical
#for most problems (even when compared to insertion sort).
#In this implementation, we are using the basic way to code the algorithm,
#we could do some optimizations to do this slow algorithm a little bit better
#but since this file is for educational purposes, I am just keep it simple.
#Source link: I saw the algorithm explanation on https://en.wikipedia.org/wiki/Bubble_sort
#Use: It is used to sort :P
#Developer: ¿?
#Mathematical analysis: It takes O(n^2) comparisons to sort n items, in worst cases it takes O(n^2)

#Name: swapValues
#Description: This function is used to swap the values of two indexs in an array
#Arguments: 3; array is the array where the values are,
#              x is an index to swap value
#              y is the other index to swap values
#Return: Nothing
#Example: swapValues(sampleArray,0,1)
def swapValues(listA,x,y):
    #I created this temporal var to avoid call len(array) several times
    len_arr=len(listA)

    #Tese conditions are done to avoid out of array exceptions
    if len_arr>0 and x<len_arr and x>=0 and y>=0 and y<len_arr and x!=y:
        #Just used this for debugging purposes
        #print("Swap "+str(array[x])+" and "+str(array[y]))
        temp_var=listA[y]
        listA[y]=listA[x]
        listA[x]=temp_var

#Name: bubbleSort
#Description: This function is the algorithm itself.
#Arguments: 1; listA is the list where the values to sort are
#Return: Nothing
#Example: bubbleSort(listToSort)
def bubbleSort(listA):
    lenListA = len(listA)

    # Since Python doesn't have a built-in do-while function
    # setting the swapped var true before starting the while
    # loop will let us to "emulate" it
    swapped = True

    while swapped == True:
        swapped = False
        for i in range(1,lenListA): # This for loop has to go from 1 to n-1 (inclusive) since last element in Python ranges is exclusive, we do n and not n-1
            if listA[i-1] > listA[i]:
                swapValues(listA,i-1,i)
                swapped = True


#This is just for testing if everything works
arr=[2,7,3,1]
print("Unsorted array:")
print(arr)
bubbleSort(arr)
print("Sorted array:")
print(arr)
