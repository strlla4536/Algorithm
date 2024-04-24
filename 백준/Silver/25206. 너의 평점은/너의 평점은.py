
gpa_sum = 0  # 학점 총합
gpa_times_grade = 0 # 과목별 학점x과목평점

for i in range(20):
  # 과목명, 학점, 등급(->과목평점)
  #class, gpa, grade = 
  li = list(map(str,input().split()))
  if li[2] == 'P' :
    pass
  else:
    gpa_sum += float(li[1]) 

  if li[2] == 'A+':
    li[2] = 4.5
  elif li[2] == 'A0':
    li[2] = 4.0

  elif li[2] == 'B+':
    li[2] = 3.5
  elif li[2] == 'B0':
    li[2] = 3.0

  elif li[2] == 'C+':
    li[2] = 2.5
  elif li[2] == 'C0':
    li[2] = 2.0

  elif li[2] == 'D+':
    li[2] = 1.5
  elif li[2] == 'D0':
    li[2] = 1.0

  else:
    li[2] = 0

  gpa_times_grade += float(float(li[1]) * li[2])

print(gpa_times_grade / gpa_sum)
