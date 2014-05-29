#!/usr/bin/env python

def get_calls():
    calls_file = open('./calls.txt')
    calls = calls_file.read()
    calls_file.close()
    return calls


# EXERCISE 1
# Obtener el gasto total de las llamadas
