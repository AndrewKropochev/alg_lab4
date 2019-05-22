#!/usr/bin/env python
# -*- coding: utf-8 -*-

def insertion_sort(a):
    for i in range(len(a)):
        key = a[i]
        j = i - 1
        while (j >= 0 and a[j] > key):
            a[j+1] = a[j]
            j = j -1
        a[j+1] = key
    return(a)
    pass
