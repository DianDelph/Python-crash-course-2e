#retoma la lista de 3-6 y deja sólo dos invitadas usando pop(). Imprime un mensaje personalizado  a cada invitada avisándole. Elimina la lista y demuestra que está borrada

#primera lista 3-4. Invitaciones

guests_list = ['ada', 'mary', 'ursula']

message = f'¡Hola {guests_list[0].title()}!, ¿quieres ir a comer?'
print(message)

message = f'¡Hola {guests_list[1].title()}!, ¿quieres ir a comer?'
print(message)

message = f'¡Hola {guests_list[2].title()}!, ¿quieres ir a comer?'

print(message)

#3-5 una invitada no podrá asistir

print(f'\n Parece que {guests_list[1].title()} no podrá venir')

guests_list[1] = 'tammy'  # reemplazo la invitada que no vendrá por la que sí

#re imprimo lista de invitados

print('\n Segunda lista\n')

message = f'¡Hola {guests_list[0].title()}!, ¿quieres ir a comer?'
print(message)

message = f'¡Hola {guests_list[1].title()}!, ¿quieres ir a comer?'
print(message)

message = f'¡Hola {guests_list[2].title()}!, ¿quieres ir a comer?'
print(message)


print('Hay espacio para más personas \n')

guests_list.insert(0, 'Leonora')  # agrega una invitada al inicio de la lista
# agrega una invitada en el lugar 2 del índice (3 real)
guests_list.insert(2, "wynne")
guests_list.append('isa')  # agrega una invitada al final de la lista

message = f'¡Hola {guests_list[0].title()}!, ¿quieres ir a comer?'
print(message)

message = f'¡Hola {guests_list[1].title()}!, ¿quieres ir a comer?'
print(message)

message = f'¡Hola {guests_list[2].title()}!, ¿quieres ir a comer?'
print(message)

message = f'¡Hola {guests_list[3].title()}!, ¿quieres ir a comer?'
print(message)

message = f'¡Hola {guests_list[4].title()}!, ¿quieres ir a comer?'
print(message)

message = f'¡Hola {guests_list[5].title()}!, ¿quieres ir a comer?'
print(message)

#3-7 no hay suficiente espacio.

print('\n ¡Vaya, parece que no hay suficientes lugares!')

guest = guests_list.pop() #remueve el último elemento de la lista y lo guarda en la variable
print(f'Lo siento {guest.title()} ya no hay lugar en la mesa')


guest = guests_list.pop()
print(f'Lo siento {guest.title()} ya no hay lugar en la mesa')

guest = guests_list.pop()
print(f'Lo siento {guest.title()} ya no hay lugar en la mesa')

guest = guests_list.pop()
print(f'Lo siento {guest.title()} ya no hay lugar en la mesa')


#imprimo mensaje a las que quedan

message = f'¡Hola {guests_list[0].title()}!, ¿quieres ir a comer?'
print(message)

message = f'¡Hola {guests_list[1].title()}!, ¿quieres ir a comer?'
print(message)

#borro los elementos de la lista

del(guests_list[0])
del(guests_list[0]) #lleva 0 porque se recorre al nuevo índice al borrarse el anterior

print(guests_list) #comprueba que esté vacía la lista
