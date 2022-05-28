def earley_parser():
    word = "a+a*a"
    vars = ['E', 'T', 'P']
    term = ['a', '*', '+']
    prods = [('E', 'T'),
             ('E', 'E+T'),
             ('T', 'P'),
             ('T', 'T*P'),
             ('P', 'a')]
    # (left, right, cursor index, h, i)
    situations = [('S', 'E', 0, 0, 0)]

    curr_situation = 0

    while curr_situation < len(situations):
        left = situations[curr_situation][0]
        right = situations[curr_situation][1]
        cursor = situations[curr_situation][2]
        h = situations[curr_situation][3]
        i = situations[curr_situation][4]

        if cursor == len(right):
            for situation in situations:
                if situation[4] == h and situation[2] < len(situation[1]) and situation[1][situation[2]] == left:
                    new_situation = (situation[0], situation[1], situation[2] + 1, situation[3], i)
                    if new_situation not in situations:
                        situations.append(new_situation)

        elif right[cursor] == word[i]:
            new_situation = (left, right, cursor + 1, h, i + 1)
            if new_situation not in situations:
                situations.append(new_situation)

        elif right[cursor] in vars:
            for prod in prods:
                if prod[0] == right[cursor]:
                    new_situation = (prod[0], prod[1], 0, i, i)
                    if new_situation not in situations:
                        situations.append(new_situation)

        if ('S', 'E', 1, 0, len(word)) in situations:
            print(situations)
            return True

        curr_situation += 1

    print(situations)

    return False


print(earley_parser())
