import codecs


# Compares word for anagram check
def compare1(word1, word2):
    sort1 = sorted(word1) # These sorts have a runtime of O(nlogn)
    sort2 = sorted(word2)

    # Returns true if anagrams
    if(sort1 == sort2):
        #print("\'", word1, "\' and \'", word2, "\' are anagrams", sep='')

        return True


# Same comparison as above, but removes needless sort on different-length words and identical words
def compare2(word1, word2):
    if((len(word1) == len(word2)) and (word1 != word2)):
        sort1 = sorted(word1) # These sorts have a runtime of O(nlogn)
        sort2 = sorted(word2)

        # Returns true if anagrams
        if (sort1 == sort2):
            #print("\'",word1, "\' and \'", word2, "\' are anagrams", sep='')

            return True


# Bad runtime with duplicates and anagrams of same word
def anagram_naive():
    for word1 in words:
        for word2 in words:
            compare1(word1, word2)


# Removes uneccessary duplicate comparison
def anagram_improved():
    for i, word1 in enumerate(words):
        temp_anagrams = set()

        for word2 in words[i + 2:]:

            # Compares the words for anagramity
            if(compare2(word1, word2)):
                temp_anagrams.add(word1)
                temp_anagrams.add(word2)

                # This is done so that word2 won't compare to other anagrams later, as we know this will be done by word1 anyways
                words.remove(word2)

        # Adds anagrams to set if there are any
        if(len(temp_anagrams) != 0):
            anagrams.append(temp_anagrams)


if __name__ == '__main__':

    # Opens file and writes words to list
    filename = "eventyr.txt"
    file = codecs.open(filename, encoding='utf-8')
    words = [line.strip('\r\n') for line in file]

    # Creates a list for anagrams to exist in
    anagrams = []
    anagram_improved()

    # Full anagram content
    print(anagrams)

    # Prints pretty
    for i in anagrams:
        for j in i:
            print(j, '', end='')
        print('')