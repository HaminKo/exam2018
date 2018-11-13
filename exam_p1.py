import string

def load_words(file_name):
    """
    Loads a txt file where each word is on a new line.

    Returns a list of words.
    """
    word_list = []

    word_file = open(file_name, 'r')

    strippables = string.punctuation + string.whitespace
    
    for word in word_file:
        word = word.strip(strippables)
        word_list.append(word)
    
    return word_list

def load_first_names(file_name):
    """
    Loads a file with a list of names and returns a list with only the first names.
    """
    return [name.split()[0] for name in load_words(file_name)]


def letter_point():
    """
    Returns a dictionary of letters with their points
    """
    letter_values = {}
    value = 0

    for letter in string.ascii_lowercase:
        value += 1
        letter_values[letter] = value
    
    return letter_values

def score_name(name):
    """
    Gives a numerical score based on alphabetical position of each letter in the name.

    Returns an integer
    """
    letter_score = letter_point()
    total_score = 0

    for letter in name.lower():
        if letter in letter_score:
            total_score += letter_score[letter]
    
    return total_score

def rank_names(name_list):
    """
    Orders a dict of names by most to least valuable.

    Returns a dict
    """
    names_score = {}

    for name in name_list:
        names_score[name] = score_name(name)
    
    return sorted(names_score.items(), key=lambda key_value: key_value[1], reverse=True)

def get_most_valuable_name(name_list):
    """
    Returns most valuable name form a list of names.
    """
    ordered_list = rank_names(name_list)

    return ordered_list[0]

def find_positive_words(name, word_list):
    """
    Returns a list of positive words
    """
    name_score = score_name(name)
    words = []

    for word in word_list:
        if score_name(word) == name_score:
            words.append(word)
    

    return None if len(words) == 0 else words
        



def main():
    first_names = load_first_names('roster.txt')
    positive_words = load_words('positive-words.txt')
    # print(first_names)

    # print(letter_point())

    # print(score_name('ABC'))

    # print(rank_names(first_names))

    most_valuable_name = get_most_valuable_name(first_names)
    print("The most valuable person in our class is {} with a name-score of {}.".format(most_valuable_name[0], most_valuable_name[1]))

    # name = 'Ha'

    # same_value_positive_words = find_positive_words(name, positive_words)
    # print(same_value_positive_words)

    # if same_value_positive_words:
    #     print('The following words share the same value as your name:')
    #     for word in same_value_positive_words:
    #         print(word)
    # else:
    #     print('No words share the same value as your name')

    name = 'Ha Min'

    same_value_positive_words = find_positive_words(name, positive_words)
    # print(same_value_positive_words)

    if same_value_positive_words:
        print('The following words share the same value as your name: {}, which has {} points.'.format(name, score_name(name)))
        for word in same_value_positive_words:
            print(word)
    else:
        print('No words share the same value as your name')

if __name__ == '__main__':
    main()
