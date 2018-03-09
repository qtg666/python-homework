# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 15:59:43 2018

@author: qtg
"""

def spliter(x):
    assert 0<x<1000,'The number you input is out of range.'#确保输入的数范围在1~1000内
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
    print(x,'=',seq.join([str(i) for i in sorted(product)]))#通过这种方法消去列表的中括号并插入乘号
spliter(int(input('Please input a number between 0 and 1000:')))

