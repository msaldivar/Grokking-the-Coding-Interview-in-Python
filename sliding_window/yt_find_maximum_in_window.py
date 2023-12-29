"""
Repeated DNA Sequences - LeetCode 239

Grokking Life

Solution Summary:
* We create a list to hold all the max values we see in our window - max_seen
* Error check to see if the window size requested is >= than the list len
* loop through the list with range being (len(nums) - window_size + 1) aka (n - k + 1)
* using python list slicing to grab our window 
* w/ the window now created use max() to find the window max value
* append to the list and return once the loop finishes

"""

def find_max_sliding_window(nums: list[int], window_size: int):
    """LeetCode 239"""
    max_seen = []

    if window_size >= len(nums):
        max_seen.append(max(nums))
        return max_seen

    for i in range(len(nums) - window_size + 1):
        window = nums[i: i + window_size]
        max_seen.append(max(window))

    return max_seen

def main():
    nums = [1,3,-1,-3,5,3,6,7]
    window_size = 3
    print(f"\nInput: {nums} window size: {window_size}")
    print(f"Maximums: {find_max_sliding_window(nums, window_size)}\n\n")

    nums = [1]
    window_size = 1
    print(f"\nInput: {nums} window size: {window_size}")
    print(f"Maximums: {find_max_sliding_window(nums, window_size)}\n\n")

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    window_size = 3
    print(f"\nInput: {nums} window size: {window_size}")
    print(f"Maximums: {find_max_sliding_window(nums, window_size)}\n\n")

    nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    window_size = 3
    print(f"\nInput: {nums} window size: {window_size}")
    print(f"Maximums: {find_max_sliding_window(nums, window_size)}\n\n")

    nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    window_size = 3
    print(f"\nInput: {nums} window size: {window_size}")
    print(f"Maximums: {find_max_sliding_window(nums, window_size)}\n\n")

    nums = [1, 5, 8, 10, 10, 10, 12, 14, 15, 19, 19, 19, 17, 14, 13, 12, 12, 12, 14, 18, 22, 26, 26, 26, 28, 29, 30]
    window_size = 3
    print(f"\nInput: {nums} window size: {window_size}")
    print(f"Maximums: {find_max_sliding_window(nums, window_size)}\n\n")

    nums = [10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67]
    window_size = 2
    print(f"\nInput: {nums} window size: {window_size}")
    print(f"Maximums: {find_max_sliding_window(nums, window_size)}\n\n")

    nums = [4, 5, 6, 1, 2, 3]
    window_size = 4
    print(f"\nInput: {nums} window size: {window_size}")
    print(f"Maximums: {find_max_sliding_window(nums, window_size)}\n\n")

    nums = [9, 5, 3, 1, 6, 3]
    window_size = 3
    print(f"\nInput: {nums} window size: {window_size}")
    print(f"Maximums: {find_max_sliding_window(nums, window_size)}\n\n")

    nums = [2, 4, 6, 8, 10, 12, 14, 16]
    window_size = 2
    print(f"\nInput: {nums} window size: {window_size}")
    print(f"Maximums: {find_max_sliding_window(nums, window_size)}\n\n")

    nums = [-1, -1, -2, -4, -6, -7]
    window_size = 3
    print(f"\nInput: {nums} window size: {window_size}")
    print(f"Maximums: {find_max_sliding_window(nums, window_size)}\n\n")

    nums = [4, 4, 4, 4, 4, 4]
    window_size = 18
    print(f"\nInput: {nums} window size: {window_size}")
    print(f"Maximums: {find_max_sliding_window(nums, window_size)}\n\n")

if __name__ == "__main__":
    main()