def longest_slide_down(pyramid, level=-1):
    if level == -1: level = len(pyramid) - 1
    if level == 0: return pyramid[0][0]

    for i in range(len(pyramid[level]) - 1):
        pyramid[level-1][i] += max(pyramid[level][i], pyramid[level][i + 1])

    return longest_slide_down(pyramid, level-1)

print(longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]))