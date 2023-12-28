



from collections import defaultdict


def min_window(s, t):
    """"""
    # empty string
    if not t:
        return ""

    # two frequency maps
    req_count = defaultdict(lambda: 1)
    window_count = {}

    # populate req_count map with t values
    for character in t:
        if character in req_count:
            req_count[character] += 1
        else:
            req_count[character]

    # populate window dict
    for character in t:
        window_count[character] = 0

    # init tracking variables
    current = 0 
    required = len(req_count)

    # init results starting and ending point and result length
    res = [-1, -1]
    res_len = float("infinity")

    # setting sliding window pointers
    left = 0
    for right in range(len(s)):
        current_character = s[right]

        # if the current character is in t, update frequency in window
        if current_character in t:
            window_count[current_character] += 1

        # update current - how many chars in t have we seen
        if current_character in req_count and \
              window_count[current_character] == req_count[current_character]:
            current += 1

        # we found our first window and will adjust
        while current == required:
            # update result - res
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1

            # pop from left of our window
            # if s[left] is a char we are looking for we want to decrement freq in window
            if s[left] in t:
                window_count[s[left]] -= 1
            
            if s[left] in req_count and window_count[s[left]] < req_count[s[left]]:
                current -= 1
            
            # move window to the left
            left += 1
    
    left, right = res
    return s[left:right+1]

        


# driver Code
def main():
    s = ["PATTERN", "LIFE", "ABRACADABRA", "STRIKER", "DFFDFDFVD"]
    t = ["TN", "I", "ABC", "RK", "VDD"]
    for i in range(len(s)):
        print(i + 1, ".\ts: ", s[i], "\n\tt: ", t[i], "\n\tThe minimum substring containing ", \
              t[i], " is: ", min_window(s[i], t[i]), sep="")
        print("-" * 100)

if __name__ == '__main__':
    main()