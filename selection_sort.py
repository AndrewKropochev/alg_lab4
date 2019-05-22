#!/usr/bin/env python
# -*- coding: utf-8 -*-

def selection_sort(array):
    for i in range(len(array) - 1):
        m = i
        for j in range((i+1), len(array)):
            if (array[j] < array[m]):
                m = j
        
        array[i], array[m] = array[m], array[i]
    return(array)
    pass
