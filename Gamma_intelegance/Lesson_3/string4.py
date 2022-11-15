new_string = 'its {product} costs {price} dollsrs'
print(new_string.format(price='1000', product='phone'))
# задали переменную в скобках и дали ему значение в нижних скобках по ключу
name = 'Tema'
suname = 'Romanov'
age = 30
print(f'My name is {name}. My suname is {suname}. I`m {age + 30} years ago')
# перед строкой указываем f, т.е. форматирование
byte_string = b'\xcf\x84o\x82'
print(byte_string.decode('utf-16'))  # декодировка с китайского языка
name_string = "артем романов"
name_string = name_string.encode('utf-16')
print(name_string)  # закодировали строку, для работы с разными языками

x = 7
if x > 10:
    print('x smaller 10')  # тело условия if
elif x == 5:  #  в другом случае, если
    print('x is 5')
elif x == 6:
    print('x is 6')
else:  # если ниодно из условий не верно, то будте элсе
    print('its not true')
# если не выполняется первое условие то выполняется второе, если не второе то третье
x = input('input your number: ')
if len(x) == 11:
    print('ok')
else:
    if len(x) < 11:
        print('smaller 11')
    elif len(x) > 11:
        print('bigger 11')
# есть несколько разных способов написать это выражение, выбираем самый простой
