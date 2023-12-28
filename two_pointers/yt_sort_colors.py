"""
Sort Colors - LeetCode 75

Grokking Life

Solution Summary:
0 = red = left
1 = white = i
2 = blue = right

* We'll take advantage of three pointers: left, right, and i to be used as the loop variable
* If the element pointed to by i (white) is 0, we swap it with the element pointed to by the left (red)
  pointer if it's not pointer to 0, and increment both the left (red), and i (white) pointers
* If the element pointed to by i (white) is 1, we increment i (white)
* If the element pointed to by i (white) is 2, we swap it with the element pointed to by the right (blue)
  pointer, if it's not pointint to 2, and decrement the right (blue) pointer
* The array is sorted when the right (blue) pointer becomes less than i (white) pointer
"""

def sort_colors(colors: list[int]) -> list[int]:
    """LeetCode 75"""
    left = 0
    right = len(colors) - 1
    i = 0

    while i <= right:
        if colors[i] == 0:
            colors[left], colors[i] = colors[i], colors[left]
            left += 1
            i += 1
        elif colors[i] == 2:
            colors[right], colors[i] = colors[i], colors[right]
            right -= 1
        else:
            i += 1

    return colors

def main():
    input = [2,0,2,1,1,0]
    print(f"input {input}: after sorting: {sort_colors(input)}")

    input = [2,0,1]
    print(f"input {input}: after sorting: {sort_colors(input)}")

    input = [0,1,0]
    print(f"input {input}: after sorting: {sort_colors(input)}")

    input = [1]
    print(f"input {input}: after sorting: {sort_colors(input)}")

    input = [2,2]
    print(f"input {input}: after sorting: {sort_colors(input)}")

    input = [1,1,0,2]
    print(f"input {input}: after sorting: {sort_colors(input)}")

    input = [2,1,1,0,0]
    print(f"input {input}: after sorting: {sort_colors(input)}")

if __name__ == "__main__":
    main()