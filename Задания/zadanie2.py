#!/usr/bin/env python3
#-*- coding: utf-8 -*-

if __name__ == '__main__':
    summa = 0
    spisok = list(map(int, input().split()))

    start = spisok[0]
    for i in spisok:
        if abs(i) < abs(start):
            start = i

    if 0 in spisok:
        nol = spisok.index(0)
        for i in spisok[nol:]:
            summa += abs(i)
    else:
        summa = "В списке нет нуля"

    spisok = spisok[::2] + spisok[1::2]
    print(start, summa)
    print(spisok)