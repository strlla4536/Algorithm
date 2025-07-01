def solution(n, w, num):
    w2 = w*2    # 2w 주기로 반복됨
    
    m1 = num % (w2) # 반복되는 주기에서 몇 번째 인지
    m2 = ((w2+1) - m1)%(w2)   
    
    # num 이상 n 이하의 수들 중 2*w로 나눈 나머지가 m1,m2인 것들의 수를 세면 된다.
    return len(range(num,n+1,w*2)) + len(range(num + (m2-m1)%(w*2), n+1, w*2))