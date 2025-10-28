#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

if __name__ == '__main__':

    spisok = list(input().split())

    poisk = input("Введите элемент: ")
    schet = 0

    for i in spisok:
        if i == poisk:
            print(schet)
        schet += 1

    if schet == 0:
        print("Заданного элемента в списке нет", file=sys.stderr)
