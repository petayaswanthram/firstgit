def min_edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],
                                  dp[i][j - 1],
                                  dp[i - 1][j - 1])

    return dp[m][n]
str1_example = "see"
str2_example = "saw"
output_example = min_edit_distance(str1_example, str2_example)
print("Output:", output_example)

str1_example = "sunday"
str2_example = "saturday"
output_example = min_edit_distance(str1_example, str2_example)
print("Output:", output_example)
