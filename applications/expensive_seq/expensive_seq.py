# Your code here
from hashtable import HashTable

def expensive_seq(x, y, z, exp_dict={}):
    # Your code here

    if x <= 0:  # check if x is 0 or under
        return y + z  # return sum of y and z
    
    else:

        if (x, y, z) not in exp_dict:  # check if tuple (x, y, z) is in the exp_dict
            #  if not, add the tuple to the dict with the value of the function's recursion with decreasing x, increasing y, and multiplicatively increasing z
            exp_dict[(x, y, z)] = expensive_seq(x-1,y+1,z, exp_dict) + expensive_seq(x-2,y+2,z*2, exp_dict) + expensive_seq(x-3,y+3,z*3, exp_dict)
            
        return exp_dict[(x, y, z)]  # return exp_dict at position of tuple (x, y, z)
        


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    # print(expensive_seq(150, 400, 800))

"""
exps(x, y, z) =
     if x <= 0: y + z
     if x >  0: exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)

x = 150
y = 400
z = 800
"""