import re
from typing import List
from sort_functions import sorting_by_order, sorting_by_frequency


def page_turner():
    """ Процедура, "переворачивающая" страницу

        Если номер текущей считанной строки - 46, увеличиваем текущее значение страницы,
        обнуляя счетчик строк.

    """
    global page_number, line_number
    if line_number == 46:
        line_number = 0
        page_number += 1


dictionary = {}
page_number = 1
line_number = 0
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
print('Да - введите число позиций в этом списке, Нет - введите "0":')
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
        page_turner()
        words: List[str] = re.split("[, \"/\[\]()—!?.:;*]+", line)
        for i in words:
            if i and len(i) >= small_words:
                if i not in dictionary:
                    count_of_words += 1
                    dictionary[i] = [1, [page_number]]
                else:
                    dictionary[i][0] += 1
                    if page_number not in dictionary[i][1]:
                        dictionary[i][1].append(page_number)
    line = input()
print(dictionary)
with open("Output.txt", 'w', encoding='utf-8') as output_data:
    sorted_by_order = sorting_by_order(dictionary)
    for i in sorted_by_order:
        output_data.write('%s встречено на следующих страницах:' % i)
        for j in range(len(dictionary[i][1])):
            if j != len(dictionary[i][1]) - 1:
                output_data.write(' %s,' % dictionary[i][1][j])
            else:
                output_data.write(' %s;' % dictionary[i][1][j])
        output_data.write('\n')
    if top_words:
        output_data.write('Список из %s наиболее встречающихся cлов в тексте:\n' % top_words)
        sorted_by_frequence = sorting_by_frequency(dictionary)
        print(sorted_by_frequence)
        if top_words <= count_of_words:
            n = top_words
        else:
            n = count_of_words
        for a in range(n):
            output_data.write(
                '%s было встречено %s раз(а)\n' % (sorted_by_frequence[a][0], sorted_by_frequence[a][1][0]))