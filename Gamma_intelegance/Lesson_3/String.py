string_sample = 'hello world world'
string_sample2 = 'hello worlD is lorl ErcaSS'
string_sample3 = ' exstra string '
german_sample = 'der Flur'

print(len(string_sample))  # количество символов в строке
print(string_sample[0:4])  # индексация строки
print(string_sample[-4:-1])  # обратная индексация
print(string_sample[-5:])  # без указания конца, значит до конца
string_sample77 = string_sample[0:10:2]  # переобозначаем переменную со значениями из середины строки с шагом 2
                          # START:END:STEP
print(string_sample77)
print(string_sample[::-1])  # нет начала и конца, значит вся строка с шагом минус один, т.е. с конца в начало
print('world' in string_sample)  # проверяем есть ли слово world в этой строке
