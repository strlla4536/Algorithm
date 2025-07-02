def solution(mats, park):
    n = len(park)
    m = len(park[0])

    # 1. park을 0(비어있음), 1(사람있음)으로 변환
    board = [[0 if cell == "-1" else 1 for cell in row] for row in park]

    # 2. 큰 돗자리부터 시도
    for size in sorted(mats, reverse=True):
        if size > n or size > m:
            continue  # 돗자리가 공원보다 큰 경우 건너뜀

        # 3. 모든 좌표에서 size x size 가능한지 확인
        for i in range(n - size + 1):
            for j in range(m - size + 1):
                can_place = True
                for x in range(i, i + size):
                    for y in range(j, j + size):
                        if board[x][y] == 1:
                            can_place = False
                            break
                    if not can_place:
                        break
                if can_place:
                    return size  # 가장 큰 크기부터 찾기 때문에 바로 return

    return -1
