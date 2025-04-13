def remove_words(infile):
    # Opening words file
    file = open(infile, 'r', encoding='utf-8')

    lines = file.readlines()
    five_letters = []


    # Going through and ignoring all words that are too long or short
    for line in lines:
        word = line.strip()
        if len(word) == 5:
            five_letters.append(word)


    file.close()
    return five_letters


def update_words(outfile, words_list):
    file = open(outfile, 'w', encoding='utf-8')
    list_len = len(words_list)

    for i in range(list_len):
        word = words_list[i]

        # Avoiding \n on last line of outfile
        if i < list_len - 1:
            file.write(f'{word}\n')

        else:
            file.write(word)

    file.close()


def main():
    file = 'words.txt'

    # Setting up test on infile
    infile = open(file, 'r', encoding='utf-8')
    init_len = len(infile.readlines())
    infile.close()


    # Cleaning infile for only 5 letter words
    clean_words = remove_words(file)
    clean_len = len(clean_words)

    # Condition controlling to update file
    if init_len > clean_len:
        update_words(file, clean_words)


main() 
