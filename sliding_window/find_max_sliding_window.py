





def find_max_sliding_window(nums, window_size):

    max_seen = []

    for i in range(len(nums) - window_size + 1):
        window = nums[i : i + window_size]
        max_seen.append(max(window))

    return max_seen


def main():
    """"""

    nums = [1,2,3,4,5,6,7,8,9,10]
    window_size = 3
    print(f"Maximum values in window size: {find_max_sliding_window(nums, window_size)}")


    nums = [3,3,3,3,3,3,3,3,3,3]
    window_size = 4
    print(f"Maximum values in window size: {find_max_sliding_window(nums, window_size)}")

    nums = [10,6,9,-3,23,-1,34,56,67,-1,-4,-8,-2,9,10,34,67]
    window_size = 3
    print(f"Maximum values in window size: {find_max_sliding_window(nums, window_size)}")

    nums = [4,5,6,1,2,3]
    window_size = 1
    print(f"Maximum values in window size: {find_max_sliding_window(nums, window_size)}")





if __name__ == "__main__":
    main()