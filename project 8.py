'''
author name:nicole nelson
date:08-10-2024
python program to extract first name
'''
first_name=input("enter your name:")
last_name=input("enter your last name:")
full_name=first_name+" "+last_name
print(full_name)
length=len(first_name)
print("first_name=",full_name[:length])