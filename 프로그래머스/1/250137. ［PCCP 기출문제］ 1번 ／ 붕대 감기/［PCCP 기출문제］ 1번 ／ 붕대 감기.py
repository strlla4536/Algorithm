def solution(bandage, health, attacks):
    # bandage = [시전 시간(t), 초당 회복량(x), 추가 회복량(y)]
    # health = 최대 체력
    # attacks = [공격 시간, 피해량]
    
    last_attack_time = attacks[-1][0]
    attack = False
    time, continuous = 0, 0
    hp = health # 캐릭터의 체력
    
    while time <= last_attack_time:
        if attacks[0][0] == time:
            attack = True
            continuous = 0
            hp -= attacks[0][1]
            attacks.pop(0)
            
            if hp <= 0:
                return -1
            
        else:
            continuous += 1
            if continuous == bandage[0]:
                hp += (bandage[1]+bandage[2])
                continuous = 0
            else:
                hp += bandage[1]
            
            if hp >= health:
                hp = health
        
        attack = False
        time += 1
    
    return hp