from distutils.command import check
import ascii_graphics, data_menager, random

#ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

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
                print('This have to be just ONE letter.')
                continue
        else:
            print('Not a letter. Try one more time.')
            continue
    return user_letter


def check_letter_to_word(word, user_letter):
    word_list = list(word.strip(''))
    # if user_letter.lower() in word_list:
    #     return True
    # else:
    #     return False
    for letter in word_list:
        if letter == user_letter.lower():
            print('Right')
        else:
            print('Wrong')



def main():
    word = pick_random_word('words.csv') # wybiera losowe słowo z pliku csv
    print(word)
    user_letter = check_user_letter() # sprawdza poprawność wpisanej danej
    check_letter_to_word(word, user_letter) # printuje false/true w zależności czy dana litera jest w słowie
    
if __name__=='__main__':
    main()