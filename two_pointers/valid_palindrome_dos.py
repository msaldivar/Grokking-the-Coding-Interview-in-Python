





def is_palindrome(sentence: str):
    """"""

    left, right = 0, len(sentence) - 1

    
    while left <= right: 
        if sentence[left] != sentence[right]:
            removeLeft = sentence[left + 1:right + 1]
            removeRight = sentence[left:right]

            return ((removeLeft == removeLeft[::-1]) or 
                    (removeRight == removeRight[::-1]))

        left += 1
        right -= 1
    
    return True



def main():
    palindrome ="madame"
    print(f"is {palindrome} a palindrome? {is_palindrome(palindrome)}")

    palindrome = "dead"
    print(f"is {palindrome} a palindrome? {is_palindrome(palindrome)}")

    palindrome = "abca"
    print(f"is {palindrome} a palindrome? {is_palindrome(palindrome)}")

    palindrome = "tebbem"
    print(f"is {palindrome} a palindrome? {is_palindrome(palindrome)}")

    palindrome = "eeccccbebaeeabebccceea"
    print(f"is {palindrome} a palindrome? {is_palindrome(palindrome)}")





if __name__ == "__main__":
    main()