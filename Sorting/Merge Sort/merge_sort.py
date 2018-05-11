#Algorythm: Merge Sort
#Description: This is a binary merge sort since we are always dividing
#the unordered list into two lists. We could do a merge sort algorithm of
#higher order just dividing the unordered list into N lists of approximately
#equal size, sort them and merge the N ordered lists.
#Source link: I saw the algorithm explanation on https://en.wikipedia.org/wiki/Merge_sort
#Use: It is used to sort, it is a divided and conquer algorithm.
#Developer: John von Neumann
#Mathematical analysis: It takes O(n log n) comparisons to sort n items, in worst cases it takes O(n) with O(n) auxiliary

#Name: mergeLists
#Description: This function is used to merge two lists
#Arguments: 2; listA with one list
#              listB with the other list
#Return: A sorted list result of merging the two lists passed as args
#Example: sortedList = mergeLists(myList1,myList2)
def mergeLists(listA,listB):

    # This is just to check we always return something correct
    lenListA = len(listA)
    lenListB = len(listB)

    if lenListA == 0 and lenListB == 0:
        return 0 # This is just if both lists are empty (why should this happen?)
    elif lenListA == 0 or lenListB == 0:
            if lenListA == 0:
                return listB # If listA is empty, these 'two' lists are already 'merged'
            else:
                return listA # The same happens if listB is empty and listA is not

    # Now we just take the smaller one of the two head elements,
    # and merge the remaining lists recursively (so recursively it acts
    # as we were sorting two 1-item lists)
    if listA[0] <= listB[0]:
        return listA[0:1] + mergeLists(listA[1:],listB)
    else:
        return listB[0:1] + mergeLists(listA,listB[1:])

#Name: mergeSort
#Description: This function is the main function of the merge sort algorithm
#Arguments: 1; listA with one list to sort
#Return: A sorted list
#Example: sortedList = mergeSort(myList1)
def mergeSort(listA):
    # If it is a list with 0 or 1 elements, it is already sorted!
    if len(listA) <= 1:
        return listA

    # Basically this splits the listA in half, sort the halves
    # and return a sorted list result of mergin those halves
    m = len(listA) // 2 # '//' is an integer division
    return mergeLists(mergeSort(listA[0:m]),mergeSort(listA[m:]))


#This is just for testing if everything works
arr=[2,7,3,1]
print("Unsorted array:")
print(arr)
arr = mergeSort(arr)
print("Sorted array:")
print(arr)
