"""
3Sum - LeetCode 15

Grokking Life

Solution Summary:
First, sort the array in ascending order. To find a triplet whose sum is equal to the target value, loop through the entire array. Each iteration:
  * Store the current array element and set up two pointers, low and high, to find the other two elements that complete the triplet:
    * The low pointer is set to the current loops index + 1
    * The high is set to the last index of the array
  * Calculate the sum of array elements pointed to by the current loops index i and the low and high pointers
  * If the sum is less than to target, move the low pointer forward 
  * If the sum is greater than target, move the high pointer backward
  * If the sum is equal to the target, check if it's a duplicate then add to triplet list


    nums = [-1,0,1,2,-1,-4]
    target = 0

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

    Input: nums = [0,1,1]
    Output: []

    Input: nums = [0,0,0]
    Output: [[0,0,0]]
"""

def sum_of_three_solution(nums: list[int]) -> list[list[int]]:
    """Two Pointer Solution"""

    nums.sort()
    triplets = []
    target = 0

    for i in range(len(nums)):
        current_value = nums[i]
        low = i + 1
        high = len(nums) - 1

        while low < high:
            temp_total = current_value + nums[low] + nums[high]

            if temp_total < target:
                low += 1
            elif temp_total > target:
                high -= 1
            elif temp_total == target:
                if [current_value, nums[low], nums[high]] not in triplets:
                    triplets.append([current_value, nums[low], nums[high]])
                
                low += 1
                high -= 1

    return triplets

def main():
    """Run Sum of Three"""

    nums = [-1,0,1,2,-1,-4]
    target = 0
    print(f"list {nums} target {target}: {sum_of_three_solution(nums)}")

    nums = [0,1,1]
    target = 0
    print(f"list {nums} target {target}: {sum_of_three_solution(nums)}")

    nums = [0,0,0]
    target = 0
    print(f"list {nums} target {target}: {sum_of_three_solution(nums)}")
 
    nums = [1,-1,0]
    target = -1
    print(f"list {nums} target {target}: {sum_of_three_solution(nums, target)}") 

    nums = [3,7,1,2,8,4,5]
    target = 10
    print(f"list {nums} target {target}: {sum_of_three_solution(nums, target)}") 

    nums = [3,7,1,2,8,4,5]
    target = 21
    print(f"list {nums} target {target}: {sum_of_three_solution(nums, target)}") 

    nums = [-1,2,1,-4,5,-3]
    target = -8
    print(f"list {nums} target {target}: {sum_of_three_solution(nums, target)}") 

    nums = [-1,2,1,-4,5,-3]
    target = 0
    print(f"list {nums} target {target}: {sum_of_three_solution(nums, target)}") 

if __name__ == "__main__":
    main()