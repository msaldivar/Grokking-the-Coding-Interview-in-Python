"""
Valid Palindrome - LeetCode 135

Grokking Life


"""

def is_this_a_pal(pal: str) -> bool:
    """Two Pointer Approach"""

    left_index = 0
    right_index = len(pal) - 1

    while left_index <= right_index:

        if pal[left_index] != pal[right_index]:
            return False
        left_index += 1
        right_index -= 1

    return True


def is_this_pal_pythonic(pal: str) -> bool:

    return pal == pal[::-1]


    



def main():
    """Is this a Pal"""
    palindrome = "kayak"
    print(f"is {palindrome} a palindrome? {is_this_pal_pythonic(pal=palindrome)}")

    palindrome = "hello"
    print(f"is {palindrome} a palindrome? {is_this_pal_pythonic(pal=palindrome)}")

    palindrome = "RACEACAR"
    print(f"is {palindrome} a palindrome? {is_this_pal_pythonic(pal=palindrome)}")

    palindrome = "A"
    print(f"is {palindrome} a palindrome? {is_this_pal_pythonic(pal=palindrome)}")

    palindrome = "ABCDABCD"
    print(f"is {palindrome} a palindrome? {is_this_pal_pythonic(pal=palindrome)}")



if __name__ == "__main__":
    main()