# All The Algorithms On Python
So yeah, just for educational purposes, I am trying to create by myself all the algorithms I can find (just reading their papers, without seeing the code). Since these are for demonstration purposes only, I advice to don't use them. There are many implementations of sorts in the Python standard library that are much better for performance reasons.

## Sort Algorithms
### Quicksort
![Quicksort animated example](https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif)

From [Wikipedia](https://en.wikipedia.org/wiki/Quicksort): Quicksort (sometimes called partition-exchange sort) is an efficient sorting algorithm, serving as a systematic method for placing the elements of an array in order.

**Properties:**
* Worst case performance	O(n^2)
* Best case performance	O(n log n) or O(n) with three-way partition
* Average case performance	O(n log n)

###### View it in action [here](https://www.toptal.com/developers/sorting-algorithms/quick-sort)

There are several partition schemes, currently I have implemented these ones:
* [Lomuto partition scheme](https://github.com/NautaDev/AllTheAlgorithmsOnPython/blob/master/Sorting/Quicksort/quicksort_lomuto_partition_scheme.py)
* [Hoare partition scheme](https://github.com/NautaDev/AllTheAlgorithmsOnPython/blob/master/Sorting/Quicksort/quicksort_hoare_partition_scheme.py)

### Merge Sort
![Merge Sort animated example](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)

From [Wikipedia](https://en.wikipedia.org/wiki/Merge_sort): In computer science, merge sort (also commonly spelled mergesort) is an efficient, general-purpose, comparison-based sorting algorithm. Most implementations produce a stable sort, which means that the implementation preserves the input order of equal elements in the sorted output. Mergesort is a divide and conquer algorithm that was invented by John von Neumann in 1945.

**Properties**
* Worst case performance	O(n log n)
* Best case performance	O(n)
* Average case performance	O(n)

###### View it in action [here](https://www.toptal.com/developers/sorting-algorithms/merge-sort)

There are several implementations, currently I have implemented these ones:
* [Binary Merge Sort](https://github.com/NautaDev/AllTheAlgorithmsOnPython/blob/master/Sorting/Merge%20Sort/merge_sort.py)

## Special Thanks
First, I want to say thank you to [The Algorithms](https://github.com/TheAlgorithms), because exploring GitHub, I found their repo, where they were doing something similar to this repo (you can check their repo [here](https://github.com/TheAlgorithms/Python).

Also, I want to thank you to TopCoders, since I am providing the animations of the algorithms from their website.

And finally (but not less important), to all the informative websites where I am reading about those algorithms:
* **Wikipedia**
