#!/usr/bin/env python

def get_calls():
    calls_file = open('calls.txt')
    calls = calls_file.read()
    calls_file.close()
    return calls


# EXERCISE 1
# Obtener el gasto total de las llamadas

calls = get_calls()
total = 0

for line in calls.split('\n'):
    total += float(line.split()[-1].replace(',', '.'))

print total
