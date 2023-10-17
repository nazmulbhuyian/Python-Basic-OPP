# Given a balanced string S
#  consists of ['R', 'L'] characters. Split it into maximum number of strings such that the new strings are also balanced.

# Note:

# Balanced strings are those who have equal quantities of 'L' and 'R' characters.
# You can not remove or reorder the characters while making the new strings.
# Input
# Only one line contains a string S
#  (2≤|S|≤1000)
#  where |S| is the length of the string.

# It's guaranteed that S
#  consists of only ['L', 'R'] letters, S
#  is balanced and |S|
#  is even.

# Output
# Print maximum number of balanced strings then the balanced strings in any order.

# Examples
# inputCopy
# LLRRLLLRRR
# outputCopy
# 2
# LLRR
# LLLRRR
# inputCopy
# LLLRRR
# outputCopy
# 1
# LLLRRR






# s = input()

# count = 0 
# result = []
# current = s[0]

# for i in range(1, len(s)):
#     current += s[i]
#     if current.count('L') == current.count('R'):
#         count += 1
#         result.append(current)
#         current = ''


# print(count)
# for s in result:
#     print(s)







s = input()

count_L = 0
count_R = 0

result = []

for char in s:
    if char == 'L':
        count_L += 1
    else:
        count_R += 1
    
    if count_L == count_R:
        result.append(s[:count_L + count_R])
        s = s[count_L + count_R:]
        count_L = 0
        count_R = 0

print(len(result))

for balanced_str in result:
    print(balanced_str)
