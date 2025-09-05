def cripto_cesar(texto,p):
    cifra = ''

    for i in range(len(texto)):
        char = texto[i]

        if(char.isupper()):
            cifra += chr((ord(char) + p - 65) % 26 + 65)
        else:
            cifra += chr((ord(char) + p - 97) % 26 + 97)
    return cifra

texto = input("Informe a o texto que deseja modificar: ")
p = int(input("Informe a o Padrao que ela deve segir: "))

print('texto: ',texto)
print('cifra: ' + cripto_cesar(texto,p))