from sys import stdin
word = list(stdin.readline().rstrip().upper())
set_word = list(set(word))
freq_list = [0]*len(set_word)

for i in range(len(set_word)):
    freq_list[i] = word.count(set_word[i])
freq_max = max(freq_list)
if freq_list.count(freq_max) > 1:
    print('?')
else:
    print(set_word[freq_list.index(freq_max)])