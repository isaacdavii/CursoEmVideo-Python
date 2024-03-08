lista = []
listaPar = []
listaImpar = []

while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    if numero % 2 == 0:
        listaPar.append(numero)
    elif numero % 2 == 1:
        listaImpar.append(numero)
    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    if continuar == "N":
        break
    while continuar not in 'SN':
        print("Opção Inválida! Tente novamente!")
        continuar = input("Quer continuar? [S/N]: ").upper().strip()
        
print(f'Lista: {sorted(lista)}')
print(f'Lista Par: {listaPar}')
print(f'Lista Impar: {listaImpar}')