# Grokking - Merge Intervals Introduction

The merge intervals pattern deals with problems involving overlapping intervals. Each interval is represented by a start and an end time. For example, an interval of [10, 20] seconds means that the interval starts at 10 seconds and ends at 20 seconds, such that both 10 and 20 are included in the interval. 

The most common problems solved using this pattern are scheduling problems. 

The key to understanding this pattern and exploiting its power lies in understanding how any two intervals may overlap. The illustration below shows the six different ways in which two intervals can relate to each other:

## Does my problem match this pattern
Yes, if: 
* Input data is a list of intervals 
* The problem requires dealing with overlapping intervals either to find their intersection, their union, or the gaps between them. This may be required as the final goal or as an intermediate step in the computation of intervals. 

No, if:
* The order of the intervals in the result is not significant
* Input list of intervals is not sorted. 