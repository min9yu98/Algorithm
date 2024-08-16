def solution(bandage, health, attacks):
    max_health = health
    max_time = attacks[-1][0]
    attacked = {}
    for i in attacks:
        attacked[i[0]] = i[1]
    seq_time = 0
    t = 0
    while t <= max_time:
        if t in attacked:
            health -= attacked[t]
            seq_time = 0
            if health <= 0:
                return -1
        else:
            seq_time += 1
            if seq_time < bandage[0]:
                health += bandage[1]
                if health > max_health:
                    health = max_health
            else:
                health += bandage[2] + bandage[1]
                if health > max_health:
                    health = max_health
                seq_time = 0
        t += 1      
    return health