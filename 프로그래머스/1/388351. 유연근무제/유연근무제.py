def solution(schedules, timelogs, startday):
    answer = 0
    num_employee = len(schedules)
    # 출근 희망시간을 출근 인정시간으로 업데이트
    for i in range(len(schedules)):
        schedules[i] += 10
        if schedules[i] % 100 >= 60:
            schedules[i] += 40  
            # 희망 출근 시각이 50분 ~ 59분일 때만 60분을 넘어가게 됨 -> 1시간 추가, 60분 삭제 => 40분 + 처음 더해준 10분 = 50분만 추가하면 됨
        
        # 출근 기록에서 토요일 & 일요일 삭제
        if startday != 7:
            del timelogs[i][6-startday:8-startday]
        else:
            del timelogs[i][6]
            del timelogs[i][0]
    
    print("timelogs : ", timelogs)
    for employee in range(num_employee):
        for day in range(5):
            if timelogs[employee][day] > schedules[employee]:
                break
            else:
                if day==4:
                    answer+=1
    return answer