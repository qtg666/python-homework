# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 15:59:43 2018

@author: qtg
"""

def spliter(x):
    assert 0<x<1000,'The number you input is out of range.'
    product=[]
    y=x
    i=2
    while i<=y:
        if y%i==0:
            product=product+[i]
            y=y/i
            i=2
        else:
            i+=1
    seq='×'    
    print(x,'=',seq.join([str(i) for i in sorted(product)]))
spliter(int(input('Please input a number between 0 and 1000:')))

