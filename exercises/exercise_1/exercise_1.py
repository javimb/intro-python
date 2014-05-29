#!/usr/bin/env python

import urllib2

def get_calls():
    url = 'https://raw.githubusercontent.com/javimb/intro-python/master/exercises/exercise_1/calls.txt'
    return urllib2.urlopen(url).read()


# EXERCISE 1
# Obtener el gasto total de las llamadas
