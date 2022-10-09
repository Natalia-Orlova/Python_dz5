# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1
# out
# The data is incorrect

from random import sample

def form_word_list(count, alph = 'абв'):
    result = []
    for i in range(count):
        temp = sample(alph, 3)
        result.append("".join(temp))
    return " ".join(result)

def del_word(word_list):
    return word_list.replace('абв ', "")


count = int(input("Введите количество слов: "))
full_list = form_word_list(count)
print(full_list)
print(del_word(full_list))
