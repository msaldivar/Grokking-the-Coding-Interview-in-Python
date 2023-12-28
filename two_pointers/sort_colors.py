
"""
0: red
1: white
2: blue
"""

def sort_colors(colors: list[int]):
    """Sort Colors"""
    left, right = 0, len(colors) - 1 
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


if __name__ == '__main__':
    main()