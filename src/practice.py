

# Number of 1 bits in a number 
def one_bits(x):
    x1 = x
    c = 0
    while(x!=0):
        x &= (x-1)
        c+=1
    
    print("Number of bits in ", x1, bin(x1), c)
    return c


def two_sums1(nums, target): 
    for x in nums: 
        if target - x in nums : 
            print (nums.index(x), nums.index(target-x))
            break

def two_sums(nums, target):
    """
    Return indices in nums such that nums[i] + nums[j] = target 
    """
    num_dict = {} 
    for i, n in enumerate(nums): 
        num_dict[n] = i
    for n in nums: 
        if target - n in num_dict: 
            print( num_dict[n], num_dict [target-n])
            break
    

    

import random
if __name__ == "__main__": 
    a = random.sample(range(1,20), 10)
    print(a)
    two_sums(a , 10)
    pass
    one_bits(100)
    c = 0
    for i in range(10):
        c += one_bits(i)


