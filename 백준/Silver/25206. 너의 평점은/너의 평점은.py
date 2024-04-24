grades = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']  # 등급
gpas = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]  # 과목평점

mul = 0 # 학점 x 과목평점
time_sum = 0 # 학점 총합

for i in range(20):
  # 과목, 학점, 등급
  a, b, c = map(str, input().split())
  if c in grades:
    c = gpas[grades.index(c)]
    time_sum += float(b)
    mul += float(b) * float(c)

print(mul / time_sum)