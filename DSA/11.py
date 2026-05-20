class Solution(object):
    def maxArea(self, height):
         res = 0
        
         l = 0
         r = len(height) - 1
         #if l< r, area = width * height, store max in res
         while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            
            #height l< r, l+=1, if l=r or l > r r-=1
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
         return res
