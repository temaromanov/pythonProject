int_var = 500
float_var = 200.7
sting_var_text = 'hello'
sting_var_num = '122.7'
bool_var = True
print(type(int_var))
int_var = str(int_var)  # присваеваем переменной новое значение
print(type(int_var))
# код читается сверху вниз, слева направо, поэтому сначала класс int а затем str
print(sting_var_text + str(int_var))  # конвертируем тип переменной с int на str
print(sting_var_text + str(bool_var))  # булиевое значение конвертируется либо в Teue или в False
print(int(float(int_var)))  # сначала конвертируем во флоут а потом уже в интенджер
print(bool(int_var))  # будет тру так как число не равно 0, иначе будет фалс

user_input = input()
print(user_input)  # сохраняется значение внесенное пользователем
print(type(user_input))
user_input = float(user_input)
print(type(user_input))
#  в инпут всегда тип данных строка и его необходимо конвертировать в int если необходимо


