#!/usr/bin/env python

def get_text():
    text_file = open('trash.txt')
    text = text_file.read()
    text_file.close()
    return text


# EXERCISE 2
# Obtener la suma de los numeros

text = get_text()
nums = filter(lambda num: num in '0123456789', text)
int_nums = map(int, nums)

print sum(int_nums)
