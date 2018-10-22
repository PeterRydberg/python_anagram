import codecs

filename = "eventyr.txt"
file = codecs.open(filename, encoding='utf-8')

words = [line.strip('\r\n') for line in file]


# Compares word for anagram check
def compare1(word1, word2):
    sort1 = sorted(word1) # These sorts has a runtime of O(nlogn)
    sort2 = sorted(word2)

    if(sort1 == sort2):
        print("\'", word1, "\' and \'", word2, "\' are anagrams", sep='')


# Same comparison as above, but removes needless sort on different-length words and identical words
def compare2(word1, word2):
    if((len(word1) == len(word2)) and (word1 != word2)):
        sort1 = sorted(word1) # These sorts has a runtime of O(nlogn)
        sort2 = sorted(word2)

        if (sort1 == sort2):
            print("\'",word1, "\' and \'", word2, "\' are anagrams",sep='')


# Bad runtime with duplicates and anagrams of same word
def anagram_naive():
    for word1 in words:
        for word2 in words:
            compare1(word1, word2)


# Removes uneccessary duplicate comparison
def anagram_improved():
    for i, word1 in enumerate(words):
        for word2 in words[i + 2:]:
            compare2(word1, word2)


anagram_naive()
print("-----------------   NEW   -----------------")
anagram_improved()
