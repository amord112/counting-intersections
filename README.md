# count-intersections

###Problem
This python code provides two methods of a solution to counting the number of intersections of chords inside a circle, given a list of radians and corresponding endpoint identifiers.

Notes: we are given a list of ascending radians, and told that no intersections occur at the same point, so their values do not matter in the context of the problem. Additionally, s_i and e_i refer to endpoints of the same chord so we use a single label for both.

#Solution approaches
The first mehod solves the question by numbering and listing the endpoints in the order they occur (from 1 to n) and counting the number of inversions inv_total while sorting the list using the MergeSort algorithm. To avoid overcounting intersections of chords that lie within one another, it creates a list of finishing endpoints and counts the number of inversions inv_ends using the same algorithm as above. The total number of intersections is calculated as inv_total - 2*inv_ends. This method has a big-O runtime of O(NlogN), dominated by the MergeSort algorithm. 

The second method iterates through the endpoints x_i in the order they occur and adds them to a list. Once and endpoint x_k is reached that already exists in the list, we have completed the chord. The number of chords intersecting it is counted by the number of endpoints (incomplete chords) existing after x_k in the list, and the endpoint x_i is deleted from the list. This method has a big-O runtime of O(N^2) as a result of the .pop() method existing inside the loop. The efficiency can be improved by implementing a binary (eg AVL) tree to store, count and update the endpoints, resulting in a comparable runtime of O(NlogN). 

#Usage 
