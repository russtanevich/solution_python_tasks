class A(dict):
	__doc__ = dict.__doc__
	pass

print("#Имеем объект словарь\nclass A(dict):\n\tpass\n")


# 1. Как получить список всех аттрибутов объекта
attr 		= dir(A)
print('\n#1. СПИСОК АТТРИБУТОВ: {}'.format(attr))


#2. Как получить список всех публичных аттрибутов объекта
public_attr	= [attr for attr in dir(A) if not attr.startswith('_') ]
print('\n#2. СПИСОК ПУБЛИЧНЫХ АТТРИБУТОВ: {}'.format(public_attr))


#3. Как получить список методов объекта
method		= [attr for attr in dir(A) if callable(getattr(A, attr)) == True]
print('\n#3. СПИСОК МЕТОДОВ ОБЪЕКТА: {}'.format(method))


#4. В какой магической переменной хранится содержимое help
print('\nС#4. ОДЕРЖАНИЕ help(dict): {}'.format(dict.__doc__))


#5. Есть 2 кортежа. Получить третий как конкатенацию двух первых
tuple_1 = (1,2,3)
tuple_2 = (4,5,6)
result 	= tuple_1 + tuple_2
print('\n#5. КОНКАТЕНАЦИЯ КОРТЕЖЕЙ: {} + {} = {}'.format(tuple_1, tuple_2, result))


#6. Есть два кортежа. Получить третий как объединение уникальных элементов первых двух кортежей
tuple_1 = (1,2,3,4,5,6)
tuple_2 = (4,5,6,7,8,9)
result 	= set(tuple_1+tuple_2)
print('\n#6. КОРТЕЖ C УНИКАЛЬНЫМИ ЭЛЕМЕНТАМИ: set({} + {}) = {}'.format(tuple_1, tuple_2, result))


#7. Почему если в цикле for список меняется, используют for i in lst[:]. Что значит [:]
print('\n"#7. b = a[:]" - это копия, a "c = a" cсылка на тот же объект')
a = [1,2,3,4,5]
b = a[:]
c = a
a.append(6)
print('>>> a = [1,2,3,4,5]\n>>> b = a[:]\n>>> c = a\n>>> a.append(6)')
print('a => {}\nb => {}\nc => {}'.format(a,b,c))
print('поэтому, если cам <lst> в цикле изменяется, то при объявлении цикла пользуйте <lst[:]>')


#8. Составть словарь из двух списков - в одном ключи, в другом значения
keys = ['a', 'b', 'c']
vals = [1, 2, 3]
dictionary = dict(zip(keys,vals))
print('\n#8. СЛОВАРЬ ИЗ ДВУХ СПИСКОВ:\ndict(zip({},{})) = {}'.format(keys,vals,dictionary)) 


#9. Словарь из списков разной длины. Есть key, но нет val - то val=None; если нету key - игнорировать
from itertools import zip_longest
keys = ['a', 'b', 'c', 'd']
vals = [1, 2, 3, 4, 5, 6]
dictionary = dict(zip_longest(keys, vals))
print('\n#9. СЛОВАРЬ ИЗ ДВУХ СПИСКОВ:\ndictionary = dict(izip_longest({}, {})) = {}'.format(keys,vals,dictionary)) 
print('!!!Выполнить\nif None in dictionary\n\tdictionary.pop(None)')
if None in dictionary:
	dictionary.pop(None)
print('dictionary = {}'.format(dictionary)) 


#10. Инвертировать словарь (ключи поменять со значениями)
dictionary 		= {'a': 1, 'b': 2, 'c': 3}
new_dictionary	= {key:val for key,val in zip(dictionary.values(), dictionary.keys())}
print('\n#10. ИНВЕРТИРОВАННЫЙ СЛОВАРЬ:\n {} <=> {}'.format(dictionary, new_dictionary))


#11. Есть строка в юникоде. Получить 8-битную строку в кодировках utf-8 и сз1251
uni_str		= 'Привет, мир!'
utf_str		= uni_str.encode('utf-8')
cp1251_str	= uni_str.encode('cp1251')
print('\n#11.\nuni_str = {}\nutf_str = {}\ncp1251_str = {}'.format(uni_str, utf_str, cp1251_str))


#12. Есть строка в cp1251. Получить юникодную
uni_str		= cp1251_str.decode('cp1251')
print('\n#12.\ncp1251_str = {}\nuni_str = {}'.format(cp1251_str, uni_str))

