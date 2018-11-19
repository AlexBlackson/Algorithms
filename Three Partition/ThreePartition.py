"""
Created on Tue May 15 19:52:47 2018
Written by Alex Blackson
ENSEA: FAME Algorithms Course
Last Updated: May 17, 2018
"""

# Memoization function given in class to prevent repeat function calls
def memoize(f):
    mem={}
    def f_memoized(*args):
        if args not in mem:
            mem[args] = f(*args)
        return mem[args]
    
    return f_memoized

def threePartition(nums):
    s = sum(nums)
    # Checks if there are at least 3 elements and the sum of the elements are divisible by 3
    if s % 3 != 0 or len(nums) < 3:
        return False
    
    # x, y, and z are the three bins for the subsets to fit in
    @memoize
    def checkSubset(curr, x, y, z):
        # Base case: all bins perfectly full - equal subsets
        if (x == 0 and y == 0 and z == 0):
            return True
        
        # Base case: all the values of the array have been checked
        if (curr < 0):
            return False
        
        # Finds first bin that current value (nums[curr]) fits in and recurses
        xFit = False
        yFit = False
        zFit = False
        
        if (x - nums[curr] >= 0):
            xFit = checkSubset(curr - 1, x - nums[curr], y, z)
    
        if (not xFit and y - nums[curr] >= 0):
            yFit = checkSubset(curr - 1, x, y - nums[curr], z)
        
        if ((not xFit) and (not yFit) and (z - nums[curr] >= 0)):
            zFit = checkSubset(curr - 1, x, y, z - nums[curr])
         
        # Will return true if current value was able to fit in array 
        return xFit or yFit or zFit
    
    return checkSubset(len(nums) - 1, s//3, s//3, s//3)