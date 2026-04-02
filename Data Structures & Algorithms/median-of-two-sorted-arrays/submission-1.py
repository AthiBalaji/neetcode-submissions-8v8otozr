def merge(a, b):
    len_a, len_b = len(a) - 1, len(b) - 1
    i = 0
    j = 0
    res = []
    while i <= len_a and j <= len_b:
        if a[i] <= b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[j])
            j+=1
    if j <= len_b:
        res.extend(b[j:])
    if i <= len_a:
        res.extend(a[i:])
    return res 
    
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = merge(nums1, nums2)
        n = len(result) 
        if n%2==0:
            median = (result[int(n/2 -1)] + result[int((n/2 +1)) - 1])/2
        else:
            median = result[int(n//2)] 
        return median
        