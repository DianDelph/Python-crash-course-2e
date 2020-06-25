#crea una lista con los números 1-1,000,000. Busca valor mínimo y valor máximo. Suma toda la lista.

#usa range() para crer una lista con un rango dado
numbers_list = list(range(1,1_000_001))

#busca el número más pequeño para comprobar que la lista comienza desde 1.
print(min(numbers_list))

#busca el número más grande para comprobar que la lista termina en un millón.
print(max(numbers_list))

#suma todos los números de la lista.
print(sum(numbers_list))

