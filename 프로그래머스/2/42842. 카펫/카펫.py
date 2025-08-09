def solution(brown, yellow):
    # 가로 x 세로 = 개수 => y_row * y_col = yellow
    # 테두리 칸 개수 = 2*전체가로 + 2*전체세로 - 모서리4칸
        # => 2 * (y_row + 2) + 2 * (y_col+2) - 4 = brown
        # => 2*(y_row+y_col+2) = brown
    
    for y_row in range(1, int(yellow**(1/2))+1):
        if yellow % y_row == 0:
            y_col = yellow // y_row
            if brown == 2*(y_row+y_col+2):
                return [max(y_row, y_col)+2, min(y_row, y_col)+2]
    