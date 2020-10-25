import sys, math
from tkinter import *

def figures(x1, y1, x2, y2):
    # Круг, окружность
    radius = math.sqrt((x2-x1)**2+(y2-y1))
    c = 2 * math.pi * radius
    s = math.pi* radius ** 2
    if x1==x2==y1==y2:
        print('Длина окружности и площадь круга будут нулевыми')
    else:
        print('Окружность:')
        print('  диаметр окружности: {}, длина окружности: {}, площадь круга: {}.'.format(radius*2, c, s))
        print()

    # Прямоугольник
    a = abs(x1-x2)
    b = abs(y1-y2)
    p = 2*a + 2*b
    s = a*b
    if x1 == x2 or y1 == y2:
        print('Площадь прямоугольника будет нулевой')
    else:
        print('Прямоугольник:')
        print('  периметр прямоугольника: {}, площадь прямоугольника: {}.'.format(p, s))

    # Draw figures
    window = Tk()
    window.title("Тестовое задание, №1")
    canva = Canvas(window, width=800, height=600, bg='White')
    canva.pack()
    canva.create_rectangle(x1, y1, x2, y2)

    # т.к. в tkinter нет функции рисования круга, а есть рисование овала, вычисляем координаты для овала, принимаем x1,y1 за центр окружности
    xA = x1 + radius
    yA = y1 + radius
    xB = x1 - radius
    yB = y1 - radius
    canva.create_oval(xA, yA, xB, yB)

    window.mainloop()

#     ОСНОВНОЙ КОД
if __name__ == "__main__":
    print('Введите координаты через пробел: x1 y1 x2 y2')
    if len(sys.argv) != 5: # первый параметр - имя скрипта
        print('Команда запуска:')
        print('\tpython {0} <x1> <y1> <x2> <y2>'.format(sys.argv[0]))
        sys.exit(-1)
    try:
        x1 = int(sys.argv[1])
        y1 = int(sys.argv[2])
        x2 = int(sys.argv[3])
        y2 = int(sys.argv[4])
    except ValueError:
        print ('Cannot cast command line params to int()')
    except Exception:
        print('I don\'t know what is it!')
    else:
        figures(x1, y1, x2, y2)