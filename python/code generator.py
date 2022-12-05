#!/usr/bin/env python
import random

def randpasswd(length, chars=None):
    if chars == None:
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%¨&*()_+/*\\|<>;:"

    password = ""
    for i in range(length):
        password += random.choice(chars)

    return password

def randnumbah(length, nums=None):
    if nums == None:
        nums = "0123456789"

    pw = ""
    for i in range(length):
        pw += random.choice(nums)

    return pw

#omit this if you just want the function
print(randpasswd(10))

print(randnumbah(10))