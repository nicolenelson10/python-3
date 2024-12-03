'''
name:Nicole Nelson
a python program to greatest common digit
'''
def gcd_number(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd_number(n2,n1%n2)
print(gcd_number(48,18))