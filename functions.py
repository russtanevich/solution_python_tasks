#1. Написать функцию, которая суммирует все, что в нее передают(кортежи, списки, числа)

def sum_all(*args):
	result = 0
	def sum_iter(args):
		nonlocal result
		for arg in args:
			if not hasattr(arg, '__iter__'):
				result += arg
			else:
				sum_iter(arg)
	sum_iter(args)
	return result


args = ( [ 1, 2, 3, 4, [5, 6] ], ( 7, 8, ( 9, 10 ) ) )
q = sum_all(args)
print('\n#1.\nsum_all({}  =>  {}'.format(args, q))


#2. Написать фунцию фабрику сложения с аргументом
def addition(arg_1):
	def inner(arg_2):
		return arg_1 + arg_2
	return inner

# реализация с lambda функцией
def add_lambda(arg_1):
	return lambda x: arg_1 + x

add5 = addition(5)
print('\n#2. \nadd(5) = addition(5)')
print('add5(2)')
print(add5(2))
print('add5(3)')
print(add5(3))


#3. Фабрика, возвращающая список функций из примера 2
def add_range(start, end):
	return [addition(i) for i in range(start, end+1)]

q = add_range(0,5)
print('\n#3.\n q = add_range(0,5)')
print('>>> q\n', q)
print('a = q[3]\n>>> a(4.5)')
a = q[3]
print(a(4.5))


#4. Аналог MAP
def mapa(func, params):
	if hasattr(func, '__iter__'):
		return [tuple(f(param) for param in params) for f in func]
	else:
		return tuple(func(param) for param in list(params))

print('\n#4.\nmapa(q, [1,2,3])')
a = mapa(q, [1,2,3])
print(a)
