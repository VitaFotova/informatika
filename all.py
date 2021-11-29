import math
import time

def my_shiny_new_decorator(function_to_decorate):
     # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
     # получая возможность исполнять произвольный код до и после неё.
     def the_wrapper_around_the_original_function():
         starttimeofthefunkcia = time.time()
         print("1. Была вызвана функция [имя этой функции %s]" % function_to_decorate.__name__)
         function_to_decorate() # Сама функция
         timeoftheexecution = time.time() - starttimeofthefunkcia
         print("2.	Время, затраченное на выполнение функции. %s" % timeoftheexecution)
     # Вернём эту функцию
     return the_wrapper_around_the_original_function

@my_shiny_new_decorator
def f1():
 b = int(input('Введите длину: '))
 c = int(input('Введите ширину: '))
 SQFT_PER_ACRE  = .000022956841 * b * c 
 print(SQFT_PER_ACRE, 'акров')

@my_shiny_new_decorator
def f2():
 a = 9.8
 d = int(input('Введите дистанцию: '))
 vf = math.sqrt(2 * a * d)
 print('Скорость при соприкосновении тела с землей %s м/с^2' % vf)

f1()

f2()