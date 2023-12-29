# Grokking - Sliding Window Introduction

The Sliding Window Pattern is used to process sequential data by maintaining a moving range of elements, the window. 
The pattern is aimed at reducing the use of nested loops in an algorithm. 

The window is a sub-list formed over a part of an iterable data structure. It can be used to slide over the data in chunks corresponding to the window size. The window allows us to process the data in segments instead of the entire list. The segment or window size can be set according to the problems's requirements. An example, if we have to find three consecutive integers with the largest sum in an array, we can set the window size to 3. This allows us to process the data three elements at a time. Biggest thing to remember `n - k + 1` 

## Does my problem match this pattern? 

Yes, if:
* The problem requires repeated computations on a contiguous set of data elements (a sublist or a substring), such that the window moves across the input list from one end to the other. The size of the window may be fixed or variable, depending on the requirements of the problem. The repeated computations may be a direct part of the final solution or they may be intermediate steps building up towards the final solution 
* The computations performed every time the window moves take `O(1)` time or are a slow-growing function, such as log

No, if:
* The input data structure does NOT support random access
* You have to process the entire data without segmentation, a window can not be created 