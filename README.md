# solution_python_tasks
- Решения заданий по языку python для обучения с сайта www.pyobjects.ru (Yury Yurevich)
- Задачи на языке Python для обучения и собеседований.
- ИСТОЧНИК:  http://pyobject.ru/blog/2010/02/04/python-quiz/ (доступ 08.05.2017)


# Вопросы и задания по Python ∞

>"Меня периодически спрашивают о тестовых заданиях по Python-тематике. Я решил обобщить вопросы и написать их в одном месте. Я не использую эти вопросы и задания в собеседованиях, но использую при обучении."

## Типы данных, основные конструкции

1. Как получить список всех атрибутов объект
2. Как получить список всех публичных атрибутов объекта
3. Как получить список методов объекта
4. В какой "магической" переменной хранится содержимое help?
5. Есть два кортежа, получить третий как конкатенацию первых двух
6. Есть два кортежа, получить третий как объединение уникальных элементов первых двух кортежей
7. Почему если в цикле меняется список, то используется for x in lst[:], что означает [:]?
8. Есть два списка одинаковой длины, в одном ключи, в другом значения. Составить словарь.
9. Есть два списка разной длины, в одном ключи, в другом значения. Составить словарь. Для ключей, для которых нет значений использовать None в качестве значения. Значения, для которых нет ключей игнорировать.
10. Есть словарь. Инвертировать его. Т.е. пары ключ: значение поменять местами — значение: ключ.
11. Есть строка в юникоде, получить 8-битную строку в кодировке utf-8 и cp1251
12. Есть строка в кодировке cp1251, получить юникодную строку

## Функции

1. Написать функцию, которой можно передавать аргументы либо списком/кортежем, либо по одному. Функция производит суммирование всех аргументов.
2. Написать функцию-фабрику, которая будет возвращать функцию сложения с аргументом.
3. Написать фабрику, аналогичную п.2, но возвращающей список таких функций
4. Написать аналог map:

## Итераторы

1. Написать функцию-генератор cycle которая бы возвращала циклический итератор.
2. Написать функцию-генератор chain, которая последовательно итерирует переданные объекты (произвольное количество)

## Модули

1. У нас есть импортированный модуль foo, как узнать физический путь файла, откуда он импортирован?
2. Из модуля foo вы импортируете модуль feedparser. Версия X feedparser'а есть в общесистемном каталоге site-packages, версия Y — рядом с модулем foo. Определена переменная окружения PYTHONPATH, и там тоже есть feedparser, версии Z. Какая версия будет использоваться?
3. Как посмотреть список каталогов, в которых Python ищет модули?
4. У вас есть модуль foo, внутри него импортируется модуль bar. Рядом с модулем foo есть файлы bar.py и bar/__init__.py Какой модуль будет использоваться.
5. Что означает и для чего используется конструкция __name__ == '__main__'

## Классы

1. Написать базовый класс Observable, который бы позволял наследникам: при передаче ****kwargs заносить соответствующие
- значения как атрибуты
- сделать так, чтобы при print отображались все публичные атрибуты
2. Написать класс, который бы по всем внешним признакам был бы словарем, но позволял обращаться к ключам как к атрибутам.
3. Пункт 2 с усложнением: написать родительский класс XDictAttr так, чтобы у наследника динамически определялся ключ по наличию метода get_'KEY'.
4. Написать класс, который регистрирует свои экземпляры и предоставляет интерфейс итератора по ним

## Метаклассы и дескрипторы

### Вопросы:

1. Для чего используются, какие аргументы получают, что должны возвращать: методы __new__ и __init__ классов
2. Какие аргументы получает __new__ и __init__ у метакласса?

### Задания:

1. Реализовать дескрипторы, которые бы фиксировали тип атрибута
2. Реализовать базовый класс (используя метакласс), который бы фиксировал тип атрибута
3. Реализовать базовый класс (используя метакласс) и дескрипторы, которые бы на основе класса создавали SQL-схему (ANSI SQL) для модели:

#python #learning
