#Algorythm: Quicksort (sometimes called partition-exchange sort)
#Description: In this file we are using the Lomuto partition scheme,
#you can seen other implementation in the other quicksort files
#Source link: I saw the algorithm explanation on https://en.wikipedia.org/wiki/Quicksort
#Use: It is used to sort, it is a comparison sort
#Developer: Tony Hoare
#Mathematical analysis: It takes O(n log n) comparisons to sort n items, in worst cases it takes O(n^2)

#Name: swapValues
#Description: This function is used to swap the values of two indexs in an array
#Arguments: 3; array is the array where the values are,
#              x is an index to swap value
#              y is the other index to swap values
#Return: Nothing
#Example: swapValues(sampleArray,0,1)
def swapValues(array,x,y):
    #I created this temporal var to avoid call len(array) several times
    len_arr=len(array)

    #Tese conditions are done to avoid out of array exceptions
    if len_arr>0 and x<len_arr and x>=0 and y>=0 and y<len_arr and x!=y:
        #Just used this for debugging purposes
        #print("Swap "+str(array[x])+" and "+str(array[y]))
        temp_var=array[y]
        array[y]=array[x]
        array[x]=temp_var

#Name: partition
#Description: Used to create a partition and order it, swapping values
#Arguments: 3; array is the array where the values are,
#              min_index is the minimum index of the partition
#              max_index is the maximum index of the partition
#Return: 1, an integer which is an index
#Example: ret_value = partition(sampleArray,0,20)
def partition(array,min_index,max_index):
    pivot_value = array[max_index]
    i = min_index - 1
    #A little note, in the Wikipedia site says this for loop should be
    #something like: 'for j in range(min_index,max_index-1)'
    #but take care of something, range() on Python doesn't include
    #the maximum element in the range, it means, we are doing
    #in reality: 'for j in range(min_index,max_index-2)
    #So I had to change it to 'for j in range(min_index,max_index)'
    #to include the max_index-1 value in the for loop
    for j in range(min_index,max_index):
        if array[j] <= pivot_value:
            i = i+1
            swapValues(array,i,j)
    swapValues(array,i+1,max_index)
    return i+1

#Name: quicksort
#Description: THe algorithm itself, basically it is the Python implementation
#of the Lomuto partition scheme of Quicksort algorithm
#Arguments: 3; array is the array where the values are,
#              min_index is the minimum index of the array (or the min
#              index we want to sort)
#              max_index is the maximum index of the array (or the max
#              index we want to sort)
#Return: Nothing
#Example: quicksort(sampleArray,0,len(sampleArray)-1) (it will sort the entire
#sampleArray
def quicksort(array,min_index,max_index):
    if min_index < max_index:
        p=partition(array,min_index,max_index)
        quicksort(array,min_index,p-1)
        quicksort(array,p+1,max_index)


#This is just for testing if everything works
arr=[2,7,3,1]
print("Unsorted array:")
print(arr)
quicksort(arr,0,len(arr)-1)
print("Sorted array:")
print(arr)
