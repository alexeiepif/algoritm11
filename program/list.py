#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def list_bottom_up(a):
    """
    Поиск длины НВП.
    """
    d = []
    for i, _ in enumerate(a):
        d.append(1)
        for j in range(i):
            if a[j] < a[i] and d[j] + 1 > d[i]:
                d[i] = d[j]+1

    ans = max(d)
    return ans


def list_bottom_up2(a):
    """
    Поиск длины и самой НВП.

    Сама НВП ищется двумя способами:
    с помощью дополнительного списка prev;
    без помощи дополнительного списка.
    """
    def restore_using_prev(m_index):
        """
        Восстановление НВП с помощью списка prev
        """
        l = []
        while True:
            l.append(m_index)
            if prev[m_index] == -1:
                break
            m_index = prev[m_index]

        l.reverse()
        return l

    def restore_without_prev(ans, m_index):
        """
        Восстановление НВП без помощи списка prev
        """
        l = []
        while True:
            l.append(m_index)
            if ans == 1:
                break
            ans -= 1
            while True:
                m_index -= 1
                if d[m_index] == ans and a[m_index] < a[l[-1]]:
                    break
        l.reverse()
        return l

    d, prev = [], []
    for i, _ in enumerate(a):
        d.append(1)
        prev.append(-1)
        for j in range(i):
            if a[j] < a[i] and d[j] + 1 > d[i]:
                d[i] = d[j]+1
                prev[i] = j

    ans, max_index = 0, 0
    for i, item in enumerate(d):
        if ans < item:
            ans, max_index = item, i

    list_using_prev = restore_using_prev(max_index)
    list_without_prev = restore_without_prev(ans, max_index)

    return ans, (list_using_prev, list_without_prev)


if __name__ == '__main__':
    a = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]
    print(list_bottom_up(a))
    print(list_bottom_up2(a))
