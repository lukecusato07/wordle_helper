'''
Starter words should use as many vowels and common letters as possible

Method for suggesting:

    - Prioritize words with vowels and common consonants (r, s, t, l, n)
    - Score the word based on the letters:
        - Score = (vowels * 2) + (number of consonants)
        - Prioritizes vowels for the starting word

'''

from random import randint
def suggest_word(valid_file):
    vowels = [97, 101, 105, 111, 117]
    consonants = [114, 115, 116, 108, 110]  # Common consonants

    # Files to be used
    # words = open(words_file, 'r', encoding='utf-8')
    valid = open(valid_file, 'r', encoding='utf-8')
    lines = valid.readlines()

    # Storing possible suggestions + score
    suggestions = {}

    for line in lines:
        line = line.strip()

        score = 0
        for l in line:
            if ord(l) in vowels:
                score += 2
            elif ord(l) in consonants:
                score += 1
        
        # Getting the average score of each char
        score /= 5
        suggestions[line] = score

    return suggestions


def extract_top(suggestions):
    top_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse = True)
    top_suggestions = dict(top_suggestions)


    # If there are multiple words with a top score, randomize which word is suggested
    to_extract = []
    max_score = max(top_suggestions.values())

    for word, score in top_suggestions.items():
        if score == max_score:
            to_extract.append(word)



    if len(to_extract) > 1:
        choice = randint(0, len(to_extract) - 1)
        starter = to_extract[choice]

    else:
        starter = to_extract[0]


    return starter


def main():
    suggestion = suggest_word('valid_words.txt')
    starter = extract_top(suggestion)

    # Make it so that this word is given to the JS file to display to the user
    print(starter)


main() 
    