#1. Написать циключескую функцию генератор

def cycle(iters):
	while True:
		for it in iters:
			yield it

q 	= cycle([1,3,5])

print('\n#1. ЦИКЛИЧЕСКИЙ ГЕНЕРАТОР:\nq = cycle([1,3,5])')
for i in range(10):
	print(next(q))


#2. Напсиать chain. которая последовательно итерирует переданные объектв

def chain(*args):
	for arg in args:
		yield from arg

q 	= chain([1,2,3],(5,6,7))

print('\n#2. ГЕНЕРАТОР ПО ВСЕМ ЧТО ВСУНУЛИ\nq = chain([1,2,3],(5,6,7))')
for i in range(9):
	print(next(q))