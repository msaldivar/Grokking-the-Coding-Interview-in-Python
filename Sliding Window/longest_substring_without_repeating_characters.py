def sum_nums_in_str(input_str):
    """Given an alphanumeric string, find the numbers embedded in the string and return their sum.

    "a1b12c123d1234e" -> 1 + 12 + 123 + 1234 = 1370
    """
    answer = []
    sum_str = ""
    for char in input_str:
        if char.isdigit():
            sum_str += char
        else:
            if sum_str:
                answer.append(int(sum_str))
            sum_str = ""

    return sum(answer)

def twoSum(nums: list[int], target: int) -> list[int]:
    numMap = {}

    for i in range(len(nums)):
        num = nums[i]
        complement = target - num

        if complement in numMap:
            return [numMap[complement], i]
        
        numMap[num] = i

    return []  # No solution found

def find_longest_substring(input_str):
    seen = {}
    length = 0
    start = 0
    left = 0

    for right in range(len(input_str)):
        char = input_str[right]
        
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        else:
            length = max(length, right - left + 1)
            start = left

        seen[char] = right
    return [length,input_str[start:start + length]]


def find_char_freq(input_str):
    """Return list of character which had the greatest frequency in the string
    
    "abbcccddddeeeefffggh" -> ["d", "e"]
    """
    freq = {}
    for char in input_str:
        freq[char] = freq.get(char, 0) + 1

    max_freq = max(freq.values())

    answer = [k for k,v in freq.items() if v == max_freq] 

    return answer

# Driver code
def main():
    # print('FIND LONGEST SUBSTRING')
    # string = [
    #     "abcabcbb",
    #     "pwwkew",
    #     "bbbbb",
    #     "ababababa",
    #     "",
    #     "ABCDEFGHI",
    #     "ABCDEDCBA",
    #     "AAAABBBBCCCCDDDD",
    # ]
    # for i in range(len(string)):
    #     print(i + 1, ". \t Input String: ", string[i], sep="")
    #     print("\t Length of longest substring: ",
    #             (find_longest_substring(string[i])))
    #     print("-" * 100)

    # print('FIND CHAR FREQ')
    # char_freq_str = "abbcccddddeeeefffggh" 
    # print(f'Input str: {char_freq_str} -> {find_char_freq(char_freq_str)}')


    print('FIND SUM IN STR')
    sum_num_str = "a1b12c123d1234e" 
    print(f"Input str: {sum_num_str} -> {sum_nums_in_str(sum_num_str)}")






if __name__ == "__main__":
    main()
    