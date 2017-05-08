#1. Класс Observable
# наследники получают kwargs как пттрибуты
# при print показываются имя класса и все публичные аттрибуты
class Observable:
	def __init__(self, **kwargs):
		for key in kwargs:
			self.__dict__[key] = kwargs[key]
	def __str__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join(
				'{}={}'.format(key, val)
				for key,val in self.__dict__.items() if not key.startswith('_')
			)
		)
class X(Observable):
	pass

print('\n#1. Класс Observable. Его наследники получают параметры и выдают как атрибуты.')
q = X(a=1,b=2)
print(q)
print(q.a, q.b)


#2. Написать класс, по всем признакам как словарь + доступ по аттрибутам
class DictAttr(dict):
	def __getattr__(self, key):
		return self[key]

print('\n#2. Класс DictAttr. по всем признакам как словарь + доступ по аттрибутам.')
d = DictAttr([('one', 1), ('two', 2)])
print("d = DictAttr([('one', 1), ('two', 2)])")
print('>>> d.one\n{}'.format(d.one))
print('>>> d.get("two")\n{}'.format(d.get('two')))
print('>>> d.get("three", "not exist")\n{}'.format(d.get('three', 'not exist')))
try:
	print('>>> d.four\n{}'.format(d.four))
except KeyError:
	print('AttrributeError')


#3. Написать родительский класс XDictAttr, чтобы у наследника определялся аттрибут при наличии метода get_<KEY>
class XDictAttr(dict):
	def __getattr__(self, key):
		if 'get_{}'.format(key) in self.__class__.__dict__:
			return self.__class__.__dict__['get_{}'.format(key)](self)
		elif key in self.keys():
			return self[key]

class X(XDictAttr):
	def get_three(self):
		return 3

print('\n#3. Класс XDictAttr, чтобы у наследника определялся аттрибут при наличии метода get_<KEY>.')
print('class X(XDictAttr):\n\tdef get_three(self):\n\t\treturn 3')
x = X([('one', 1), ('two', 2)])
print("x = X([('one', 1), ('two', 2)])")
print('>>> x.one')
print('{}'.format(x.one))
print('>>> x.get("two")')
print('{}'.format(d.get('two')))
print('>>> d.three')
print('{}'.format(x.three))


#4. Класс регистратор и предоставляет иньервейс итератора по ним

class Reg:
	__safe = []
	def __init__(self):
		self.__safe.append(self)

	def __iter__(self):
		return (i for i in self.__safe)

x = Reg()
y = Reg()
print('\n#4. Класс регистратор и предоставляет иньервейс итератора по ним')
print('x => {}'.format(x))
print('y => {}'.format(y))
for i in Reg():
	print(i)

