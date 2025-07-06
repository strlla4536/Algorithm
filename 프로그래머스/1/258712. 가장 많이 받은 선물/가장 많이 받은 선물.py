def solution(friends, gifts):
    # 친구 수
    friends_num = len(friends)

    # 1) 주고받은 선물 기록 초기화
    # gift_record[i][j] = i가 j로부터 받은 선물 수
    gift_record = [[0] * friends_num for _ in range(friends_num)]

    # gifts 리스트를 순회하며 기록 업데이트
    for gift in gifts:
        # giver: 선물 준 사람, receiver: 선물 받은 사람
        giver, receiver = gift.split()
        giver_idx = friends.index(giver)
        receiver_idx = friends.index(receiver)
        gift_record[receiver_idx][giver_idx] += 1

    # 2) 선물 지수 계산
    # gift_score[i] = (i가 친구들에게 준 선물 수) - (i가 친구들에게 받은 선물 수)
    gift_score = [0] * friends_num
    for i in range(friends_num):
        # i가 "준" 총합 = sum of column i
        given = sum(gift_record[row][i] for row in range(friends_num))
        # i가 "받은" 총합 = sum of row i
        received = sum(gift_record[i])
        gift_score[i] = given - received
        # 디버그: 지수 출력
        print(f"gift_score[{i}] = {gift_score[i]}")

    print(f"전체 선물 지수: {gift_score}")

    # 3) 다음 달 예상 받을 선물 수 계산
    # get_gift_list[i] = i가 받을 선물 개수
    get_gift_list = [0] * friends_num

    # 친구 쌍(i, j)에 대해 비교
    for i in range(friends_num - 1):
        for j in range(i + 1, friends_num):
            # 3-1) 직접 주고받은 기록이 다르다면
            if gift_record[i][j] != gift_record[j][i]:
                # 기록이 많은 쪽이 다음 달에 받는다
                if gift_record[i][j] < gift_record[j][i]:
                    # j가 i에게 더 많이 줬으므로 i가 받고
                    get_gift_list[i] += 1
                else:
                    # i가 j에게 더 많이 줬으므로 j가 받음
                    get_gift_list[j] += 1
            else:
                # 3-2) 직접 기록이 없거나 같다면 선물 지수로 판단
                if gift_score[i] > gift_score[j]:
                    get_gift_list[i] += 1
                elif gift_score[i] < gift_score[j]:
                    get_gift_list[j] += 1
                # 같으면 아무도 받지 않음

    # 디버그: 각 친구가 받을 선물 수
    print(f"선물 내역 : {gift_record}")
    print(f"예상 받을 선물 수 : {get_gift_list}")

    # 4) 가장 많이 받을 친구가 받을 선물 수 리턴
    return max(get_gift_list)
