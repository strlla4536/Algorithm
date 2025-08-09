def solution(n):
    # 1의 개수를 세고, 1씩 더해가면서 1의 개수 같아지면 stop
    one = bin(n).count('1')
    
    while True:
        n += 1
        if bin(n).count('1') == one:
            return n
    