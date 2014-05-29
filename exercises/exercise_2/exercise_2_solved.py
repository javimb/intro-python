#!/usr/bin/env python

import urllib2

def get_text():
    url = 'https://raw.githubusercontent.com/javimb/intro-python/master/exercises/exercise_2/trash.txt'
    return urllib2.urlopen(url).read()


# EXERCISE 2
# Obtener la suma de los numeros

text = get_text()
nums = filter(lambda num: num in '0123456789', text)
int_nums = map(int, nums)

print sum(int_nums)
