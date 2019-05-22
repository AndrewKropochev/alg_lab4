# -*- coding: utf-8 -*-
import random

def quick_sort(lst, low=0, high=None):
    
    if(len(lst) <= 1): return(lst)
    def subpart(lst, low, high, pivot_index):
        lst[low], lst[pivot_index] = lst[pivot_index], lst[low]
        pivot = lst[low]
        x = low + 1
        y = low + 1
        
        while y <= high:
            if lst[y] <= pivot:
                lst[y], lst[x] = lst[x], lst[y]
                x += 1
            y += 1

        lst[low], lst[x - 1] = lst[x - 1], lst[low]
        return x - 1

    if high is None:
        high = len(lst) - 1
    
    if high - low < 1:
        return 

    pivot_index = random.randint(low, high)
    x = subpart(lst, low, high, pivot_index)
    quick_sort(lst, low, x - 1)
    quick_sort(lst, x + 1, high)
    return(lst)
    
