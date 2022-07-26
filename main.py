import ascii_graphics, data_menager, random

ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def pick_random_word(filename):
    words_list = data_menager.get_table_from_file(filename)
    random_word = words_list[random.randint(0, len(words_list) - 1)]
    return random_word


def check_user_letter():
    while True:
        user_letter = input("Please write your letter: ").upper()
        if user_letter.isalpha():
            if len(user_letter) == 1:
                break
            else:
                print('This have to be just ONE letter')
                continue
        else:
            print('Not a letter')
            continue

def main():
    word = pick_random_word('hangman/words.csv')
    check_user_letter()

    
if __name__=='__main__':
    main()