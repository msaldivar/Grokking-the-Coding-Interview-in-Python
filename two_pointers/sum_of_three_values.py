

def find_sume_of_three(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    triplets = []

    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1
        cur_value = nums[i]

        while left < right:
            temp_total = cur_value + nums[left] + nums[right]
            if temp_total > target:
                right -= 1
            elif temp_total < target:
                left += 1
            elif temp_total == target:
                if [cur_value, nums[left], nums[right]] not in triplets:
                    triplets.append([cur_value, nums[left], nums[right]])
                left += 1
                right -= 1
            
    return triplets



def main():
    nums = [1,-1,0]
    target = -1
    find_sume_of_three(nums, target)

    nums = [-1,0,1,2,-1,-4]
    target = 0
    print(f"triplet for {nums} target: {target} {find_sume_of_three(nums, target)}")


    nums = [-1,0,1,2,-1,-4]
    target = 0
    print(f"list {nums} target {target}: {find_sume_of_three(nums, target)}")

    nums = [0,1,1]
    target = 0
    print(f"list {nums} target {target}: {find_sume_of_three(nums, target)}")

    nums = [0,0,0]
    target = 0
    print(f"list {nums} target {target}: {find_sume_of_three(nums, target)}")
 

    # nums = [3,7,1,2,8,4,5]
    # target = 10
    # find_sume_of_three(nums, target)

    # nums = [3,7,1,2,8,4,5]
    # target = 21
    # find_sume_of_three(nums, target)

    # nums = [-1,2,1,-4,5,-3]
    # target = -8
    # find_sume_of_three(nums, target)


    # nums = [-1,2,1,-4,5,-3]
    # target = 0
    # find_sume_of_three(nums, target)

if __name__ == '__main__':
    main()