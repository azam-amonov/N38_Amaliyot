strs = ["fyl", "fyl", "fyl"]
def longestPref(strs):
    prefix = ''

    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != char:
                return prefix
        prefix += char
    return prefix

var = longestPref(strs)
print(var)
