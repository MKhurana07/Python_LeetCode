def findMedianSortedArrays(nums1, nums2):
    len1 = len(nums1)
    len2 = len(nums2)
    merged = []
    i= 0
    k = 0
    j= 0
    while i<len1 and k<len2:
        if (nums1[i] < nums2[k]):
            merged.append(nums1[i])
            i = i+1
        else:
            merged.append(nums2[k])
            k = k+1
        
    if i>len1-1:
        
        while k<len2:
            merged.append(nums2[k])
            k=k+1
            
    else:
        while i<len1:
            merged.append(nums1[i])
            i=i+1
            
    median_index = int(len(merged)/2)
    if len(merged)%2 == 0:
        median = (merged[median_index] + merged[median_index-1])/2
    else:
        median = merged[median_index]
    print(median)
    print(merged)

findMedianSortedArrays([1,2,5],[3,4])
