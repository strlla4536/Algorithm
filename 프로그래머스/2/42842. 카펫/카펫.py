def check(brown, yellow, y_row, y_col):
    a = brown + yellow
    b = (y_row+2) * (y_col+2)
    print("갈 + 노 = ",a)
    print("가로 * 세로 = ", b)
    if a % b == 0:
        print("실행1")
        return True
    else:
        print("실행2")
        return False
    
    
def solution(brown, yellow):
    # (brown + yellow) = (yellow_row + 2) * (yellow_col + 2)
    # yellow = yellow_row * yellow_col
    if yellow == 1:
        return [3, 3]
    if yellow == 2:
        return [4, 3]
        
    for r in range(1, yellow//2+1):
        print("yellow row : ", r)
        
        if yellow % r == 0:
            print("1")
            c = yellow // r
            print("c:", c)
            
            if r>=c:
                print("brown, yellow row, yellow col = ", brown, r, c)
                if check(brown, yellow, r, c):
                    print("check:", check)
                    return [r+2, c+2]
    