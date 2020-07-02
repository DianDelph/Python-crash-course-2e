#toma la lista del ejercicio 4-9 y usa slices para: imprimir los primeros tres números, los tres de en medio y los tres el final.

#crea la lista de cubos
cubes = [value**2 for value in range(1, 11)]

#imprime los primeros tres numeros
print('Los primeros tres números son: ')
for cube in cubes[:3]:
	print(cube)

#imprime los  tres numeros de en medio
print('Los tres números de en medio son: ')
for cube in cubes[3:6]:
	print(cube)

#imprime los primeros tres numeros
print('Los últimos tres números son: ')
for cube in cubes[-3:]:
	print(cube)