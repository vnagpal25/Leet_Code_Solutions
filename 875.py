class Solution:
    # def can_eat_the_bananas(self, piles, k, h):
    #     #return true if possible
    #     #false otherwise
    #     time = 0
    #     for pile in piles:
    #         #time needed to consume the pile: ceil(pile/k)
    #         #if we have 3 bananas and k = 2
    #         #in the first hour, we eat 2 bananas so 3 -2 = 1
    #         #it takes us another hour to eat the remaining banana
    #         # so for k = 2 and b = 3,t = 2
    #         time += math.ceil(pile/k)
    #         if time > h:
    #             return False
    #     return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the maximum value of the piles array
        # defines the fastest rate at which we can consume all the bananas
        # [30,11,23,4,20] if k = 30, then we can eat all the bananas in 5 hours
        # any value bigger than 30 results in the same time due to the constraints
        # 
        # max_val = max(piles)

        # k = 0 doesn't ever work so no point in including it
        # the minimum possible k to consume the bananas in h hours is
        # in the list [1, 2, 3 ... ,k ... ,max_val]
        l, r = 1, max(piles)
        to_ret_k = r

        # search until our pointers cross each other
        while l <= r:
            # compute the average
            k = (l + r)//2
            time = 0
            for pile in piles:
            #time needed to consume the pile: ceil(pile/k)
            #if we have 3 bananas and k = 2
            #in the first hour, we eat 2 bananas so 3 -2 = 1
            #it takes us another hour to eat the remaining banana
            # so for k = 2 and b = 3,t = 2
                time += math.ceil(pile/k)

            if time <= h:
                # we can eat the bananas at this rate
                # lets check if we can minimize this
                to_ret_k = min(k, to_ret_k)
                r = k - 1
            else:
                l = k + 1
        return to_ret_k

