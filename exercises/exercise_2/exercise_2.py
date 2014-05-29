#!/usr/bin/env python

def get_text():
    text_file = open('trash.txt')
    text = text_file.read()
    text_file.close()
    return text


# EXERCISE 2
# Obtener la suma de los numeros
