#1. Путь к импортированному модулю
try:
	import data_types
	print('+'*22)
	print('\n#1. Путь к модулю: {}'.format(data_types.__file__))
except ImportError:
	print('#1. Импорт не удался')


#2. Откуда будет импорт
import sys
print('\n#2. ПОРЯДОК ИМПОРТИРОВАНИЯ : {}'.format(sys.path))


#3. Список каталогов, где python ищет
print('\n#3. ГДЕ ИЩЕТ : {}'.format(sys.path))


#4. Сначала импортируется папка с __init__.py или файл
print('\n#4. PYTHON ОТДАЕТ ПРИОРИТЕТ ИМПОРТУ ПАКЕТОВ')


#5. для чего __name__ == '__main__' 
class Program:
	def hello(self):
		print('Hello world')

if __name__ == '__main__':
	print('\n#5. При условии __name__ == "__main__" запускается \
		тело условия, если модуль запущен как скрипт (не импортирован)')
	Program().hello()