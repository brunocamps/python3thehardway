#Validar palavras que comecam com a, bc e a

#Bruno Marques de Campos
#825077
#Compiladores UNAERP 2018-2
#brunocamposdev@gmail.com

estado = 1

palavra = input('Digite uma palavra: ')

tamanho = len(palavra)
print(f"Tamanho da palavra é {tamanho} caracteres")

i = 0

for x in range(tamanho):
    if (palavra[x] == 'a'):
        estado = 1
    else:
        if(palavra[x] == 'b'):
            estado = 2
        else:
            estado = 99
            break

    if (palavra[x] == 'c'):
        estado = 3
    else:
        estado = 99
        break

    if (palavra[x] == 'a'):
        estado = 3
    else:
        estado = 99
        break


if (estado == 3):
    print(f"A palavra {palavra} é válida")
else:
    print(f"A palavra {palavra} é inválida")




