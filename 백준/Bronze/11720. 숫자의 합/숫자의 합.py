n = int(input())

nums = input()
sum = 0

numList = [int(i) for i in nums]

for i in range(n):
  sum += numList[i]

print(sum)