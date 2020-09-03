# Add up and print the sum of the all of the minimum elements of each inner array:
# [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# input of list of arrays
# iterate through each of the lists to find the minimum
# we want to find the sum of each of those minimums

def find_sum(arr):
    min_sum = 0
    for lis in arr:
        min_sum += min(lis)

    return min_sum

if __name__ == "__main__":
    arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
    print(find_sum(arr))