
def is_palindrome(pal: str) -> bool:

    left = 0
    right = len(pal) - 1

    while left < right:
        if pal[left] != pal[right]:
            return False
        
        left += 1
        right -= 1
    
    return True

def is_pal_pythonic(pal: str) -> bool:
    """Pythonic solution"""

    return pal == pal[::-1]

def main():
    palindrome = "kayak"
    print(f"is {palindrome} a palindrome? {is_pal_pythonic(pal=palindrome)}")

    palindrome = "hello"
    print(f"is {palindrome} a palindrome? {is_pal_pythonic(pal=palindrome)}")

    palindrome = "RACEACAR"
    print(f"is {palindrome} a palindrome? {is_pal_pythonic(pal=palindrome)}")

    palindrome = "A"
    print(f"is {palindrome} a palindrome? {is_pal_pythonic(pal=palindrome)}")

    palindrome = "ABCDABCD"
    print(f"is {palindrome} a palindrome? {is_pal_pythonic(pal=palindrome)}")

main()