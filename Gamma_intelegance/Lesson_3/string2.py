string_sample = 'hello world world'
string_sample2 = 'hello worlD is lorl ErcaSS'
string_sample3 = '****exstra string***'
german_sample = 'der Flur'
print(string_sample2.upper())  # после точки применяется метод возведения всех символов в верхний регистр
print(string_sample2.lower())  # приведение всех символов в нижний регистр
print(string_sample2.capitalize())  # делает заглавным первую букву в строке
print('hello', end=' ')
print('world')  # записали два принта в одной строке
print(string_sample3.strip('*'))  # убирает символы в начале и конце строки, если пусто, то убирет пробелы
print(string_sample3.lstrip('*'))  # убирает символы в начале строки и rstrip символы в конце строки
print(string_sample.replace('world', "go", 1))  # заменяет все совпадения внутри строки на новое,цыфра сколько слов
print(string_sample.count('world'))  # считае слова в строке
print(string_sample.count('world', 6, 13))  # считает количество символов от индекса до индекса
print(string_sample.find('world'))  # находит первое совпадение по индексам
