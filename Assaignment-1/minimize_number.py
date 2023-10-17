# Given a number N and an array A of N positive numbers. Print maximum possible operations that can be performed.

# The operation is as follows: if all numbers are even then divide each of them by 2 otherwise, you can not perform any more operations.

# Input
# First line contains a number N (1 ≤ N ≤ 200) number of elements.

# Second line contains N numbers (1  ≤  Ai  ≤  109).

# Output
# Print the maximum possible number of operations that can be performed.

# Examples
# inputCopy
# 3
# 8 12 40
# outputCopy
# 2
# inputCopy
# 4
# 5 6 8 10
# outputCopy
# 0
# Note
# First example:

# Initially, [8,12,40] are written on the blackboard. Since all those integers are even, You can perform the operation.

# After the operation is performed once, [4,6,20] are written on the blackboard. Since all those integers are again even, You can perform the operation.

# After the operation is performed twice, [2,3,10] are written on the blackboard. Now, there is an odd number 3 on the blackboard, so you cannot perform the operation any more.

# Thus, you can perform the operation at most twice.

# Second example:

# Since there is an odd number 5 on the blackboard already in the beginning, You cannot perform the operation at all.




# N = int(input())
# A = list(map(int, input().split()))

# max_operations = 0

# while all(num % 2 == 0 for num in A):
#     A = [num // 2 for num in A]
#     max_operations += 1

# print(max_operations)




N = int(input())

a = list(map(int, input().split()))

answer = 0

all_even = True

for num in a:
    if num % 2 != 0:
        all_even = False
        break

while all_even:
    for i in range(N):
        a[i] //= 2
    answer += 1
    all_even = all(num % 2 == 0 for num in a)

print(answer)

