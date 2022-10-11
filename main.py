import ascii_graphics, data_menager, random

LIVES = 0


def pick_random_word(filename):
    words_list = data_menager.get_table_from_file(filename)
    random_word = random.choice(words_list)
    return random_word


def check_user_letter():
    while True:
        user_letter = input("Please write your letter: ").upper()
        if user_letter.isalpha():
            if len(user_letter) == 1:
                break
            else:
                print('This have to be just ONE letter.')
                continue
        else:
            print('Not a letter. Try one more time.')
            continue
    return user_letter


def display(word):
    display_list = []
    for letter in word:
        display_list.append('_')
    return display_list


def check_letter_to_word(word, user_letter, display_list):
    for position in range(len(word)):
        letter = word[position]
        if letter == user_letter.lower():
            display_list[position] = user_letter
    return display_list

    
def print_lives(LIVES):
    print(ascii_graphics.lives_graphics[LIVES - 1])

    
def guessing_word(word, display_list):
    global LIVES
    while LIVES <= 7:
        if LIVES == 7:
            print('You failed.')
            break
        else:
            if '_' in display_list:
                user_letter = check_user_letter()
                if user_letter.lower() in word:
                    guessed = ' '.join(check_letter_to_word(word, user_letter,  display_list))
                    print(guessed)
                else:
                    LIVES += 1
                    print_lives(LIVES)
            else:
                print('You have win.')
                break

def main():
    word = pick_random_word('words.csv') # wybiera losowe słowo z pliku csv
    print(word) #checking
    display_list = display(word)
    print(' '.join(display_list))
    guessing_word(word, display_list)


    
if __name__=='__main__':
    main()