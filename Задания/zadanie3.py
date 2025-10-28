#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    t = tuple(map(int, input().split()))

    index_last = -1

    for i in range(1, len(t) - 1):
        if t[i] > t[i - 1] and t[i] > t[i + 1]:
            index_last = i - 1

    if index_last != -1:
        print(t[:index_last])
    else:
        print("Подходящих троек нет", file=sys.stderr)