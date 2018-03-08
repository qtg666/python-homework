
# coding: utf-8

# In[5]:


def examer(x):
    if x%400==0:
        print('The year you input is a leap year.')
    else:
        if x%4==0:
            if x%100==0:
                print('The year you input is not a leap year.')
            else:
                print('The year you input is a leap year.')
        else:
            print('The year you input is not a leap year.')
examer(int(input('Please input a year to be examed:')))

