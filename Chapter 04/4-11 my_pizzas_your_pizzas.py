#usa el la lista de 4-1, para copiar listas y modificarlas.

pizzas_list = ['mexicana','pepperoni','margarita']

#copia la lista a una nueva

friend_pizzas = pizzas_list[:]

#agrega una pizza a la lista original

pizzas_list.append('quesos')

#agrega una pizza diferente a la nueva lista

friend_pizzas.append('berenjena')

#comprueba que las listas son diferentes. Primero imprime la lista original y luego la nueva.

print('Mis pizzas favoritas son:')
for pizza in pizzas_list:
	print(pizza)

print('\nLas pizzas favoritas de mi amiga son:')
for pizza in friend_pizzas:
	print(pizza)

