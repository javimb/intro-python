#!/usr/bin/env python

import urllib2

def get_calls():
    url = 'https://raw.githubusercontent.com/javimb/intro-python/master/exercises/exercise_1/calls.txt'
    return urllib2.urlopen(url).read()


# EXERCISE 1
# Obtener el gasto total de las llamadas

calls = get_calls()
total = 0

for line in calls.split('\n'):
    total += float(line.split()[-1].replace(',', '.'))

print total
