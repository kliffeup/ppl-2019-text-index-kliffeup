import re
from typing import List
from sort_functions import sorting_by_order, sorting_by_frequency

vocabulary = {}
page_number = 1
line_number = 0
page_size = 46
print('Здравствуйте, Вас приветствует Составитель индекса текста!')
print('Желаете сохранять регистр символов при составлении индекса?')
print('Да - введите "1", Нет - введите "0":')
char_case = int(input())
print('Желаете учитывать служебные части речи (местоимения, предлоги, междометия и т.п.) при составлении индекса?')
print('Да - введите "1", Нет - введите "0":')
small_words = int(input())
if small_words:
    small_words = 0
else:
    small_words = 4
print('Желаете составить список наиболее часто встречающихся слов?')
# Надеюсь, что юзер всё-таки увидит приписку "ЦЕЛОЕ", прежде напечатает что-то отличное
# от от целого положительного числа
print('Да - введите ЦЕЛОЕ ПОЛОЖИТЕЛЬНОЕ число позиций в этом списке, Нет - введите "0":')
top_words = int(input())
count_of_words = 0
print('Введите свой текст ниже, для окончания считывания переведите строку после последней строки текста'
      ' и наберите следующую строку:')
print('end of text input')
line = str(input())
while line != 'end of text input':
    if char_case == 0:
        line = line.lower()
    if line:
        line_number += 1
        if line_number == page_size:
            line_number = 1
            page_number += 1
        words: List[str] = re.split("[, \"/\[\]()—!?.:;*]+", line)
        # i бегает по элементам списка слов, считанных с вновь введённой строки;
        # он, конечно, будет целым
        for i in words:
            if i and len(i) >= small_words:
                if i not in vocabulary:
                    count_of_words += 1
                    vocabulary[i] = [1, [page_number]]
                else:
                    vocabulary[i][0] += 1
                    if page_number not in vocabulary[i][1]:
                        vocabulary[i][1].append(page_number)
    line = input()
with open("Output.txt", 'w', encoding='utf-8') as output_data:
    sorted_by_order = sorting_by_order(vocabulary)
    output_data.write("Алфавитный индекс слов, встретившихся в введённом тексте:\n")
    for k in sorted_by_order:
        output_data.write(f"{k} встречено на следующих страницах:")
        for j in range(len(vocabulary[k][1])):
            if j != len(vocabulary[k][1]) - 1:
                output_data.write(f" {vocabulary[k][1][j]},")
            else:
                output_data.write(f" {vocabulary[k][1][j]}.")
        output_data.write('\n')
    if top_words:
        output_data.write(f'Список из {top_words} наиболее встречающихся cлов в тексте:\n')
        sorted_by_frequence = sorting_by_frequency(vocabulary)
        if top_words <= count_of_words:
            n = top_words
        else:
            n = count_of_words
        for a in range(n):
            if a != n - 1:
                output_data.write(
                    f'{sorted_by_frequence[a][0]} было встречено {sorted_by_frequence[a][1][0]} раз(а),\n')
            else:
                output_data.write(
                    f'{sorted_by_frequence[a][0]} было встречено {sorted_by_frequence[a][1][0]} раз(а).\n')
