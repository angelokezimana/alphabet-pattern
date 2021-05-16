__author__ = "Kezimana Aimé-Angelo"


alphabets = {
    'A': [(-2, 1, -2), (1, -3, 1), (5,), (1, -3, 1), (1, -3, 1)],
    'B': [(4, -1), (1, -3, 1), (4, -1), (1, -3, 1), (4, -1)],
    'C': [(-1, 4), (1, -4), (1, -4), (1, -4), (-1, 4)],
    'D': [(4, -1), (1, -3, 1), (1, -3, 1), (1, -3, 1), (4, -1)],
    'E': [(5,), (1, -4), (5,), (1, -4), (5,)],
    'F': [(5,), (1, -4), (5,), (1, -4), (1, -4)],
    'G': [(5,), (1, -4), (1, -2, 2), (1, -3, 1), (5,)],
    'H': [(1, -3, 1), (1, -3, 1), (5,), (1, -3, 1), (1, -3, 1)],
    'I': [(1,), (1,), (1,), (1,), (1,)],
    'J': [(5,), (-4, 1), (-4, 1), (-3, 1, -1), (2, -3)],
    'K': [(1, -3, 1), (1, -2, 1, -1), (2, -3), (1, -2, 1, -1), (1, -3, 1)],
    'L': [(1, -4), (1, -4), (1, -4), (1, -4), (5,)],
    'M': [(1, -3, 1), (2, -1, 2), (1, -1, 1, -1, 1), (1, -3, 1), (1, -3, 1)],
    'N': [(1, -3, 1), (2, -2, 1), (1, -1, 1, -1, 1), (1, -2, 2), (1, -3, 1)],
    'O': [(-1, 3, -1), (1, -3, 1), (1, -3, 1), (1, -3, 1), (-1, 3, -1)],
    'P': [(4, -1), (1, -3, 1), (4, -1), (1, -4), (1, -4)],
    'Q': [(-1, 3, -1), (1, -3, 1), (2, -2, 1), (1, -1, 1, -1, 1), (-1, 3, -1)],
    'R': [(4, -1), (1, -3, 1), (4, -1), (1, -1, 1, -2), (1, -3, 1)],
    'S': [(-1, 4), (1, -4), (-1, 3, -1), (-4, 1), (4, -1)],
    'T': [(5,), (-2, 1, -2), (-2, 1, -2), (-2, 1, -2), (-2, 1, -2)],
    'U': [(1, -3, 1), (1, -3, 1), (1, -3, 1), (1, -3, 1), (-1, 3, -1)],
    'V': [(1, -3, 1), (1, -3, 1), (1, -3, 1), (-1, 1, -1, 1, -1), (-2, 1, -2)],
    'W': [(1, -3, 1), (1, -3, 1), (1, -1, 1, -1, 1), (2, -1, 2), (1, -3, 1)],
    'X': [(1, -3, 1), (1, -3, 1), (-2, 1, -2), (1, -3, 1), (1, -3, 1)],
    'Y': [(1, -3, 1), (-1, 1, -1, 1, -1), (-2, 1, -2), (-2, 1, -2), (-2, 1, -2)],
    'Z': [(5,), (-3, 1, -1), (-2, 1, -2), (-1, 1, -3), (5,)],
}


def transform_a_word(word: str) -> list:
    if len(word)-1 >= 1:
        concatenate_2_lists = list(
            zip(alphabets[word[0]], alphabets[word[1]]))

        result = [tuple_in_list[0]+(-3,)+tuple_in_list[1]
                  for tuple_in_list in concatenate_2_lists]

        if len(word)-1 >= 2:
            return [tuple_in_list[0]+(-3,)+tuple_in_list[1]
                    for tuple_in_list in list(zip(result, transform_a_word(word[2:])))]

        if len(word)-1 == 1:
            return result

    return alphabets[word[0]]


word = input(
    "Enter a word (numbers or special characters not allowed):").upper()

try:
    get_a_word_transformed = transform_a_word(word)
    for items_of_tuple in get_a_word_transformed:
        merge_items = ''
        for number in items_of_tuple:
            if number < 0:
                merge_items += ' ' * abs(number)
            else:
                merge_items += 'X' * number

        print(merge_items)

except KeyError:
    print("Numbers or special characters not allowed. Only letters allowed!!")
