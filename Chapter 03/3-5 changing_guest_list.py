#retoma la lista de 3-4. Avisa que una invitada no vendrá, modifica la lista con otra invitada e imprime otro set de invitaciones

guests_list = ['ada', 'mary', 'ursula']

message = f'¡Hola {guests_list[0].title()}!, ¿quieres ir a comer?'
print(message)

message = f'¡Hola {guests_list[1].title()}!, ¿quieres ir a comer?'
print(message)

message = f'¡Hola {guests_list[2].title()}!, ¿quieres ir a comer?'
print(message)

print(f'\n Parece que {guests_list[1].title()} no podrá venir')

guests_list[1] = 'tammy' #reemplazo la invitada que no vendrá por la que sí

#re imprimo lista de invitados

print('\n Segunda lista\n')

message = f'¡Hola {guests_list[0].title()}!, ¿quieres ir a comer?'
print(message)

message = f'¡Hola {guests_list[1].title()}!, ¿quieres ir a comer?'
print(message)

message = f'¡Hola {guests_list[2].title()}!, ¿quieres ir a comer?'
print(message)