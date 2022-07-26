import ascii_graphics, data_menager, random

def pick_random_word(filename):
    words_list = data_menager.get_table_from_file(filename)
    random_word = words_list[random.randint(0, len(words_list) - 1)]
    return random_word


print(pick_random_word('hangman/words.csv'))