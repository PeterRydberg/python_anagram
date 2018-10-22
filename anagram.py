import codecs

filename = "eventyr.txt"
file = codecs.open(filename, encoding='utf-8')

words = [line.strip('\r\n') for line in file]

# Compares word for anagram check
def compare(word1, word2):
    sort1 = sorted(word1)
    sort2 = sorted(word2)

    if(sort1 == sort2):
        print(word1, "and", word2, "are anagrams")

# Bad runtime with duplicates
def anagram_naive():
    for word1 in words:
        for word2 in words:
            compare(word1, word2)

anagram_naive()

