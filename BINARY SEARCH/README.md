# Binary-search


The binary search works on one condition that the array provided to it must be sorted. This is also a disadvantage of binary searchthat is the array is not sorted then it will not work.
Explanation of the Binary Search Algorithm:
1. **Initialization**: 
   - Set `left` to 0 (the index of the first element in the array) and `right` to `len(array) - 1` (the index of the last element in the array).
   
2. **Search Loop**:
   - While `left` is less than or equal to `right`, continue the search.
   
3. **Middle Index Calculation**:
   - Calculate the middle index of the array using `(left + right) // 2`. This index represents the midpoint of the current search interval.
   
4. **Comparison with the Key**:
   - If the element at the middle index is equal to the key, return the index of the middle element.
   - If the element at the middle index is greater than the key, update `right` to `mid - 1` to search in the left half of the array.
   - If the element at the middle index is less than the key, update `left` to `mid + 1` to search in the right half of the array.
   
5. **Repeat**:
   - Repeat steps 3 and 4 until either the key is found or `left` exceeds `right`, indicating that the key is not present in the array.

This binary search algorithm efficiently finds the position of the key in the sorted array or determines that the key is not present.


