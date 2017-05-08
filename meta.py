import abc

# ВОПРОСЫ
#1. Для чего используются, какие аргументы получают, что должны возвращать методы __new__, __init__

# __new__ - принимает объект класса, возвращает его экземпляр. КОНСТРУКТОР
# q = Q.__new__(Q)
# __init__ - принимает экземпляр и значения аттрибутов. Ничего не возвращает. ИНИЦИАЛИЗАТОР
# Q.__init__(q, *args, **kwargs)

#2. Какие аргументы получают __new__ & __init__ у метакласса

##********************

# ЗАДАНИЯ

# 1. Дескрипторы, которые классифицируют тип аттрибута
print('######## 1 #############')
class Property:

	__counter = 0

	def __init__(self, value):
		self.__type			= type(value)
		self.__attr 		= '{}#{}'.format(self.__class__.__name__, self.__counter)
		self.__value		= value
		Property.__counter	+= 1
	
	def __set__(self, instance, value):
		if type(value) == self.__type:
			instance.__dict__[self.__attr] = value
		else:
			raise TypeError ('Value must be: {}'.format(self.__type))

	def __get__(self, instance, objtype=None):
		try:
			return instance.__dict__[self.__attr]
		except KeyError:
			return self


class Image(object):
	
	height 	= Property(0)
	width 	= Property(0)
	path	= Property('/tmp/')


##############################################################
##############################################################
#2. Реализовать базовый класс, который бы фиксировал аттрибуты
print('######## 2 #############')
import abc


class AutoStorage:

	def __init__(self, key):
		self.__attr 		= '#{}'.format(key)
	
	def __set__(self, instance, value):
		setattr(instance, self.__attr, value)

	def __get__(self, instance, objtype=None):
		if instance is None:
			return self
		else:
			return getattr(instance, self.__attr)
		

class Validated(abc.ABC, AutoStorage):

	def __set__(self, instance, value):
		value = self.validate(instance, value)
		super().__set__(instance, value)

	@abc.abstractmethod
	def validate(self, instance, value):
		"""ABSTRACT METHOD VALIDATE"""


class Quantity(Validated):

	def validate(self, instance, value):
		if value > 0:
			return value
		else:
			raise ValueError('must be > 0')


class NonBlank(Validated):

	def  validate(self, instance, value):
		if type(value) is not str:
			raise TypeError ('must be {}'.format(type(str)))
		elif len(value) < 1:
			raise ValueError ('Must not blank')

		return value



class ObjectMeta(type):

	def __init__(cls, name, bases, attr):
		if len(bases) >= 0:
			for key,value in attr.items():
				if not key.startswith('_'):
					if isinstance(value, int):
						setattr(cls, '{}'.format(key), Quantity(key))
					if isinstance(value, str):
						setattr(cls, '{}'.format(key), NonBlank(key))


class Object(metaclass=ObjectMeta):
	"""'instance of metaclass"""


class Image(Object):
	height 	= 0
	width	= 5
	path	= '/tmp'
	size 	= 0

img = Image()
img.height 	= 2
img.width	= 5
img.path	= 'user/exapmles'
img.size 	= 2

print(img.height, img.width, img.path, img.size)

###############################################################
###############################################################
""""
3. Реализовать базовый класс (используя метакласс) и дескрипторы,
которые бы на основе класса создавали SQL-схему (ANSI SQL) для модели
"""
print('######## 3 #############')
class Str:
	__counter = 0

	def __init__(self, length):
		self.length 	= length
		self.__attr		= '_{}#{}'.format(
				self.__class__.__name__.lower(),
				self.__counter
			)

		self.__counter += 1

	def __set__(self, instance, value):
		if isinstance(value, str):
			setattr(instance, self.__attr, value)
		else:
			raise TypeError('MUST be STR')

	def __get__(self, instance, objtype=None):
		if not instance is None:
			return getattr(instance, self.__attr)
		else:
			return self

	def sql_type(self):
		return 'varchar({})'.format(self.length)


class Integer:
	__counter = 0

	def __init__(self):
		self.__attr		= '_{}#{}'.format(
				self.__class__.__name__.lower(),
				self.__counter
			)
		self.__counter += 1

	def __set__(self, instance, value):
		if isinstance(value, int):
			setattr(instance, self.__attr, value)
		else:
			raise TypeError('MUST be INT')

	def __get__(self, instance, objtype=None):
		if not instance is None:
			return getattr(instance, self.__attr)
		else:
			return self

	def sql_type(self):
		return 'integer'



class TableMeta(type):
	def __init__(self, name, bases, attr):
		self.name = name
		if len(bases) > 0:
			self.fields = {}
			for key,value in attr.items():
				if not key.startswith('_'):
					self.fields[key] = value.sql_type()
			self.sql 	= self.sql_create

	def sql_create(self):
		test 	= "CREATE TABLE {name} (\n\t{attrs}\n)"
		name 	= self.name.lower()
		pairs 	= tuple(key + ' ' + val for key,val in self.fields.items())
		attrs	= test.format(name=name, attrs=',\n\t'.join(pairs))
		return attrs

	

class Table(metaclass=TableMeta):
	"""Meta Table instance"""
	def sql(self):
		return ''

class Image(Table):
	height 	= Integer()
	width	= Integer()
	path	= Str(128)
	size 	= Integer()

img = Image()
print(img.sql())
