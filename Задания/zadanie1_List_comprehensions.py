#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    spisok = list(input().split())

    poisk = input("Введите элемент: ")
    naiden = [i for i, elem in enumerate(spisok) if elem == poisk]

    if len(naiden) == 0:
        print("Заданного элемента в списке нет", file=sys.stderr)
    else:
        print(naiden)