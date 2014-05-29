#!/usr/bin/env python

# EXERCISE 4
# Cambia el bloque de codigo modificable para que el tiempo de ejecucion
# se menor de 0.001 segundos
# AVISO: zero = 0 no es valido!

import time

start = time.time()

# Bloque de codigo modificable
zero = xrange(1000000)[0]
####

print 'Time: ', time.time() - start
