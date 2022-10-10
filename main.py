import ascii_graphics, data_menager, random

#ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

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
    



def main():
    word = pick_random_word('words.csv') # wybiera losowe słowo z pliku csv
    print(word) #checking
    display_list = display(word)
    print(' '.join(display_list))

    
    user_letter = check_user_letter()
    guessed = ' '.join(check_letter_to_word(word, user_letter, display_list))

    
if __name__=='__main__':
    main()