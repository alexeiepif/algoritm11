#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


def fib(n, func="TD"):
    """
    Функции вычисления числа фибоначчи.

    Вызывает fib_td если funk="TD".
    Вызывает fib_bu если funk="BU".
    Вызывает fib_bu_improved если funk="BU_I".
    """

    def fib_td(n):
        """
        Вычисление числа фибонначи с помощью динамического программирования.

        Используется динамическое программирование назад.
        """
        if n <= 1:
            f[n] = n
        else:
            f[n] = fib_td(n - 1) + fib_td(n-2)
        return f[n]

    def fib_bu(n):
        """
        Вычисление числа фибонначи с помощью динамического программирования.

        Используется динамическое программирование вперед.
        """
        f = [-1]*(n+1)
        f[0], f[1] = 0, 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]

    def fib_bu_imroved(n):
        """
        Вычисление числа фибонначи с помощью динамического программирования.

        Используется динамическое программирование с уменьшенным количеством
        потребляемой памяти.
        """
        if n <= 1:
            return n
        prev, curr = 0, 1
        for _ in range(n - 1):
            prev, curr = curr, prev + curr
        return curr

    match func:
        case "TD":
            f = [-1]*(n+1)
            return fib_td(n)
        case "BU":
            return fib_bu(n)
        case "BU_I":
            return fib_bu_imroved(n)
        case _:
            print(f"Неизвестраня функция {func}", file=sys.stdeer())
            exit(1)


if __name__ == '__main__':
    N = 10
    print(f"\nФибоначчи({N}) разными функциями:")
    print(f"{fib(N, "TD") = }")
    print(f"{fib(N, "BU") = }")
    print(f"{fib(N, "BU_I") = }")
