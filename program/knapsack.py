#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re


def knapsack_bu(W, weight, cell):
    """
    Задача о рюкзаке

    Применяется динамическое программирование снизу вверх
    """
    def knapsack_with_reps(W, weight, cell):
        """
        Поиск максимальной стоимости предметов в рюкзаке.

        Предметы могут повторяться сколько угодно раз.
        """
        d = [0] * (W+1)
        for w in range(1, W+1):
            for weight_i, cell_i in zip(weight, cell):
                if weight_i <= w:
                    d[w] = max(d[w], d[w - weight_i] + cell_i)
        return d[W]

    def knapsack_without_reps(W, weight, cell):
        """
        Поиск максимальной стоимости предметов в рюкзаке.

        Предметы не могут повторяться.
        Так же функция возвращает solution, в которой 1 помечены элементы,
        которые были добавлены в рюкзак.
        """
        def restore(d, weight_rev, cell_rev):
            """
            Восстановление предметов в рюкзаке.

            Возвращает массив, где i элемент = 1,
            если предмет i был в рюкзаке,
            и 0, если нет.
            """
            solution = []
            w = W
            elem = len(weight_rev)
            for weight_i, cell_i in zip(weight_rev, cell_rev):
                if d[w][elem] == d[w - weight_i][elem-1] + cell_i:
                    solution.append(1)
                    w -= weight_i
                else:
                    solution.append(0)
                elem -= 1
            solution.reverse()
            return solution

        d = [[0] for _ in range(W+1)]
        d[0] = [0] * (len(weight) + 1)
        for weight_i, cell_i in zip(weight, cell):
            for w in range(1, W+1):
                d[w].append(d[w][-1])
                if weight_i <= w:
                    d[w][-1] = max(d[w][-1], d[w - weight_i][-2] + cell_i)

        solution = restore(d, weight[::-1], cell[::-1])

        return d[W][-1], solution

    with_rep = knapsack_with_reps(W, weight, cell)
    without_rep = knapsack_without_reps(W, weight, cell)

    return with_rep, without_rep


if __name__ == '__main__':
    W = 10
    weight = [6, 3, 4, 2]
    cell = [30, 14, 16, 9]
    with_rep_bu, without_rep_bu = knapsack_bu(W, weight, cell)
    print(f"{with_rep_bu = }\n{without_rep_bu = }")
