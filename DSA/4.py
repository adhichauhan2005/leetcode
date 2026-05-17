class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged = []

        i = 0
        j = 0
        #Ascending sort
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        #If 1 array finishes first copy the elements of second into merged array
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

       #Median
        total = len(merged)
        
        if total % 2 == 1:
            return merged[total // 2]
        else:
            mid1 = merged[(total // 2) - 1]
            mid2 = merged[total // 2]

            return (mid1 + mid2) / 2
