
def solution(a, k):
    """
    Idea is to use binary search
    If we can make k ribbons from length x, 
    we can definitely make k ribbons from length x - 1
    
    So, we can save some work by not having to check all of the possible values
    
    If we use binary search we can solve the problem in O(nlog(n)) time instead of O(n^2)

    The largest possible value that can yeild a single ribbon is max(a)
    
    The smallest possible value that can yeild a ribbon is 0 (not cutting them at all)


    """
    
    left, right = 0, max(a)
    
    # continue while left is smaller than right, not equal to
    # this might cause division by 0
    while left < right:
        # our guess is (left + right) / 2
        mid = (left + right + 1) >> 1 # same as integer division by 2, bit shift
        
        # count all the ribbons that we can make
        cnt = sum(x // mid for x in a)
        
        if cnt >= k: # we can create k ribbons from this length
            # let's see if we can make k ribbons from a larger length
            left = mid
        else: # we can't make k ribbons from this length
            right = mid - 1 # let's cut shorter pieces and see when we can reach k
    
    return left
    

## O(n^2) solution 2 
# # def solution(a, k):
# #     m = max(a)
    
# #     for i in range(m, 0, -1):
# #         total_ribbons = 0
# #         for num in a:
# #             total_ribbons += (num // i)
# #             if total_ribbons >= k:
# #                 return i        
        
## O(n^2) solution 1 
# # def solution(a, k):
# #     i = 1
# #     while True:
        
# #         total_ribbons = 0
        
# #         for num in a:
# #             total_ribbons += (num // i)
        

# #         if total_ribbons  < k:
# #             return i - 1
        
# #         i += 1
