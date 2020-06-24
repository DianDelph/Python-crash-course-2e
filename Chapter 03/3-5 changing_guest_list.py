#retoma la lista de 3-4. Avisa que una invitada no vendrá, modifica la lista con otra invitada e imprime otro set de invitaciones

guests_list = ['ada', 'mary', 'ursula']

message = f'¡Hola {guests_list[0].title()}!, ¿quieres ir a comer?'
print(message)

message = f'¡Hola {guests_list[1].title()}!, ¿quieres ir a comer?'
print(message)

message = f'¡Hola {guests_list[2].title()}!, ¿quieres ir a comer?'
print(message)

print(f'\t Parece que {guests_list[1].title()} no podrá venir')

guests_list[1] = 'tammy'

print
