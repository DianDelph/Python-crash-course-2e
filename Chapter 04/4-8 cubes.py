# calcula los cubos del 1-10 y los integra en una lista

cubes_list = []

#crea lista. cada valor dentro de 1-11 lo eleva al cubo y lo anexa a la lista
for value in range(1,11):
	cubes_list.append(value**3)

#imprime lista
for cube in cubes_list:
	print(cube)
