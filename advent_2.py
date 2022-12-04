SCORE_MAP = {
    "X": (1,3), #rock
    "Y": (2,1), #paper
    "Z": (3,2), #scissors
    "A": (1,3),
    "B": (2,1),
    "C": (3,2)
}

def get_score_value_from_map(k):
    return SCORE_MAP[k]

def get_winning_hand(val):
    for x in SCORE_MAP:
        (score, defeats)=SCORE_MAP[x]
        if defeats== val:
            return score

def play_round(left,right):
    (left_val, left_defeats) = left
    (right_val, _) = right
    if right_val== 1:
        return left_defeats
    elif right_val == 2:
        return left_val + 3
    elif right_val == 3:
        return get_winning_hand(left_val) + 6



def get_round_score(left,right):
    (left_val, _) = left
    (right_val, right_defeats) = right
    score = 0
    if left_val== right_defeats:
        score += 6
    elif right_val == left_val:
        score += 3
    return score + right_val

def problem_1():
    with open('advent_2.in') as file:
        data = [i for i in file.read().strip().split('\n')]
    
    input_left = []
    input_right = []

    for e in data:
        actions = e.split(" ")
        input_left.append(get_score_value_from_map(actions[0]))
        input_right.append(get_score_value_from_map(actions[1]))


    total_score = 0
    total_score_2 = 0
    for i,e in enumerate(input_left):
        total_score += get_round_score(input_left[i],input_right[i])
        total_score_2 += play_round(input_left[i],input_right[i])

    print(total_score)
    print(total_score_2)

problem_1()
