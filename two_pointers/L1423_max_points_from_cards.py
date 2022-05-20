

def get_max_points_from_cards_opt(card_points,k):
    l = 0
    r = len(card_points) - k
    max_sum = sum(card_points[r:])
    total = max_sum
    while r < len(card_points):
        total  +=( card_points[l] - card_points[r])

        max_sum = max(max_sum, total)
        l += 1
        r += 1

    return max_sum

def get_max_points_from_cards(card_points,k):

    if len(card_points) <= k:
        return sum(card_points)

    max_sum = 0

    front = card_points[:k]
    back = list(reversed(card_points[len(card_points)-k:]))

    print(front, back)

    for i in range(k):
        tot_1 = sum(front[:(i+1)])

        if i+1 != k:
            tot_1 += sum(back[:k-(i+1)])

        tot_2 = sum(back[:(i+1)])

        if i+1 != k:
            tot_2 += sum(front[:k-(i+1)])

        max_sum = max(max_sum, tot_1, tot_2)

    return max_sum



card_points = [1,2,3,4,5,6,1]
k = 3
print('max points from cards are {}'.format(get_max_points_from_cards_opt(card_points,k)))