#Algorythm: Quicksort (sometimes called partition-exchange sort)
#Description: In this file we are using the Hoare partition scheme,
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
    pivot_value = array[min_index]
    i = min_index - 1
    j = max_index + 1

    while True:

        #Since Python doesn't have a 'do'...'while' loop,
        #we emulate it with something like this
        i = i + 1
        while array[i] < pivot_value:
            i = i +1

        j = j - 1
        while array[j] > pivot_value:
            j = j -1

        if i >= j:
            return j

        swapValues(array,i,j)

#Name: quicksort
#Description: The algorithm itself, basically it is the Python implementation
#of the Hoare partition scheme of Quicksort algorithm
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
        quicksort(array,min_index,p)
        quicksort(array,p+1,max_index)


#This is just for testing if everything works
arr=[2,7,3,1]
print("Unsorted array:")
print(arr)
quicksort(arr,0,len(arr)-1)
print("Sorted array:")
print(arr)
