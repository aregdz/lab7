# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = list(map(float, input("Введите элементы списка: ").split()))
    a = int(input("Введите значения a: "))
    b = int(input("Введите значения b: "))
    print(f"Максимальный элемент списка - {max(A)}")
    l = 0
    for i, item in enumerate(A):
        if item > 0:
            l = i

    s = sum(A[:l+1])
    print(f"Cумма элементов списка, расположенных до последнего положительного элемента - {s}")

    d = [i for i in A if abs(i)>a and abs(i)<b]
    print(f"Сжатый список - {d}")

    la = len(A)
    ld = len(d)
    while ld != la:
        d.append(0)
        ld = len(d)
    print(f"Список с добавлёнными 0 - {d}")