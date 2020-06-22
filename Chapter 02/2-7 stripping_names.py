#quita el espacio en blanco de una variable

full_name = "\tAda Lovelace\n"

print("Sin modificaciones")
print(full_name)

print("\nAplicando lstrip()") 
print(full_name.lstrip()) #quito el espacio de la izquierda

print("\nAplicando rstrip()")
print(full_name.rstrip()) #quito el espacio de la derecha

print("\nAplicando strip()")
print(full_name.strip()) #quito el espacio de ambos lados

