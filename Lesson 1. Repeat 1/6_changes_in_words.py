import sys

word = input()
words = list(map(str.strip, sys.stdin))
right_words = []

for word1 in words:
    new_word = list(word)
    flag = False
    for i in range(len(word1)):
        if word1[i] in new_word:
            new_word.remove(word1[i])
        else:
            flag = True
            break
    if flag:
        continue
    else:
        right_words.append(word1)
print(len(right_words))
print('\n'.join(right_words))
