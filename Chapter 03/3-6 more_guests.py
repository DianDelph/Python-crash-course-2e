#retoma la lista de invitados de 3-5. Agrega más invitados a la lista.

guests_list = ['ada', 'mary', 'ursula']

print('Hay espacio para más personas \n')

guests_list.insert(0, 'tammy') #agrega una invitada al inicio de la lista
guests_list.insert(2, "wynne")  # agrega una invitada en el lugar 2 del índice (3 real)
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
