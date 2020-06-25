#crea una lista de lugares, las ordena normal y reversed.

#crea la lista
places_list = ['vancouver', 'auckland','oslo', 'barcelona','londres']

#imprime 
print('lista original')
print(places_list)

#usa sorted() para imprimir la lista en orden alfabético sin modificar la original.
print('\nlista con sorted()')
print(sorted(places_list))

#muestra lista original
print('lista original')
print(places_list)

#usa sorted(reverse=True) para imprimir la lista en orden alfabético inverso sin modificar la original.
print('\nlista con sorted(reverse=True)')
print(sorted(places_list, reverse=True))

#muestra lista original
print('lista original')
print(places_list)

#usa reverse() para cambiar el orden de la lista original
print('\nLista con reverse()')
places_list.reverse()
print(places_list)

#vuelve a usar reverse() para regresar al orden original.
print('\nLista otra vez con reverse()')
places_list.reverse()
print(places_list)

#usa sort para ordenar alfabéticamente la lista original.
print('\nLista con sort()')
places_list.sort()
print(places_list)

#usa sort(reverse=True) para ordenar la lista original en orden inverso alfabéticamente.
print('\nLista con orden alfabético inverso')
places_list.sort(reverse=True)
print(places_list)