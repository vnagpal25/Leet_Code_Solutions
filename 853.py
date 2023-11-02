class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        time_to_dest = [] # holds the time each car will take to reach its destination
        
        # zip and sort the list so that we can go through the cars in a specific order
        # and also have their corresponding speeds
        pos_speed = zip(position, speed)
        pos_speed = sorted(pos_speed, key=lambda x : x[0])

        # iterate over backwards
        # basically the logic here is that we want to compute the time to destination for each car
        # on the first iteration, we simply append it to the stack
        # on subsequent iterations, we compare the time_to_dest for the current car to the last car's time appended on the stack
        # if it takes the same amount of time or shorter, that means that the car is faster and will overtake the car at/before the destination
        # if this is the case, we won't append it to the stack, because they'll be considered the same car fleet
        # if the time taken is longer, then that means that it will never overtake the car before/at the target, and should be considered a seperate car fleet
        # then it should be append to the stack
        # iterating over the sorted list and using a stack ensures that we are not missing anything 
        for pos, v in pos_speed[::-1]:
            time = (target - pos) / v
            
            if time_to_dest and time <= time_to_dest[-1]:
                continue
            time_to_dest.append(time)    

        # now
        return len(time_to_dest)
