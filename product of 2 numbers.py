'''
name:Nicole Nelson
a python program to find product
'''
def mult_number(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+mult_number(n1,n2-1)
print(mult_number(5,4))