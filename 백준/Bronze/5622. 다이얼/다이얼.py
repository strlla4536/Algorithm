# import sys
# input = sys.stdin.readline

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

word = input()
sum = 0

for w in range(len(word)):
  for i in dial:
    if word[w] in i:
      sum += dial.index(i) + 3


print(sum)