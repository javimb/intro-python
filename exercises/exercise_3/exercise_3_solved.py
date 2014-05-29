#!/usr/bin/env python

# EXERCISE 3
# Imprimir (separados por comas) todos los numeros que son divisibles entre 7 pero
# no son multiplos de 5, que esten entre 2000 y 3200 (ambos incluidos)


nums = [str(x) for x in range(2000, 3201) if not x % 7 and x % 5 != 0]
print ','.join(nums)

nums = map(str, filter(lambda x: not x % 7 and x % 5 != 0, range(2000, 3201)))
print ','.join(nums)
